"""Last

Revision ID: ef881ab26399
Revises: 2aa54fdd67a9
Create Date: 2023-06-11 16:19:31.468067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef881ab26399'
down_revision = '2aa54fdd67a9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('user', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('user', 'id')
    # ### end Alembic commands ###
