#!/bin/bash

pandoc output_data/markdown/*.md -f markdown+pipe_tables -t pdf \
    -o output_data/pdf/liturgical-calendar.pdf \
    --toc --toc-depth 2 --verbose \
    --metadata title="Церковный Календарь" \
    --metadata author="свт. Димитрий Ростовский" \
    --pdf-engine=xelatex \
    -V fontenc=T2A \
    --variable sansfont=Ubuntu \
    --variable mainfont=Ubuntu