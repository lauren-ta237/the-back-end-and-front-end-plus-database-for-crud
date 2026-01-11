from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

# connect to mysql server(no DB yet)
url_database = 'mysql+pymysql://root:p%40ssWord-123@localhost:3306'
engine = create_engine(url_database)
with engine.connect() as conn:
    conn.execute(text("CREATE DATABASE IF NOT EXISTS blogapplication"))

# now connect to the specific database
url_database = 'mysql+pymysql://root:p%40ssWord-123@localhost:3306/blogapplication'
engine = create_engine(url_database)

# verify we can connect to the target database and give a clear message if not
try:
    with engine.connect() as conn:  # quick connectivity check
        pass
except OperationalError as e:
    raise RuntimeError(
        "Unable to connect to 'blogapplication' database. Create it manually or disable super-read-only on the server."
    ) from e

# specify the automatic flush and commit
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()