"""create account table

Revision ID: 680e1e31d643
Revises: 
Create Date: 2022-04-18 23:28:17.715184

"""
from email.policy import default
from xmlrpc.client import Boolean
from alembic import op
import sqlalchemy as sa 
from sqlalchemy import Table, MetaData
import json, os, sys


# revision identifiers, used by Alembic.
revision = '680e1e31d643'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    meta = MetaData(bind=op.get_bind())
    
    meta.reflect(only=('anime_list', 'anime'))
    
    anime_list = Table('anime_list', meta)
    op.create_anime_list(
        'anime_list',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, unique=True, nullable=False),
        sa.Column('edition', sa.Integer, index=True),
        sa.Column('isDubbed', sa.Boolean, default=False)
        )
    op.create_anime(
        'anime',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, index=True),
        sa.Column('episodes', sa.Integer, index=True),
        sa.Column('upcoming', sa.String, index=True),
        sa.Column('ongoing', sa.Boolean, index=True),
        sa.Column('title_id', sa.Integer, index=True)
    )
    op.create_primary_key(
        'primary_key', 'anime_list',['id', 'edition']
    )
    op.create_foreign_key(
        'foreign_key','anime_list','anime',["id"],["title_id"]
    )
    
    
    # op.bulk_insert(anime_list, )

def downgrade():
    pass


# file = open('scraper\animelist.json')
# animeList = json.load(file)
# print(animeList)

if os.path.isfile('backend\scraper\animelist.json'):
    print("file exists")