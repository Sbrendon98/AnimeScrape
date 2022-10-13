"""create anime table

Revision ID: 680e1e31d643
Revises: 
Create Date: 2022-04-18 23:28:17.715184

"""
import sqlalchemy as sa 
from alembic.config import Config
from alembic import op, command
from sqlalchemy import MetaData

from db import engine, Base


# revision identifiers, used by Alembic.
revision = '680e1e31d643'
down_revision = None
branch_labels = None
depends_on = None

# meta = MetaData(bind=op.get_bind())
# meta.create_all(engine)
# alembic_cfg = Config("alembic.ini")
# command.stamp(alembic_cfg, "head")

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
        sa.Column('title_id', sa.Integer, index=True)
    )
    op.create_table(
        'favorites',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String, index=True),
        sa.Column('isFavorite', sa.Boolean, index=True),
        sa.Column('upcoming', sa.String, index=True)
    )
    # op.create_primary_key(
    #     'primary_key', 'anime_list',['id']
    # )
    # op.create_foreign_key(
    #     'foreign_key','anime_list','anime',["id"],["title_id"]
    # )


def downgrade():
    op.drop_table('anime_list')
