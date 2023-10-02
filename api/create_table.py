from sqlalchemy import create_engine, MetaData
from models.index import users

# Replace "your_database.db" with the desired database URI (SQLite file path)
db_uri = "sqlite:///classificationdb.sqlite"

# Create an SQLAlchemy engine
engine = create_engine(db_uri)

# Create the table
metadata = MetaData()
# Use checkfirst to avoid re-creating if it already exists
users.create(engine, checkfirst=True)
