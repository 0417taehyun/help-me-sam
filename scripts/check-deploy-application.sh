# !/bin/bash

CHANGE_DIR=$(git diff --name-only HEAD^ HEAD | cut \d'/' -f1 | uniq)

echo "Changed directories: $CHANGE_DIR"

COUNT=$(echo $CHANGE_DIR | wc -w)

if [ $COUNT -ne 1 ]; then
    echo "Error: Changes must be in only one directory, but found changes in $COUNT directories."
    exit 1
fi

echo "::set-output name=changed-dir::$CHANGE_DIR"
