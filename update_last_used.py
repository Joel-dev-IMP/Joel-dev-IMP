#!/bin/python
import duckdb

import re
import readline
from pathlib import Path


def main() -> None:
    db = duckdb.connect(":memory:")
    HIST_FILE = Path.home() / ".update_last_used_history"

    if HIST_FILE.exists():
        deduplicated_history: list[str] = []
        full_history: list[str] = []
        with HIST_FILE.open("r") as f:
            full_history = f.readlines()

        for item in reversed(full_history):
            if item not in deduplicated_history:
                deduplicated_history.append(item)

        with HIST_FILE.open("w") as f:
            f.writelines(reversed(deduplicated_history))

    try:
        readline.read_history_file(HIST_FILE)
        initial_history_length = readline.get_current_history_length()
    except FileNotFoundError:
        HIST_FILE.open("w+").close()
        initial_history_length = 0

    readline.set_auto_history(True)

    db.sql("""CREATE TABLE tools_and_skills (
    id INTEGER NOT NULL,
    name VARCHAR PRIMARY KEY,
    category VARCHAR NOT NULL,
    last_used DATE NOT NULL,
    update_count INTEGER NOT NULL,
    comment VARCHAR
);""")

    db.sql("""INSERT INTO
    tools_and_skills
SELECT
    row_number() OVER (
        ORDER BY
            category,
            name
    ) AS id,
    *,
FROM
    'tools_and_skills.csv'
ORDER BY
    category,
    name;
""")

    print(db.sql("""SELECT * FROM tools_and_skills;"""))
    while (id := input("Which tool(s) do you want to update? (Enter one or more comma separated digits or Q to quit) ").lower()) != "q":
        if not re.match("^\\s*\\d+\\s*(,\\s*\\d+\\s*)*$", id):
            print("Invalid number(s)!")
            continue

        ids = [int(i.strip()) for i in id.split(",")]

        tool_names = db.sql("""SELECT name FROM tools_and_skills WHERE id IN ?;""",
                            params=(ids,)).fetchall()
        last_tool = tool_names[-1][0]

        if len(tool_names) > 1:
            last_tool = " and " + last_tool

        last_used = input(
            f"When was your last use of {", ".join(n[0] for n in tool_names[:-1])}{last_tool}? (Defaults to now()) ")

        if not last_used:
            last_used = "now()"

        #! WARNING: THIS ALLOWS INJECTING SQL. DO NOT DO THIS IN YOUR APPLICATION UNLESS YOU HAVE A GOOD REASON TO!
        #! I am doing this here, because I am the only input source, and I actually want to be able to inject expressions like
        #! `now() - '4 days'::interval` or `'2026-10-13'` in order to be able to conveniently set the value of "last_used" to whatever I like
        db.execute(f"""UPDATE tools_and_skills
SET
    last_used = ({last_used})::date,
    update_count = update_count + 1
WHERE
    id IN ?
    AND last_used < ({last_used})::date;""", (ids,))
        print(db.sql("""SELECT
    *
FROM
    tools_and_skills
WHERE
    id IN ?;""", params=(ids,)))

    db.sql("""SELECT
    name,
    category,
    last_used,
    update_count,
    comment
FROM
    tools_and_skills
ORDER BY
    id;""").to_csv("tools_and_skills.csv")

    new_history_length = readline.get_current_history_length()
    readline.set_history_length(100)
    readline.append_history_file(
        new_history_length - initial_history_length, HIST_FILE)


if __name__ == "__main__":
    main()
