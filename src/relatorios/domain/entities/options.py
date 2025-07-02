from pydantic import BaseModel
from typing import Optional

class Options(BaseModel):
    history: Optional[bool] = False
    total: Optional[bool] = False
    duration_average: Optional[bool] = False