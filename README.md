<pre>
Welcome to Joel-dev-IMP.
System Information:
* <b>OS</b>: Fedora Linux 44 (GNU/Linux 7.2.4-200.fc44.x86_64)
* <b>WM</b>: Hyprland 0.56.2

This profile belongs to Joel.
To get started, you can try the following commands:
* <b>whoami</b>: Print information about the person behind this profile
* <b>profile-facts</b>: Print fun-facts about this profile
* <b>duckdb</b>: A <a href="https://duckdb.org/" target="_blank" rel="noopener noreferrer">database system</a> that appreciates ducks

Joel-dev-IMP@github:~$ <b>whoami</b>
- Computer Science Student <a href="https://www.cit.tum.de/cit/startseite/" target="_blank" rel="noopener noreferrer">@ Technical University of Munich (TUM)</a>
- Open-Source Contributor (since 2020)
- A person that likes to experiment with different tech-stacks

Joel-dev-IMP@github:~$ <b>profile-facts</b>
- Joined on January 12, 2021
- Pushed a private source code mirror of <a href="https://freefilesync.org/" target="_blank" rel="noopener noreferrer">FreeFileSync</a> with commits
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
             ('Markdown', 'DOCUMENTS', '2026-09-16', ''),
             (
                 'Typst',
                 'DOCUMENTS',
                 '2026-09-16',
                 'Check out https://typst.app/'
             ),
             ('SQL', 'DATABASES', '2026-09-16', ''),
             (
                 'Python',
                 'PROGRAMMING_LANGUAGES',
                 '2026-09-16',
                 'First programming language'
             ),
             ('Javascript', 'PROGRAMMING_LANGUAGES', '2026-09-16', ''),
             ('Bash', 'COMMAND_LINES', '2026-09-16', ''),
             ('Git', 'VERSION_CONTROL', '2026-09-16', ''),
             ('Visual Studio Code', 'IDE', '2026-09-16', ''),
             ('HTML', 'WEB_DEVELOPMENT', '2026-09-16', ''),
             (
                 'GIMP',
                 'GRAPHICS_EDITORS',
                 '2026-09-15',
                 'I hope the GIMP UX gets a little love'
             ),
             ('Docker', 'CONTAINERS', '2026-09-15', ''),
             ('CSS', 'WEB_DEVELOPMENT', '2026-09-12', ''),
             ('Tailwind', 'WEB_DEVELOPMENT', '2026-09-12', ''),
             ('Next.js', 'WEB_DEVELOPMENT', '2026-09-12', ''),
             ('Typescript', 'WEB_DEVELOPMENT', '2026-09-12', ''),
             ('Figma', 'DESIGN_TOOLS', '2026-09-10', ''),
             ('LaTeX', 'DOCUMENTS', '2026-07-13', ''),
             ('C', 'PROGRAMMING_LANGUAGES', '2026-01-17', ''),
             ('Java', 'PROGRAMMING_LANGUAGES', '2025-12-18', ''),
             (
                 'OCaml',
                 'PROGRAMMING_LANGUAGES',
                 '2025-08-13',
                 'Learned this at TUM'
             ),
             ('C++', 'PROGRAMMING_LANGUAGES', '2025-06-18', '');

memory D SELECT
             name,
             now()::date - last_used AS days_since_last_use
         FROM
             tools_and_skills
         ORDER BY
             days_since_last_use;
┌────────────────────┬─────────────────────┐
│        name        │ days_since_last_use │
│      varchar       │        int64        │
├────────────────────┼─────────────────────┤
│ Markdown           │                   0 │
│ Typst              │                   0 │
│ SQL                │                   0 │
│ Python             │                   0 │
│ Javascript         │                   0 │
│ Bash               │                   0 │
│ Git                │                   0 │
│ Visual Studio Code │                   0 │
│ HTML               │                   0 │
│ GIMP               │                   1 │
│ Docker             │                   1 │
│ CSS                │                   4 │
│ Tailwind           │                   4 │
│ Next.js            │                   4 │
│ Typescript         │                   4 │
│ Figma              │                   6 │
│ LaTeX              │                  65 │
│ C                  │                 242 │
│ Java               │                 272 │
│ OCaml              │                 399 │
│ C++                │                 455 │
└────────────────────┴─────────────────────┘
  21 rows                        2 columns
memory D .exit
Joel-dev-IMP@github:~$ <b>date +%Y-%m-%d</b>
2026-09-16
Joel-dev-IMP@github:~$ <b>exit</b>
</pre>
