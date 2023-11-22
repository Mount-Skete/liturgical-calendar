#!/bin/bash

for i in "$@"; do
  case $i in
    -o=*|--output=*)
      OUTPUT="${i#*=}"
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

echo "Output filename '${OUTPUT_FILENAME}'"

DIR="$(realpath "$(dirname "$0")")"

pandoc "${DIR}"/../output_data/markdown/*.md -f markdown+pipe_tables -t epub3 \
    -o "${DIR}"/../output_data/epub/"${OUTPUT_FILENAME}" \
    --toc --toc-depth 2 --verbose \
    --metadata title="Церковный Календарь" \
#    --metadata author="свт. Димитрий Ростовский"