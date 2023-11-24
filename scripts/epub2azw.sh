#!/bin/bash

for i in "$@"; do
  case $i in
    -i=*|--input=*)
      INPUT="${i#*=}"
      shift
      ;;
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

INPUT_FILENAME="liturgical-calendar.epub"
if [ "$INPUT" ]; then
  INPUT_FILENAME="${INPUT}"
fi

OUTPUT_FILENAME="liturgical-calendar.azw3"
if [ "$OUTPUT" ]; then
  OUTPUT_FILENAME="${OUTPUT}"
fi

echo "Input filename '${INPUT_FILENAME}'"
echo "Output filename '${OUTPUT_FILENAME}'"

DIR="$(realpath "$(dirname "$0")")"

ebook-convert "${DIR}"/../output_data/epub/"${INPUT_FILENAME}" \
             "${DIR}"/../output_data/azw/"${OUTPUT_FILENAME}" \
#             --dont-compress
