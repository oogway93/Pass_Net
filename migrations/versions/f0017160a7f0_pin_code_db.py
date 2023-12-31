"""Pin code db

Revision ID: f0017160a7f0
Revises: 8b9ac313f022
Create Date: 2023-08-19 18:14:56.094309

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'f0017160a7f0'
down_revision: Union[str, None] = '8b9ac313f022'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Pin-Code',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('pin', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Pin-Code')
    # ### end Alembic commands ###
