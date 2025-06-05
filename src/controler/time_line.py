from domain.entities import Status, Register
from typing import List


class TimeLineController:

    def __init__(self, registers: List[Register]):
        self.registers = registers


    def get_time_line(self) -> List[Status]:
        if not self.registers:
            return []

        last_status = None
        last_value_status = None
        status = []

        for register in self.registers:
            if register.status_agent != last_value_status:
                if last_status is not None:
                    last_status.finalised = True
                    last_status.end = register.dt_status_agent
                    status.append(last_status)

                last_status = Status(register.status_agent, [register], register.dt_status_agent, None)
                last_value_status = register.status_agent
            else:
                last_status.registers.append(register)

        # Adiciona o último status após o loop
        if last_status is not None:
            status.append(last_status)

        return status