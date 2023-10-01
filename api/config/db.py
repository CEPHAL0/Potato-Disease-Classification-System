from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

engine = create_engine("mysql+pymysql://root@localhost:3306/classificationdb")

session = Session(engine)

# DATABASE_URL = "sqlite:///./api/classificationdb.db"

# engine = create_engine(DATABASE_URL)
meta = MetaData()

conn = engine.connect()
