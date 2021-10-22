from pymcversion import get_ios_store_lookup

def test_get_ios_store_lookup():
    lookup = get_ios_store_lookup()

    assert lookup.version != ''
