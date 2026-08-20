"""create permissions table

Revision ID: 635411882b91
Revises: 58e90dbbdb67
Create Date: 2026-08-20 14:00:39.797807

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "635411882b91"
down_revision: Union[str, Sequence[str], None] = "58e90dbbdb67"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "permissions",
        sa.Column("permission_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("permission_id"),
        sa.UniqueConstraint("name"),
    )

    op.create_index(
        op.f("ix_permissions_permission_id"),
        "permissions",
        ["permission_id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        op.f("ix_permissions_permission_id"),
        table_name="permissions",
    )
    op.drop_table("permissions")