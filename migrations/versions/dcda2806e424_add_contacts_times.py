"""add_contacts_times

Revision ID: dcda2806e424
Revises: 149536898a7f
Create Date: 2022-09-03 17:17:35.375507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcda2806e424'
down_revision = '149536898a7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts_times',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('day', sa.Integer(), nullable=True),
    sa.Column('contact_id', sa.Integer(), nullable=True),
    sa.Column('from', sa.Time(), nullable=True),
    sa.Column('to', sa.Time(), nullable=True),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.contact_id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contacts_times_contact_id'), 'contacts_times', ['contact_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contacts_times_contact_id'), table_name='contacts_times')
    op.drop_table('contacts_times')
    # ### end Alembic commands ###
