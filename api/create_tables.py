from models.user import users
from sqlalchemy import create_engine, MetaData

# Define the path to your SQLite database file
DATABASE_URL = "sqlite:///./api/classificationdb.db"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a metadata object
meta = MetaData()

# Import your "users" table from models/user.py

# Bind the engine to the metadata
meta.bind = engine

# Create all tables defined in the metadata
meta.create_all()
