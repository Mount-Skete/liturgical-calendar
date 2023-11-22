from argparse import ArgumentParser
from datetime import datetime

from book import Book

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-y",
                        dest="year",
                        type=int,
                        required=False,
                        action="store",
                        help='Book calendar year',
                        default=datetime.now().year)

    args = parser.parse_args()

    book = Book(args.year)
    book.create()
