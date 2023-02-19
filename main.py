import json
from typing import Dict

from fastapi import FastAPI
from mongoengine import connect

from src.models import Event as EventModel
from src.schemas import Event as EventSchema


app = FastAPI()
connect('test', host='127.0.0.1', port=27017)


@app.get('/')
def get_hello_world() -> Dict:
    return {'hello': 'world'}


@app.get('/events')
def get_events() -> Dict:
    return {'events': [json.loads(o.to_json()) for o in EventSchema.objects]}


@app.get('/event/{id_}')
def get_event(id_: str) -> Dict:
    return json.loads(EventSchema.objects.get(id=id_).to_json())


@app.post("/event")
def post_event(event_model: EventModel) -> Dict:
    event_schema = EventSchema(**event_model.dict())
    event_schema.save()
    return json.loads(event_schema.to_json())
