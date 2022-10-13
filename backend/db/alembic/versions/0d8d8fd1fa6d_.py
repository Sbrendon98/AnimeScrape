"""empty message

Revision ID: 0d8d8fd1fa6d
Revises: eb1ae001d7f2
Create Date: 2022-10-13 18:32:43.079163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d8d8fd1fa6d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'anime_list',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String,  nullable=False),
        sa.Column("code", sa.String,  nullable=False),
        sa.Column('edition', sa.Integer, index=True),
        sa.Column('isDubbed', sa.Boolean, default=False)
        )
    op.create_table(
        'anime',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String, index=True),
        sa.Column('episodes', sa.Integer, index=True),
        sa.Column('upcoming', sa.String, index=True),
        sa.Column('ongoing', sa.Boolean, index=True),
        sa.Column("isFavorite", sa.Boolean, index=True),
        sa.Column('title_id', sa.Integer, index=True),
    )
    


def downgrade():
    pass
