from weatherkit.cache import TTLCache


def test_set_and_get():
    cache = TTLCache(ttl_seconds=60)
    cache.set("Madrid", {"temp_c": 20})
    assert cache.get("Madrid") == {"temp_c": 20}


def test_missing_key():
    assert TTLCache().get("Lisbon") is None
