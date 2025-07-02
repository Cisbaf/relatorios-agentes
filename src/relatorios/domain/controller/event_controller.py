from pydantic import BaseModel
from relatorios.domain.entities.date_range import DateRange
from relatorios.domain.entities.options import Options
from relatorios.domain.entities.status_event import StatusEvent
from relatorios.domain.services.pause_service import PauseService
from relatorios.domain.services.removed_service import RemovedService
from relatorios.application.implements.mongo import execute_query_filter_date
from typing import Literal, List

events_list = Literal["pause", "removed"]

class EventController(BaseModel):
    events: List[events_list]
    agents_id : List[str]
    date_rage: DateRange
    options: Options
    
    def _get_event_(self, event_name: events_list):
        if event_name == "pause":
            return PauseService(options=self.options)
        if event_name == "removed":
            return RemovedService(options=self.options)

    def execute(self):
        data = {}
        events = [self._get_event_(event) for event in self.events]
        for agent_id in self.agents_id:
            agent_data = {}
            status_list = [StatusEvent.build_from_dict(register) for register in
                execute_query_filter_date(agent_id, self.date_rage)]
            for status in status_list:
                for event in events:
                    event.check_and_register(status)
            for i, event in enumerate(self.events):
                agent_data[event] = events[i].get_datas()
            data[agent_id] = agent_data
        return data
