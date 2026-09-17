#!/bin/python
from pathlib import Path

import duckdb
import subprocess
import re


def get_system_information() -> str:
    """Get the information on the current system using fastfetch and format it in a nice way"""
    info = subprocess.check_output("fastfetch").decode(encoding="utf-8")

    os_info = re.search("OS: [^(]+", info)
    kernel_info = re.search("Kernel: [^(\n]+", info)
    wm_info = re.search("WM: [^(]+", info)

    if os_info is None or kernel_info is None or wm_info is None:
        raise

    system_information = os_info.group().strip().replace("OS:", "* <b>OS</b>:")
    system_information += f" (GNU/{kernel_info.group().replace("Kernel:", "").strip()})\n"
    system_information += wm_info.group().strip().replace("WM:", "* <b>WM</b>:")

    return system_information


def shell_command(command: str) -> str:
    """Formats an arbitrary command to look like a shell command"""
    return f"Joel-dev-IMP@github:~$ <b>{command.removeprefix("./")}</b>"


def run_command(command: str, shell: bool = False) -> str:
    """Runs a command and formats the output to look like it was hand-typed in a shell"""
    output = subprocess.check_output(
        command.split(" "), shell=shell).decode(encoding="utf-8")
    return f"{shell_command(command)}\n{output.removesuffix("\n")}"


def execute_duckdb_queries() -> str:
    """Executes all queries from tools_and_skills.sql and formats them (and their outputs) to look like a terminal session."""
    DUCKDB_PREFIX = "memory D"
    TOOLS_AND_SKILLS = Path.cwd() / "tools_and_skills.sql"
    db = duckdb.connect(":memory:")

    duckdb_commands = shell_command("duckdb") + "\n"

    with TOOLS_AND_SKILLS.open("r") as f:
        queries = f.read().split(";")

    for query in filter(lambda x: x != "", queries):
        query += ";"
        result = db.sql(query)

        # Offset all query lines to ensure that they don't start before the first line
        query_lines = [" " * (len(DUCKDB_PREFIX) + 1) +
                       q + "\n" for q in query.splitlines()]

        duckdb_commands += DUCKDB_PREFIX + " "
        duckdb_commands += "".join(query_lines).strip() + "\n"

        if result is not None:
            duckdb_commands += str(result)
        else:
            duckdb_commands += "\n"

    duckdb_commands += f"{DUCKDB_PREFIX} .exit"
    return duckdb_commands


def main() -> None:
    README = Path.cwd() / "README.md"
    README_CONTENT = f"""
<pre>
Welcome to Joel-dev-IMP.
System Information:
{get_system_information()}

This profile belongs to Joel.
To get started, you can try the following commands:
* <b>whoami</b>: Print information about the person behind this profile
* <b>profile-facts</b>: Print fun-facts about this profile
* <b>duckdb</b>: A <a href="https://duckdb.org/">database system</a> that appreciates ducks

{run_command("./whoami")}
{run_command("./profile-facts")}
{execute_duckdb_queries()}
{run_command("date +%Y-%m-%d")}
{run_command("exit", shell=True).strip()}
</pre>"""

    with README.open("w+", encoding="utf-8") as f:
        f.write(README_CONTENT.strip() + "\n")


if __name__ == "__main__":
    main()
