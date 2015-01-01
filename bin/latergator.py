from __future__ import print_function

import sys

from alligator import Gator, Worker


def main(dsn):
    gator = Gator(dsn)

    worker = Worker(gator)
    worker.run_forever()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python latorgator.py <DSN>')
        sys.exit(1)

    dsn = sys.argv[2]
    main(dsn)
