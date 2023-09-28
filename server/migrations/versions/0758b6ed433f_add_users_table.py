"""add users table

Revision ID: 0758b6ed433f
Revises: a1a3e217f07f
Create Date: 2023-09-28 14:19:50.191479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0758b6ed433f'
down_revision = 'a1a3e217f07f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('_password_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###