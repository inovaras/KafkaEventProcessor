from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from kafka import KafkaProducer


router = APIRouter()


class Event(BaseModel):
    timestamp: str
    user_id: str
    payload: dict

producer = KafkaProducer(bootstrap_servers=['172.18.0.17:9094'],
                         api_version=(0,11,5))

@router.post("/kafka/event", response_model=Event, description="Отправка сообщения в kafka.")
def create_event(event: Event):
    try:
        value = event.model_dump_json().encode('utf-8')
        producer.send(
            topic='messages',
            value=value,
            key=b'from-api-kafka-messages',
            )
        producer.flush()
        return event
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
