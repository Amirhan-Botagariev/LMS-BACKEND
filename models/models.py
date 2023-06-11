from sqlalchemy import MetaData, Integer, Table, Column, String, Boolean

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, unique=True, index=True, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("role", String, default="guest", nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("phone_number", String),
    Column("gender", String),
    Column("country", String),
    Column("university", String),
)
