import pymongo
from datetime import datetime, timedelta

mongo_uri = "mongodb://root:7890380@45.231.133.116:27017"
name_db = "status_agent"

def get_collection(name: str):
    client = pymongo.MongoClient(mongo_uri)
    db = client[name_db]
    collection = db[name]
    return collection

def get_date_range(start_date: str, end_date: str) -> list[str]:
    """Retorna um array com todas as datas no intervalo (formato DD/MM/YYYY)"""
    date_format = "%d/%m/%Y"
    
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)
    date_list = []
    current_date = start
    
    while current_date <= end:
        date_list.append(current_date.strftime(date_format))
        current_date += timedelta(days=1)
    return date_list

def execute_query_filter_date(id_callroute: str, start_date: str, end_date: str):
    collection = get_collection(id_callroute)
    date_range = get_date_range(start_date, end_date)
    results = []
    for date in date_range:
        query = {
            "date_status_dt": {
                "$regex": f"^{date}"
            }
        }
        results.extend(list(collection.find(query)))
    return results