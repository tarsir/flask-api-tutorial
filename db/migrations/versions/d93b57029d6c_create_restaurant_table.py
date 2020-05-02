"""create restaurant table

Revision ID: d93b57029d6c
Revises: 857adc9ec9ac
Create Date: 2020-03-12 23:21:36.244034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd93b57029d6c'
down_revision = '857adc9ec9ac'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            'restaurant',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String(100)),
            sa.Column('city', sa.String(50)),
            sa.Column('state', sa.String(50)),
            sa.Column('email_address', sa.String(100)),
            sa.Column('phone_number', sa.String(15)),
            sa.Column('average_table_time', sa.Integer),
            sa.Column('seat_count', sa.Integer))


def downgrade():
    op.drop_table('restaurant')
