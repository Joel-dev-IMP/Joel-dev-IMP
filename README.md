<pre>
Welcome to Joel-dev-IMP.
System Information:
* <b>OS</b>: Fedora Linux 44 (GNU/Linux 7.2.5-200.fc44.x86_64)
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
             comment VARCHAR
         );

memory D INSERT INTO
             tools_and_skills (name, category, last_used, comment)
         VALUES
             (
                 'Python',
                 'PROGRAMMING_LANGUAGES',
                 '2026-09-17',
                 'First programming language'
             ),
             (
                 'Javascript',
                 'PROGRAMMING_LANGUAGES',
                 '2026-09-16',
                 ''
             ),
             ('C', 'PROGRAMMING_LANGUAGES', '2026-01-17', ''),
             ('Java', 'PROGRAMMING_LANGUAGES', '2025-12-18', ''),
             (
                 'OCaml',
                 'PROGRAMMING_LANGUAGES',
                 '2025-08-13',
                 'Learned this at TUM'
             ),
             ('C++', 'PROGRAMMING_LANGUAGES', '2025-06-18', ''),
             ('Markdown', 'DOCUMENTS', '2026-09-19', ''),
             (
                 'Typst',
                 'DOCUMENTS',
                 '2026-09-19',
                 'Check out https://typst.app/'
             ),
             ('LaTeX', 'DOCUMENTS', '2026-07-13', ''),
             ('HTML', 'WEB_DEVELOPMENT', '2026-09-16', ''),
             ('CSS', 'WEB_DEVELOPMENT', '2026-09-12', ''),
             ('Typescript', 'WEB_DEVELOPMENT', '2026-09-12', ''),
             ('Tailwind', 'WEB_DEVELOPMENT', '2026-09-12', ''),
             ('Next.js', 'WEB_DEVELOPMENT', '2026-09-12', ''),
             ('Figma', 'DESIGN_TOOLS', '2026-09-10', ''),
             (
                 'GIMP',
                 'GRAPHICS_EDITORS',
                 '2026-09-15',
                 'I hope the GIMP UX gets a little love'
             ),
             ('Docker', 'CONTAINERS', '2026-09-15', ''),
             ('SQL', 'DATABASES', '2026-09-19', ''),
             ('Bash', 'COMMAND_LINES', '2026-09-16', ''),
             ('Git', 'VERSION_CONTROL', '2026-09-19', ''),
             ('Visual Studio Code', 'IDE', '2026-09-19', '');

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
│ Markdown           │                   0 │
│ SQL                │                   0 │
│ Typst              │                   0 │
│ Visual Studio Code │                   0 │
│ Python             │                   2 │
│ Bash               │                   3 │
│ HTML               │                   3 │
│ Javascript         │                   3 │
│ Docker             │                   4 │
│ GIMP               │                   4 │
│ CSS                │                   7 │
│ Next.js            │                   7 │
│ Tailwind           │                   7 │
│ Typescript         │                   7 │
│ Figma              │                   9 │
│ LaTeX              │                  68 │
│ C                  │                 245 │
│ Java               │                 275 │
│ OCaml              │                 402 │
│ C++                │                 458 │
└────────────────────┴─────────────────────┘
  21 rows                        2 columns
memory D .exit
Joel-dev-IMP@github:~$ <b>date +%Y-%m-%d</b>
2026-09-19
Joel-dev-IMP@github:~$ <b>exit</b>
</pre>
