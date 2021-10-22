from pymcversion import get_bedrock_server_latest_version

def test_get_bedrock_server_latest_version():
    version = get_bedrock_server_latest_version()

    assert version != ''
