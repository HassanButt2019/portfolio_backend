"""Add projects table

Revision ID: a596a1d111a4
Revises: e0a8e30fcf53
Create Date: 2025-01-12 02:24:14.281920

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a596a1d111a4'
down_revision: Union[str, None] = 'e0a8e30fcf53'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
