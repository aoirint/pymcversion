from pymcversion import (
    get_bedrock_server_latest_version,
    get_java_version_manifest,
    get_ios_store_lookup,
)

def command_bedrock_server_linux_version(args):
    print(get_bedrock_server_latest_version().linux.version)

def command_bedrock_server_linux_url(args):
    print(get_bedrock_server_latest_version().linux.url)

def command_java_version(args):
    print(get_java_version_manifest().latest.release)

def command_ios_version(args):
    print(get_ios_store_lookup().version)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_bedrock = subparsers.add_parser('bedrock-server')
    parser_bedrock.set_defaults(handler=command_bedrock_server_linux_version)
    subparsers_bedrock = parser_bedrock.add_subparsers()
    parser_bedrock_linux_version = subparsers_bedrock.add_parser('linux-version')
    parser_bedrock_linux_version.set_defaults(handler=command_bedrock_server_linux_version)
    parser_bedrock_linux_url = subparsers_bedrock.add_parser('linux-url')
    parser_bedrock_linux_url.set_defaults(handler=command_bedrock_server_linux_url)

    parser_java = subparsers.add_parser('java')
    parser_java.set_defaults(handler=command_java_version)
    subparsers_java = parser_java.add_subparsers()
    parser_java_version = subparsers_java.add_parser('version')
    parser_java_version.set_defaults(handler=command_java_version)

    parser_ios = subparsers.add_parser('ios')
    parser_ios.set_defaults(handler=command_ios_version)
    subparsers_ios = parser_ios.add_subparsers()
    parser_ios_version = subparsers_ios.add_parser('version')
    parser_ios_version.set_defaults(handler=command_ios_version)

    args = parser.parse_args()

    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()
