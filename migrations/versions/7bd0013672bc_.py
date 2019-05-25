"""empty message

Revision ID: 7bd0013672bc
Revises: 43df266be83d
Create Date: 2019-05-20 13:00:19.501759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bd0013672bc'
down_revision = '43df266be83d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parties')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parties',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='parties_pkey')
    )
    # ### end Alembic commands ###
