"""changed receipt category name to better fit task

Revision ID: ac0281840e69
Revises: 27ded3f077f3
Create Date: 2026-05-12 18:34:20.248261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac0281840e69'
down_revision: Union[str, Sequence[str], None] = '27ded3f077f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
