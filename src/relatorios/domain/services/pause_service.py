from relatorios.domain.repositories.event_repository import EventRepository, Event
from relatorios.domain.values_object.type_status_agent import TypeStatusAgent
from relatorios.domain.values_object.type_pause import TypePause
from relatorios.domain.utils.time import format_timedelta

class PauseService(EventRepository):

    def check_and_register(self, status):
        if len(self._events) > 0:
            event = self._events[-1]
            if not event.end:
                event.end = status.dt_status_agent
                event.duration = event.end - event.start

        if status.status_agent == TypeStatusAgent.IsOnBreak:
            self._events.append(Event(
                status=status,
                start=status.dt_status_agent
        ))
            
        self._last_status = status
        
    def extract(self, event):
        return {
            "type": TypePause.get(event.status.cod_pause).name,
            "duration": format_timedelta(event.duration),
            "date": event.status.dt_status_agent.strftime("%d/%m/%Y, %H:%M:%S")
        }
        