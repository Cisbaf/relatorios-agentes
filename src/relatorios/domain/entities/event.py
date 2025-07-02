from pydantic import BaseModel
from relatorios.domain.entities.status_event import StatusEvent
from typing import Optional, Dict
from datetime import datetime, timedelta

class Event(BaseModel):
    status: StatusEvent
    start: datetime
    end: Optional[datetime] = None
    duration: Optional[timedelta] = None
    extra: Optional[Dict] = None