#!/usr/bin/env python

import logging
import sys
import client


def main():
    client.Client()


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    sys.exit(main())
