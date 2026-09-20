CREATE TABLE tools_and_skills (
    name VARCHAR PRIMARY KEY,
    category VARCHAR NOT NULL,
    last_used DATE NOT NULL,
    comment VARCHAR
);

INSERT INTO
    tools_and_skills (name, category, last_used, comment)
VALUES
    (
        'Python',
        'PROGRAMMING_LANGUAGES',
        '2026-09-20',
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
    ('Next.js', 'WEB_DEVELOPMENT', '2026-09-20', ''),
    ('Figma', 'DESIGN_TOOLS', '2026-09-10', ''),
    (
        'GIMP',
        'GRAPHICS_EDITORS',
        '2026-09-15',
        'I hope the GIMP UX gets a little love'
    ),
    ('Docker', 'CONTAINERS', '2026-09-20', ''),
    ('SQL', 'DATABASES', '2026-09-20', ''),
    ('Bash', 'COMMAND_LINES', '2026-09-16', ''),
    ('Git', 'VERSION_CONTROL', '2026-09-20', ''),
    ('Visual Studio Code', 'IDE', '2026-09-20', '');

SELECT
    name,
    now()::date - last_used AS days_since_last_use
FROM
    tools_and_skills
ORDER BY
    days_since_last_use,
    name;