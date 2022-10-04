from typing import Generator

import pytest
from fastapi.testclient import TestClient

from ..main import myApp
from ..database import SessionLocal

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://my_fast_api_user:fast_api_pwd@mysql-server:3306/my_fast_api_test_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@pytest.fixture()
def db() -> Generator:
    yield SessionLocal

@pytest.fixture()
def client() -> Generator:
    with TestClient(myApp) as c:
        yield c