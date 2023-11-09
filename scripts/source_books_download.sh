#!/bin/bash

DIR="$(realpath "$(dirname "$0")")"
URL='https://ws-export.wmcloud.org/?format=epub&lang=ru&page=%D0%96%D0%B8%D1%82%D0%B8%D1%8F_%D1%81%D0%B2%D1%8F%D1%82%D1%8B%D1%85_%D0%BF%D0%BE_%D0%B8%D0%B7%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8E_%D1%81%D0%B2%D1%82._%D0%94%D0%B8%D0%BC%D0%B8%D1%82%D1%80%D0%B8%D1%8F_%D0%A0%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BE'
curl -L -o "${DIR}/../source_data/saints_book.epub" "$URL"