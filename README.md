<pre>
Welcome to Joel-dev-IMP.
System Information:
* <b>OS</b>: Fedora Linux 44 (GNU/Linux 7.3.4-200.fc44.x86_64)
* <b>WM</b>: KWin

This profile belongs to Joel.
To get started, you can try the following commands:
* <b>whoami</b>: Print information about the person behind this profile
* <b>profile-facts</b>: Print fun-facts about this profile
* <b>duckdb</b>: A <a href="https://duckdb.org/">database system</a> that appreciates ducks

Joel-dev-IMP@github:~$ <b>whoami</b>
- Computer Science Student <a href="https://www.cit.tum.de/cit/startseite/">@ Technical University of Munich (TUM)</a>
- Open-Source Contributor (since 2020)
- A person that likes to experiment with different tech-stacks

Joel-dev-IMP@github:~$ <b>profile-facts</b>
- Joined on January 12, 2021
- Pushed a private source code mirror of <a href="https://freefilesync.org/">FreeFileSync</a> with commits
  dating back to 2008 - making the public GitHub history quite confusing

Joel-dev-IMP@github:~$ <b>duckdb</b>
memory D CREATE TABLE tools_and_skills (
             name VARCHAR PRIMARY KEY,
             category VARCHAR NOT NULL,
             last_used DATE NOT NULL,
             update_count INTEGER NOT NULL, -- How often this has this tool/skill been updated in this repo?
             comment VARCHAR
         );

memory D INSERT INTO
             tools_and_skills (name, category, last_used, update_count, comment) (
                 SELECT
                     name,
                     category,
                     last_used,
                     update_count,
                     comment
                 FROM
                     'tools_and_skills.csv'
             );

memory D SELECT
             name,
             now()::date - last_used AS days_since_last_use
         FROM
             tools_and_skills
         ORDER BY
             days_since_last_use,
             name;
┌────────────────────┬─────────────────────┐
│        name        │ days_since_last_use │
│      varchar       │        int64        │
├────────────────────┼─────────────────────┤
│ C++                │                   1 │
│ Git                │                   1 │
│ Python             │                   1 │
│ Visual Studio Code │                   1 │
│ Bash               │                   2 │
│ Github Actions     │                   2 │
│ SQL                │                   4 │
│ Docker             │                   5 │
│ Typescript         │                   5 │
│ Typst              │                   5 │
│ CSS                │                  11 │
│ Javascript         │                  11 │
│ Next.js            │                  11 │
│ Tailwind           │                  11 │
│ Figma              │                  14 │
│ Markdown           │                  28 │
│ C                  │                  35 │
│ LaTeX              │                  41 │
│ GIMP               │                  48 │
│ Java               │                  54 │
│ IntelliJ Idea      │                  55 │
│ HTML               │                  62 │
│ OCaml              │                 461 │
└────────────────────┴─────────────────────┘
  23 rows                        2 columns
memory D .exit
Joel-dev-IMP@github:~$ <b>date '+%Y-%m-%d %H:00'</b>
2026-11-17 12:00
Joel-dev-IMP@github:~$ <b>exit</b>
</pre>
