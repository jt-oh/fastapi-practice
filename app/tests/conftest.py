from typing import Generator

import pytest
from fastapi.testclient import TestClient

from ..main import myApp
from ..api.deps import get_db
from ..database import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://my_fast_api_user:fast_api_pwd@mysql-server:3306/my_fast_api_test_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

myApp.dependency_overrides[get_db] = override_get_db


@pytest.fixture()
def configure_test_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def db() -> Generator:
    yield TestingSessionLocal()

@pytest.fixture()
def client() -> Generator:
    with TestClient(myApp) as c:
        yield c