"""create user and profile table

Revision ID: 0ed68df4fd68
Revises: c8042065281a
Create Date: 2024-02-25 20:31:15.974032

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0ed68df4fd68"
down_revision: Union[str, None] = "c8042065281a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_users_email", table_name="users")
    op.drop_column("users", "is_active")
    op.drop_column("users", "hashed_password")
    op.drop_column("users", "is_verified")
    op.drop_column("users", "is_superuser")
    op.drop_column("users", "email")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column("email", sa.VARCHAR(length=320), autoincrement=False, nullable=False),
    )
    op.add_column(
        "users",
        sa.Column("is_superuser", sa.BOOLEAN(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "users",
        sa.Column("is_verified", sa.BOOLEAN(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "users",
        sa.Column(
            "hashed_password",
            sa.VARCHAR(length=1024),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.add_column(
        "users",
        sa.Column("is_active", sa.BOOLEAN(), autoincrement=False, nullable=False),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)
    # ### end Alembic commands ###
