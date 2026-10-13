#!/bin/python
import duckdb

import re


def main() -> None:
    db = duckdb.connect(":memory:")

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
    while (id := input("Which tool do you want to update? (Enter a digit or Q to quit) ").lower()) != "q":
        if not re.match("^\\d+$", id):
            print("Invalid number!")
            continue

        last_used = input("When was the tool last used? (Defaults to now()) ")

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
    id = ?
    AND last_used < ({last_used})::date;""", (id,))
        print(db.sql("""SELECT
    *
FROM
    tools_and_skills
WHERE
    id = ?;""", params=(id,)))

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


if __name__ == "__main__":
    main()
