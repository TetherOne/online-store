"""ad nullable to profiles

Revision ID: f3130bd66b8f
Revises: 0ed68df4fd68
Create Date: 2024-02-25 21:06:20.445478

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f3130bd66b8f"
down_revision: Union[str, None] = "0ed68df4fd68"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("profiles", "city", existing_type=sa.VARCHAR(), nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("profiles", "city", existing_type=sa.VARCHAR(), nullable=False)
    # ### end Alembic commands ###
