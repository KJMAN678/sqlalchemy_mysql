from sqlalchemy import Column, Integer, create_engine, MetaData, DATETIME, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

USER_NAME = env("USER_NAME")
PASSWORD = env("PASSWORD")
DB_NAME = env("DB_NAME")
DB_HOST = env("DB_HOST")

engine = create_engine(
    f'mysql+pymysql://{USER_NAME}:{PASSWORD}@{DB_HOST}/{DB_NAME}',
    connect_args={
        "ssl": {
            "ssl_ca": "global-bundle.pem"
        }
    }
)

metadata = MetaData(engine)

Base = declarative_base()

class User(Base):
  __tablename__ = "user"
  __table_args__ = {"mysql_engine": "InnoDB"}

  id = Column("id", Integer, primary_key=True, autoincrement=True)
  name = Column("name", String(255))
  created = Column("created", DATETIME, default=datetime.now, nullable=False)
  modified = Column("modified", DATETIME, default=datetime.now, nullable=False)	
  
  def __init__(self, name):
    self.name = name
    now = datetime.now()
    self.created = now
    self.modified = now

# テーブルの作成
Base.metadata.create_all(engine)

# セッションを作るクラスを作成
SessionClass = sessionmaker(engine)
session = SessionClass()

# INSERT
user_a = User(name="Smith")
session.add(user_a)
session.commit()