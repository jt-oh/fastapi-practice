# FastAPI Practice

practice fastapi python web framework on docker environment

## Docker Environment

### Development

script for running develop environment of fastapi on container

#### FastAPI App Docker Container

``` shell
docker run \
    -dp 8000:8000 \
    -w /data \
    -v "$(pwd)/app:/data/app" \
    --network=my-mysql-network \
    python:3.10.7 \
    sh -c "pip install --no-cache-dir fastapi uvicorn sqlalchemy mysql-connector-python requests pytest && uvicorn app.main:myApp --host 0.0.0.0 --reload"
```

#### MySQL Docker Container

``` shell
docker run \
    -dp 3306:3306 \
    -v my-mysql-data:/var/lib/mysql \
    --network=my-mysql-network \
    --network-alias=mysql-server \
    -e MYSQL_ROOT_PASSWORD=secret \
    -e MYSQL_DATABASE=todos \
    --platform "linux/amd64" \
    mysql:5.7

```

##### MySQL User Creation

``` sql
mysql> create database my_fast_api_db;
mysql> create user 'my_fast_api_user'@'%' identified by 'fast_api_pwd';
mysql> grant all on my_fast_api_db.* to 'my_fast_api_user'@'%';
```

## Database ORM

### SQLAlchemy

- Installation

``` shell
pip install SQLAlchemy
```

- Tutorials

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

## Test

### Pytest

- Installation

``` shell
pip install pytest
```

- Tutorials

<https://docs.pytest.org/en/7.1.x/getting-started.html>