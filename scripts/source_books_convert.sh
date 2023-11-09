#!/bin/bash

DIR="$(realpath "$(dirname "$0")")"
#pandoc -f epub -t html4 \
#       -o "${DIR}/../source_data/saints_book.html" \
#       "${DIR}/../source_data/saints_book.epub" \
#       --standalone \
#       --embed-resources

pandoc -f epub -t html4 \
       -o "${DIR}/../source_data/saints_book.html" \
       "${DIR}/../source_data/saints_book.epub"
