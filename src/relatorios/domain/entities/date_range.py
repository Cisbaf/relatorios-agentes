from datetime import datetime, timedelta
from typing import ClassVar

from pydantic import BaseModel


class DateRange(BaseModel):
    start: str
    end: str

    # Datas recebidas e armazenadas no MongoDB (campos *_dt_iso) representam
    # horário LOCAL de Brasília, sem informação de fuso (datetime "naive").
    # Os limites de consulta abaixo são construídos no mesmo referencial,
    # para que a comparação com o banco seja consistente.
    DATE_FORMAT: ClassVar[str] = "%d/%m/%Y"

    def get_datetime_range(self) -> tuple[datetime, datetime]:
        """Retorna (início, fim) como datetime, cobrindo o intervalo completo
        de dias solicitado: do início do primeiro dia (00:00:00) ao fim do
        último dia (23:59:59.999999), inclusive."""
        start = datetime.strptime(self.start, self.DATE_FORMAT)
        end = datetime.strptime(self.end, self.DATE_FORMAT)
        end_of_last_day = end + timedelta(days=1) - timedelta(microseconds=1)
        return start, end_of_last_day
