"""'Init'

Revision ID: 436612a0e388
Revises: d5e34e137303
Create Date: 2023-11-15 18:26:50.637325

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '436612a0e388'
down_revision: Union[str, None] = 'd5e34e137303'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('first_name', sa.String(length=50), nullable=False))
    op.drop_column('contacts', 'fist_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('fist_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.drop_column('contacts', 'first_name')
    # ### end Alembic commands ###