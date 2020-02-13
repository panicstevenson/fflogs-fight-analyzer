import argparse
import logging
import os
import sys
from fflogs_fight_analyzer import fflogs


def _create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="fflogs_fight_analyzer",
        description="Simple interface to parse elements and events from FF Logs' web API.",
    )
    parser.add_argument(
        "--api-key",
        type=str,
        help="FF Logs public API key, which can be found at https://www.fflogs.com/profile",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug level logging, increasing verbosity for all requests",
    )
    return parser


def _main(args: argparse.Namespace):
    # prefer passed in CLI argument over environment variable
    api_key = args.api_key or os.getenv("FF_LOGS_API_KEY")
    client = fflogs.Client(api_key)
    client.get("zones")


if __name__ == "__main__":
    ARGUMENTS = _create_argument_parser().parse_args()
    LOGGING_LEVEL = logging.DEBUG if ARGUMENTS.debug else logging.INFO
    logging.basicConfig(level=LOGGING_LEVEL, format="%(levelname)s: %(message)s")
    sys.exit(_main(ARGUMENTS))
