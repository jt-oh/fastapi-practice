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
    sh -c "pip install --no-cache-dir fastapi uvicorn && uvicorn main:myApp --host 0.0.0.0 --reload"
```
