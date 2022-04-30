"""create anime table

Revision ID: 680e1e31d643
Revises: 
Create Date: 2022-04-18 23:28:17.715184

"""
import os
import sqlalchemy as sa 
# from email.policy import default
# from xmlrpc.client import Boolean
# from alembic.config import Config
from alembic import op, command
# from sqlalchemy import MetaData
from scraper import animelist
# from db import engine


# revision identifiers, used by Alembic.
revision = '680e1e31d643'
down_revision = None
branch_labels = None
depends_on = None

# meta = MetaData(bind=op.get_bind())
# meta.create_all(engine)
# alembic_cfg = Config("./alembic.ini")
# command.stamp(alembic_cfg, "head")

def upgrade():
    op.create_table(
        'anime_list',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, unique=True, nullable=False),
        sa.Column("code", sa.String, unique=True, nullable=False),
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
    # op.create_primary_key(
    #     'primary_key', 'anime_list',['id']
    # )
    # op.create_foreign_key(
    #     'foreign_key','anime_list','anime',["id"],["title_id"]
    # )
    
    
    #op.bulk_insert(anime_list, animelist.animeFile())

def downgrade():
    op.drop_table('anime_list')
