import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

# engine = create_engine("mysql+pymysql://root@localhost:3306/classificationdb")


# Get the current working directory (assuming your script is in the project's root)
# project_root = os.getcwd()

# Define the path to the SQLite database file using an absolute path
# DATABASE_URL = f"sqlite:///{os.path.join(project_root, 'api', 'classificationdb.sqlite')}"

# Rest of your SQLAlchemy code


DATABASE_URL = "sqlite:///../api/classificationdb.sqlite"
engine = create_engine(DATABASE_URL)

# engine = create_engine(DATABASE_URL)
session = Session(engine)

meta = MetaData()


conn = engine.connect()
