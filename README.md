<pre>
Welcome to Joel-dev-IMP.
System Information:
* <b>OS</b>: Fedora Linux 44 (GNU/Linux 7.2.8-200.fc44.x86_64)
* <b>WM</b>: Hyprland 0.56.2

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
│ Git                │                   0 │
│ Python             │                   0 │
│ SQL                │                   0 │
│ Visual Studio Code │                   0 │
│ Javascript         │                   4 │
│ Typst              │                   4 │
│ LaTeX              │                   6 │
│ Bash               │                  11 │
│ GIMP               │                  13 │
│ Docker             │                  18 │
│ Next.js            │                  18 │
│ Typescript         │                  18 │
│ Java               │                  19 │
│ IntelliJ Idea      │                  20 │
│ Markdown           │                  24 │
│ HTML               │                  27 │
│ CSS                │                  31 │
│ Tailwind           │                  31 │
│ Figma              │                  33 │
│ C                  │                 269 │
│ OCaml              │                 426 │
│ C++                │                 482 │
└────────────────────┴─────────────────────┘
  22 rows                        2 columns
memory D .exit
Joel-dev-IMP@github:~$ <b>date '+%Y-%m-%d %H:00'</b>
2026-10-13 09:00
Joel-dev-IMP@github:~$ <b>exit</b>
</pre>
