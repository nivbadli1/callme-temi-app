"""delete_contacts_times

Revision ID: 149536898a7f
Revises: dc50c465af39
Create Date: 2022-09-03 17:15:28.091127

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '149536898a7f'
down_revision = 'dc50c465af39'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contacts_times')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts_times',
    sa.Column('day', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('contact_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('from', mysql.TIME(), nullable=False),
    sa.Column('to', mysql.TIME(), nullable=False),
    sa.ForeignKeyConstraint(['contact_id'], ['contacts.contact_id'], name='contacts_times_FK', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('day', 'contact_id', 'from', 'to'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###