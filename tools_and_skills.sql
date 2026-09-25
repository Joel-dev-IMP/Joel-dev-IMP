CREATE TABLE tools_and_skills (
    name VARCHAR PRIMARY KEY,
    category VARCHAR NOT NULL,
    last_used DATE NOT NULL,
    comment VARCHAR
);

INSERT INTO
    tools_and_skills (name, category, last_used, comment) (
        SELECT
            name,
            category,
            last_used,
            comment
        FROM
            'tools_and_skills.csv'
    );

SELECT
    name,
    now()::date - last_used AS days_since_last_use
FROM
    tools_and_skills
ORDER BY
    days_since_last_use,
    name;