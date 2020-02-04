import logging
import sys
from fflogs_fight_analyzer import fflogs


def main():
    client = fflogs.Client()
    client.get("zones")


if __name__ == "__main__":
    LOGGER = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    sys.exit(main())
