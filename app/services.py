import uuid # Universally Unique Identifier ( permanent ID to identify users, files, or database records without any risk of duplicates)
from datetime import datetime, timedelta, timezone
from database import get_connection
from models.secret_model import Secret


def create_secret(secret_text, expires_in, one_time):

    secret_id = str(uuid.uuid4())
    expires_at = datetime.now(timezone.utc) + timedelta(
        minutes=expires_in
    )

    created_at = datetime.now(timezone.utc)

    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO secrets (
                id,
                secret_text,
                expires_at,
                one_time,
                is_read,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                secret_id,
                secret_text,
                expires_at.isoformat(),
                int(one_time),
                0,
                created_at.isoformat()
            )
        )
        conn.commit()
    return secret_id


def get_secret(secret_id):

    with get_connection() as conn:
        row = conn.execute(
            """
            SELECT *
            FROM secrets
            WHERE id = ?
            """,
            (secret_id,)
        ).fetchone()

    if not row:
        return None, "not_found"

    secret = Secret(
        id=row[0],
        secret_text=row[1],
        expires_at=row[2],
        one_time=row[3],
        is_read=row[4],
        created_at=row[5]
    )

    expires_at = datetime.fromisoformat(secret.expires_at)

    if datetime.now(timezone.utc) > expires_at:
        with get_connection() as conn:

            conn.execute(
                """
                DELETE FROM secrets
                WHERE id = ?
                """,
                (secret_id,)
            )

            conn.commit()
        return None, "expired"

    if secret.one_time and secret.is_read:
        return None, "already_read"

    if secret.one_time:
        with get_connection() as conn:

            conn.execute(
                """
                UPDATE secrets
                SET is_read = 1
                WHERE id = ?
                """,
                (secret_id,)
            )

            conn.commit()
    return secret.secret_text, None