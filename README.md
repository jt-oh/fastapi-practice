# FastAPI Practice

practice fastapi python web framework on docker environment

## Docker Environment

### Development

script for running develop environment of fastapi on container

``` shell
docker run \
    -dp 8000:8000 \
    -w /app \
    -v "$(pwd)/app:/app" \
    --network=my-mysql-network \
    python:3.10.7 \
    sh -c "pip install --no-cache-dir fastapi uvicorn sqlalchemy mysql-connector-python && uvicorn main:myApp --host 0.0.0.0 --reload"
```

## Database ORM

### SQLAlchemy

- Installation

``` shell
pip install SQLAlchemy
```

- Tutorial
<https://docs.sqlalchemy.org/en/20/>

## MySql DBAPI

### MySQL-Connector

- Installation

``` shell
pip install mysql-connector-python
```

- Tutorials
<https://dev.mysql.com/doc/connector-python/en/>

## Migration

### Alembic

- Installation

``` shell
pip install alembic
```

- Tutorials
<https://alembic.sqlalchemy.org/en/latest/tutorial.html#the-migration-environment>