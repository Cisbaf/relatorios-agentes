from domain.entities.enum import TypeStatusAgent, TypeStatusRamal, TypePause

def get_type_status_agent(value: int):
    return TypeStatusAgent.get(value)

def get_type_status_ramal(value: int):
    return TypeStatusRamal.get(value)

def get_type_pause(value: int):
    return TypePause.get(value)
