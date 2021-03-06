"""lecturer_id added

Revision ID: 5f17a2dd40ec
Revises: 
Create Date: 2021-01-15 23:12:51.875950

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5f17a2dd40ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('name', table_name='role')
    op.drop_table('role')
    op.drop_index('email', table_name='user')
    op.drop_index('username', table_name='user')
    op.drop_table('user')
    op.add_column('workshops', sa.Column('lecturer_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'workshops', 'speaker', ['lecturer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'workshops', type_='foreignkey')
    op.drop_column('workshops', 'lecturer_id')
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=180), nullable=False),
    sa.Column('username', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('role_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_date', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], name='user_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('username', 'user', ['username'], unique=True)
    op.create_index('email', 'user', ['email'], unique=True)
    op.create_table('role',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=80), nullable=False),
    sa.Column('created_date', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('name', 'role', ['name'], unique=True)
    # ### end Alembic commands ###
