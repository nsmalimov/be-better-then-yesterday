CREATE
TYPE record_type AS ENUM ('good', 'bad');

CREATE TABLE quotes
(
    id     SERIAL NOT NULL PRIMARY KEY,
    text   TEXT   NOT NULL,
    author VARCHAR(255) DEFAULT 'Автор неизвестен',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE users
(
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE records
(
    id      SERIAL                             NOT NULL PRIMARY KEY,
    user_id VARCHAR(255) REFERENCES users (id) NOT NULL,
    type record_type NOT NULL,
    text    TEXT                               NOT NULL,
    mask    VARCHAR(255)                       NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);