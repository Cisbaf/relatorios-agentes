import pymongo, os
from controler.call import CallController
from domain.entities.register import Register
from controler.pause import PauseController
from controler.removed import RemovedController
from controler.time_line import TimeLineController
from domain.utils.type import get_type_pause

mongo_uri = "mongodb://root:7890380@45.231.133.116:27017"
name_db = "status_agent"
name_collection = "105291648767"

client = pymongo.MongoClient(mongo_uri)
db = client[name_db]
collection = db[name_collection]

# Data alvo
data_str = "09/04/2025"

# Consulta com regex
query = {
    "date_status_dt": {
        "$regex": f"^{data_str}"  # Filtra qualquer string que COMEÇA com "18/03/2025"
    }
}

# Executar a busca
resultados = [Register.build_from_dict(data) for data in list(collection.find(query))]

print(resultados)

# print(resultados)
print(len(resultados))
# # print("Quantidade de resultado", len(resultados))

# call = CallController()
# pause = PauseController()
# removed = RemovedController()


# for register in resultados:
#     call.register(register)
#     pause.register(register)
#     # removed.register(register)
    
# print(call)
# for calls in call.calls:
#     print(calls)

# print(pause)
# for p in pause.pauses:
#     print(p)

# print(pause)
#     pause.register(register)
#     removed.register(register)

# qr = {
#     'STATUS_': '1',
#     'CALLERID_R_ANI': {
#         "$regex": f"^2132936400",  # Prefix match starting with "2132936400"
#     }
# }

# calls = []
# sum = 0
# for cl in db.list_collections():
#     collection_name = cl['name']
#     result = list(db[collection_name].find(qr))
#     sum += len(result)

# print(sum)