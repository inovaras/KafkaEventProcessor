from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from kafka import KafkaProducer
from contextlib import asynccontextmanager
from api.v1 import kafka_event
from time import sleep

def func():
    producer = KafkaProducer(bootstrap_servers=['172.18.0.17:9094'], api_version=(0,11,5))
    while True:
        producer.send(
            topic='messages',
            value=b'my supernewmessage',
            key=b'supernew-test-message',
        )
        print('Отправил сообщение')
        sleep(3)

@asynccontextmanager
async def lifespan(_: FastAPI):
    print("successful")
    # func()

    yield
    print("bye")

app = FastAPI(lifespan=lifespan)
app.include_router(kafka_event.router, prefix="/api/v1", tags=["kafka_event"])


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body},
    )