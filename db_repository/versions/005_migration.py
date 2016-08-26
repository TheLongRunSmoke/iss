from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
stat = Table('stat', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('timestamp', Integer),
    Column('request', Integer),
)

tle_data = Table('tle_data', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('timestamp', INTEGER),
    Column('useCount', INTEGER),
    Column('addTime', INTEGER),
    Column('tle', VARCHAR(length=100)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['stat'].create()
    pre_meta.tables['tle_data'].columns['useCount'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['stat'].drop()
    pre_meta.tables['tle_data'].columns['useCount'].create()
