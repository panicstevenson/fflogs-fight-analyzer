#!/usr/bin/env python

import logging
import sys
import fflogs


def main():
    client = fflogs.Client()


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    sys.exit(main())
