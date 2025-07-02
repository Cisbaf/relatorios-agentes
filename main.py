from relatorios.domain.entities.date_range import DateRange
from relatorios.domain.controller.event_controller import EventController
from relatorios.domain.entities.options import Options
from fastapi import FastAPI

app = FastAPI()

@app.post("/consult")
def execute(params: EventController):
    return params.execute()
