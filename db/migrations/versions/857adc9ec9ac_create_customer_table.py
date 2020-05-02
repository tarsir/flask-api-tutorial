"""create customer table

Revision ID: 857adc9ec9ac
Revises: 
Create Date: 2020-02-18 22:00:57.415324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '857adc9ec9ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
            'customer',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('first_name', sa.String(40)),
            sa.Column('last_name', sa.String(40)),
            sa.Column('email_address', sa.String(100)),
            sa.Column('phone_number', sa.String(15)),
            sa.Column('city', sa.String(50)),
            sa.Column('state', sa.String(50)),
            sa.Column('is_registered', sa.Boolean),
            sa.Column('password_hash', sa.String(100)))

def downgrade():
    op.drop_table('customer')
