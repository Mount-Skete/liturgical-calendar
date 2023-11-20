#!/bin/bash

pandoc output_data/markdown/*.md -f markdown+pipe_tables -t epub3 \
    -o output_data/epub/liturgical-calendar.epub \
    --toc --toc-depth 2 --verbose \
    --metadata title="Церковный Календарь" \
#    --metadata author="свт. Димитрий Ростовский"