import argparse
import logging
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
    return parser


def _main(args: argparse.Namespace):
    client = fflogs.Client(args.api_key)
    client.get("zones")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    sys.exit(_main(_create_argument_parser().parse_args()))
