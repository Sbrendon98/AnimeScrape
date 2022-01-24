"""init

Revision ID: 3deeecd26918
Revises: 
Create Date: 2022-01-23 02:33:06.041243

"""
from sqlalchemy import ForeignKey
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3deeecd26918'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'anime_list',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, unique=True, index=True, nullable=False),
        sa.Column('isDubbed', sa.Boolean, default=False)
    )
    
    op.create_table(
        'anime',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, unique=True, index=True),
        sa.Column('episodes', sa.Integer, index=True),
        sa.Column('upcoming', sa.String, index=True),
        sa.Column('ongoing', sa.Boolean, index=True),
        sa.Column('title_id', sa.Integer, ForeignKey("anime_list.id"))
    )


def downgrade():
    op.drop_table('anime')
    op.drop_table('anime_list')
