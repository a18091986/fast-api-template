"""create users table

Revision ID: 49f611f04a6a
Revises:
Create Date: 2025-03-15 19:36:21.704199

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "49f611f04a6a"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
