from pymcversion import get_bedrock_server_latest_version

def test_get_bedrock_server_latest_version():
    info = get_bedrock_server_latest_version()

    assert info.linux.url != ''
    assert info.linux.version != ''

    assert info.win.url != ''
    assert info.win.version != ''
