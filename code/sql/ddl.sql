CREATE TABLE IF NOT EXISTS users (
  id            INT PRIMARY KEY      NOT NULL,
  name          VARCHAR              NOT NULL,
  email         VARCHAR              NOT NULL,
  inserted_at   INT,
  updated_at    INT
);

CREATE TABLE IF NOT EXISTS count_per_extension(
  extension       VARCHAR    NOT NULL,
  count           INT        NOT NULL,
  inserted_at     INT
);