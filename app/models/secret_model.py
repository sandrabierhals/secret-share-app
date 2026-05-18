class Secret:

    def __init__(
        self,
        id,
        secret_text,
        expires_at,
        one_time,
        is_read,
        created_at
    ):
        self.id = id
        self.secret_text = secret_text
        self.expires_at = expires_at
        self.one_time = one_time
        self.is_read = is_read
        self.created_at = created_at