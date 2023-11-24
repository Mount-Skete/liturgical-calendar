#!/bin/bash

for i in "$@"; do
  case $i in
    -v=*|--version=*)
      VERSION="${i#*=}"
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

if [ "$VERSION" ]; then
  echo "Releasing version $VERSION"
  git tag -s -a "$VERSION" -m "$VERSION"
else
  echo "Usage: create-release.sh -v=v1.0.0"
fi
