CREATE TYPE record_type AS ENUM ('good', 'bad');

CREATE TABLE quote
(
    id     SERIAL NOT NULL PRIMARY KEY,
    text   TEXT,
    author JSON,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE user
(
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE record
(
    id      SERIAL NOT NULL PRIMARY KEY,
    type record_type,
    text JSON,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);