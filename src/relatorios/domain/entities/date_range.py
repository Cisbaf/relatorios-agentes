from datetime import datetime
from pydantic import BaseModel
from datetime import timedelta

class DateRange(BaseModel):
    start: str
    end: str

    def get_date_range(self) -> list[str]:
        """Retorna um array com todas as datas no intervalo (formato DD/MM/YYYY)"""
        date_format = "%d/%m/%Y"
        
        start = datetime.strptime(self.start, date_format)
        end = datetime.strptime(self.end, date_format)
        date_list = []
        current_date = start
        
        while current_date <= end:
            date_list.append(current_date.strftime(date_format))
            current_date += timedelta(days=1)
        return date_list
