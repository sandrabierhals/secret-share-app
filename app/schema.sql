CREATE TABLE IF NOT EXISTS secrets (
    id TEXT PRIMARY KEY,
    secret_text TEXT NOT NULL,
    expires_at TEXT NOT NULL,
    one_time INTEGER NOT NULL,
    is_read INTEGER NOT NULL DEFAULT 0,
    created_at TEXT NOT NULL
);