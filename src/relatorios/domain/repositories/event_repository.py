from pydantic import BaseModel
from relatorios.domain.entities.status_event import StatusEvent
from relatorios.domain.entities.options import Options
from relatorios.domain.entities.event import Event
from typing import List, Dict, Optional
from datetime import timedelta
from relatorios.domain.utils.time import format_timedelta


class EventRepository(BaseModel):
    options: Options
    _events: Optional[List[Event]] = []
    _last_status: Optional[StatusEvent] = None

    def check_and_register(self, status: StatusEvent):
        ...

    def extract(self, event: Event):
        ...

    def get_datas(self) -> Dict:
        data = {}
        if self.options.history:
            data["history"] = [self.extract(event) for event in self._events]
        if self.options.total:
            data["total"] = len(self._events)
        if self.options.duration_average:
            average_duration = None
            durations = [event.duration for event in self._events if event.duration]
            if durations:
                total_duration = sum(durations, timedelta())
                average_duration = format_timedelta(total_duration / len(durations))
            data["durationAverage"] = average_duration
        return data