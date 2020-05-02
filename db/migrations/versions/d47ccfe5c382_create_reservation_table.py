"""create reservation table

Revision ID: d47ccfe5c382
Revises: d93b57029d6c
Create Date: 2020-03-29 10:59:24.599816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd47ccfe5c382'
down_revision = 'd93b57029d6c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            'reservation',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('guest_count', sa.Integer),
            sa.Column('is_confirmed', sa.Boolean),
            sa.Column('is_canceled', sa.Boolean),
            sa.Column('time_and_date', sa.DateTime),
            sa.Column('customer_id', sa.Integer),
            sa.Column('restaurant_id', sa.Integer))
    op.create_foreign_key(
            'fk_reservation_customer_id',
            'reservation',
            'customer',
            ['customer_id'],
            ['id']
            )
    op.create_foreign_key(
            'fk_restaurant_customer_id',
            'reservation',
            'restaurant',
            ['restaurant_id'],
            ['id']
            )


def downgrade():
    op.drop_table('reservation')
