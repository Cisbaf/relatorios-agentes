from fastapi import FastAPI
from api.services.mongo import execute_query_filter_date
from relatorios_agent.application.controller.status_agent_controller import StatusAgentController
from relatorios_agent.application.controller.status_ramal_controller import StatusRamalController
from relatorios_agent.domain.status_event.entities.status_event import StatusEvent
from relatorios_agent.domain.status_agent.entities.removed import Removed
from relatorios_agent.domain.status_agent.entities.pause import Pause
from relatorios_agent.domain.status_ramal.entities.call import Call
from pydantic import BaseModel

app = FastAPI()

class DataSearch(BaseModel):
    id_callrout: str
    start_date: str
    end_date: str


@app.post("/removeds")
def removeds(data: DataSearch):
    controller = StatusAgentController()
    registers = [StatusEvent.build_from_dict(register) for register in
                execute_query_filter_date(data.id_callrout, data.start_date, data.end_date)]
    events = [controller.get(event) for event in registers]
    removeds = [event for event in events if isinstance(event, Removed)]
    return removeds


@app.post("/calls")
def calls(data: DataSearch):
    controller = StatusRamalController()
    registers = [StatusEvent.build_from_dict(register) for register in
            execute_query_filter_date(data.id_callrout, data.start_date, data.end_date)]
    events = [controller.get(event) for event in registers]
    calls = [event for event in events if isinstance(event, Call)]
    return calls

@app.post("/pauses")
def pauses(data: DataSearch):
    controller = StatusAgentController()
    registers = [StatusEvent.build_from_dict(register) for register in
            execute_query_filter_date(data.id_callrout, data.start_date, data.end_date)]
    events = [controller.get(event) for event in registers]
    pauses = [event for event in events if isinstance(event, Pause)]
    return pauses

