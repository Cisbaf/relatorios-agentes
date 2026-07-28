import os

import pymongo
from relatorios.domain.entities.date_range import DateRange

mongo_uri = os.getenv("MONGO_URI")
name_db = os.getenv("MONGO_DB", "status_agent")

if not mongo_uri:
    raise RuntimeError("Variável de ambiente MONGO_URI não configurada")

_client = pymongo.MongoClient(mongo_uri)


def get_collection(name: str):
    db = _client[name_db]
    collection = db[name]
    return collection


def execute_query_filter_date(id_callroute: str, date: DateRange):
    """
    Busca os registros de um agente dentro do intervalo de datas informado.

    Usa uma única query com $gte/$lte sobre o campo date_status_dt_iso
    (Date nativo do MongoDB, indexado), em vez do padrão anterior de
    disparar uma query com $regex por dia do intervalo — que exigia N
    varreduras completas da collection (uma por dia), sem uso de índice.

    IMPORTANTE sobre ordenação: os resultados são ordenados por _id (ordem
    de inserção no MongoDB), e não por date_status_dt_iso. Isso é proposital
    e preserva o comportamento da implementação anterior (que não ordenava
    explicitamente e dependia da ordem natural de inserção do Mongo).

    O campo date_status_dt/date_status_dt_iso é calculado no producer como
    "agora menos tempo decorrido desde a última mudança", o que significa
    que NÃO é estritamente monotônico em relação à ordem real de coleta —
    dois documentos podem ter seus timestamps calculados "fora de ordem"
    por alguns segundos mesmo quando um foi de fato gravado depois do outro.

    Serviços como RemovedService dependem da sequência exata em que os
    eventos foram processados para detectar corretamente transições de
    estado (ex: RINGING seguido de IsRemoved). Ordenar por date_status_dt_iso
    em vez de _id pode inverter a ordem relativa de eventos próximos no
    tempo e mudar o resultado dessas análises — por isso mantemos _id como
    critério de ordenação, e usamos date_status_dt_iso apenas para o FILTRO
    de intervalo (onde o ganho de performance do índice se aplica).
    """
    collection = get_collection(id_callroute)
    start, end = date.get_datetime_range()

    query = {
        "date_status_dt_iso": {
            "$gte": start,
            "$lte": end,
        }
    }
    return list(collection.find(query).sort("_id", pymongo.ASCENDING))
