#!/bin/bash

for i in "$@"; do
  case $i in
    -o=*|--output=*)
      OUTPUT="${i#*=}"
      shift
      ;;
    -y=*|--year=*)
      YEAR="${i#*=}"
      shift
      ;;
    -*|--*)
      echo "Unknown option $i"
      exit 1
      ;;
    *)
      ;;
  esac
done

OUTPUT_FILENAME="liturgical-calendar.epub"
if [ "$OUTPUT" ]; then
  OUTPUT_FILENAME="${OUTPUT}"
fi

if [ -z "$YEAR" ]; then
  YEAR=$(date +%Y)
fi

echo "Output filename '${OUTPUT_FILENAME}'"
echo "Year: $YEAR"

DIR="$(realpath "$(dirname "$0")")"

pandoc "${DIR}"/../output_data/markdown/*.md -f markdown+pipe_tables+raw_html -t epub3 \
    -o "${DIR}"/../output_data/epub/"${OUTPUT_FILENAME}" \
    --toc --toc-depth 2 --verbose \
    --metadata title="Календарь Православных Праздников ${YEAR}" \
    --metadata author="свт. Димитрий Ростовский" \
    --epub-cover-image="${DIR}"/../images/cover.jpg