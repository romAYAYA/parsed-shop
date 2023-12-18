import sqlalchemy as _sql
import sqlalchemy.orm as _orm

SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"

engine = _sql.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _orm.declarative_base()
