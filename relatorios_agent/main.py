import pymongo
from domain.status_event.entities.status_event import StatusEvent
from application.controller.status_ramal_controller import StatusRamalController
from application.controller.status_agent_controller import StatusAgentController
from domain.status_ramal.entities.call import Call
from domain.status_event.values_object.type_status_agent import TypeStatusAgent
from domain.status_agent.entities.pause import Pause
from domain.status_agent.entities.removed import Removed


mongo_uri = "mongodb://root:7890380@45.231.133.116:27017"
name_db = "status_agent"
name_collection = "174231413720"

client = pymongo.MongoClient(mongo_uri)
db = client[name_db]
collection = db[name_collection]

# Data alvo
data_str = "30/05/2025"

# Consulta com regex
query = {
    "date_status_dt": {
        "$regex": f"^{data_str}"  # Filtra qualquer string que COMEÇA com "18/03/2025"
    }
}

# Executar a busca
resultados = [StatusEvent.build_from_dict(data) for data in list(collection.find(query))]
for result in resultados:
    print(result)
    print("")
controller = StatusAgentController()

events = [controller.get(event) for event in resultados]

removeds = [event for event in events if isinstance(event, Removed)]