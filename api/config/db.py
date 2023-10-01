from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root@localhost:3306/classificationdb")

# DATABASE_URL = "sqlite:///./api/classificationdb.db"

# engine = create_engine(DATABASE_URL)
meta = MetaData()


conn = engine.connect()
