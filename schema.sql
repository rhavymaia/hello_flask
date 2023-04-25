DROP TABLE IF EXISTS pessoas;

CREATE TABLE pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
);