import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="ip address for server to listen on, defaults to 0.0.0.0"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="port for server to be hosted on, defaults to 8000"
    )
    parser.add_argument(
        "--reload",
        type=bool,
        required=True,
        help="boolean for the uvicorn run command's 'reload' parameter"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        default=0,
        help="increase logging verbosity; can be used multiple times",
    )
    
    return parser.parse_args()
