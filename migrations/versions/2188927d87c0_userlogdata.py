"""UserLogData

Revision ID: 2188927d87c0
Revises: ff8d9261c51e
Create Date: 2023-02-07 18:14:10.283339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2188927d87c0'
down_revision = 'ff8d9261c51e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_log_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(length=512), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_log_data')
    # ### end Alembic commands ###