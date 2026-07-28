import os
from unittest.mock import MagicMock, patch

import pytest

os.environ.setdefault("MONGO_URI", "mongodb://user:pass@localhost:27017")

from relatorios.domain.entities.date_range import DateRange


@pytest.fixture
def mock_client():
    with patch("relatorios.application.implements.mongo.pymongo.MongoClient") as mock_cls:
        mock_instance = MagicMock()
        mock_cls.return_value = mock_instance
        yield mock_instance


def test_execute_query_filter_date_uses_single_gte_lte_query(mock_client):
    from relatorios.application.implements import mongo as mongo_module

    mock_collection = MagicMock()
    mock_collection.find.return_value.sort.return_value = ["doc1", "doc2"]
    mongo_module._client = mock_client
    mock_client.__getitem__.return_value.__getitem__.return_value = mock_collection

    date_range = DateRange(start="01/03/2025", end="31/03/2025")
    result = mongo_module.execute_query_filter_date("AGENTE123", date_range)

    assert result == ["doc1", "doc2"]
    # Uma única chamada ao find (não uma por dia do intervalo)
    mock_collection.find.assert_called_once()
    query_arg = mock_collection.find.call_args[0][0]
    assert "date_status_dt_iso" in query_arg
    assert "$gte" in query_arg["date_status_dt_iso"]
    assert "$lte" in query_arg["date_status_dt_iso"]


def test_execute_query_filter_date_query_bounds_match_date_range(mock_client):
    from relatorios.application.implements import mongo as mongo_module

    mock_collection = MagicMock()
    mock_collection.find.return_value.sort.return_value = []
    mongo_module._client = mock_client
    mock_client.__getitem__.return_value.__getitem__.return_value = mock_collection

    date_range = DateRange(start="10/03/2025", end="10/03/2025")
    mongo_module.execute_query_filter_date("AGENTE123", date_range)

    query_arg = mock_collection.find.call_args[0][0]
    expected_start, expected_end = date_range.get_datetime_range()
    assert query_arg["date_status_dt_iso"]["$gte"] == expected_start
    assert query_arg["date_status_dt_iso"]["$lte"] == expected_end


def test_execute_query_filter_date_sorts_by_id_not_by_timestamp(mock_client):
    """
    A ordenação deve ser por _id (ordem de inserção), não por
    date_status_dt_iso. O campo de timestamp é calculado no producer e não
    é estritamente monotônico em relação à ordem real de gravação — ordenar
    por ele pode inverter a sequência de eventos próximos no tempo e mudar
    o resultado de serviços que dependem de ordem (ex: RemovedService).
    """
    from relatorios.application.implements import mongo as mongo_module

    mock_collection = MagicMock()
    mock_collection.find.return_value.sort.return_value = []
    mongo_module._client = mock_client
    mock_client.__getitem__.return_value.__getitem__.return_value = mock_collection

    date_range = DateRange(start="01/03/2025", end="31/03/2025")
    mongo_module.execute_query_filter_date("AGENTE123", date_range)

    mock_collection.find.return_value.sort.assert_called_once_with("_id", 1)
