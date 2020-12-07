"""empty message

Revision ID: 75cf54fdcfaf
Revises: 
Create Date: 2020-12-07 13:32:53.408367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75cf54fdcfaf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('equipment_types',
    sa.Column('code', sa.Integer(), nullable=False),
    sa.Column('type_name', sa.String(length=30), nullable=False),
    sa.Column('sn_mask', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('code'),
    sa.UniqueConstraint('type_name')
    )
    op.create_table('equipments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_code', sa.Integer(), nullable=True),
    sa.Column('serial_number', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['type_code'], ['equipment_types.code'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('serial_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('equipments')
    op.drop_table('equipment_types')
    # ### end Alembic commands ###