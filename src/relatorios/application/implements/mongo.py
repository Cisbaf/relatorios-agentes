import pymongo
from relatorios.domain.entities.date_range import DateRange

mongo_uri = "mongodb://root:7890380@45.231.133.116:27017"
name_db = "status_agent"

def get_collection(name: str):
    client = pymongo.MongoClient(mongo_uri)
    db = client[name_db]
    collection = db[name]
    return collection


def execute_query_filter_date(id_callroute: str, date: DateRange):
    collection = get_collection(id_callroute)
    date_range = date.get_date_range()
    results = []
    for date in date_range:
        query = {
            "date_status_dt": {
                "$regex": f"^{date}"
            }
        }
        results.extend(list(collection.find(query)))
    return results