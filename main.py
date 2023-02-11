from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_hello_world() -> Dict:
    return {'hello': 'world'}


@app.get('/event/{id_}')
def get_event(id_: int) -> Dict:
    return {'id': id_, 'name': f'Event {id_}', 'start': '2023-01-01', 'end': ''}
