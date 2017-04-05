"""empty message

Revision ID: e970af6f46ea
Revises: 007d3184e48f
Create Date: 2017-04-05 16:47:40.373854

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e970af6f46ea'
down_revision = '007d3184e48f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('address')
    op.drop_table('tags')
    op.drop_table('person')
    op.drop_table('page')
    op.drop_table('tag')
    op.drop_table('category')
    op.add_column('user', sa.Column('openid', sa.String(length=120), nullable=True))
    op.create_unique_constraint(None, 'user', ['openid'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'openid')
    op.create_table('category',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tag',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('page',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('person',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tags',
    sa.Column('tag_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('page_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['page_id'], ['page.id'], name='tags_ibfk_2'),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], name='tags_ibfk_1'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('address',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('person_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['person_id'], ['person.id'], name='address_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('post',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('title', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('body', mysql.TEXT(), nullable=True),
    sa.Column('pub_date', mysql.DATETIME(), nullable=True),
    sa.Column('category_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], name='post_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###