from pymcversion import get_java_version_manifest

def test_get_java_version_manifest():
    manifest = get_java_version_manifest()

    assert manifest.latest.release != ''
