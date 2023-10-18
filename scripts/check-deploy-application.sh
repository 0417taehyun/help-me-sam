#!/bin/bash

CHANGED_DIRECTORIES=$(git diff --name-only HEAD^ HEAD | grep '/' | awk -F/ '{ print $1 }' | uniq)
echo "Changed directories: \n$CHANGED_DIRECTORIES"

COUNT=$(echo $CHANGED_DIRECTORIES | wc -w)

if [ $COUNT -ne 1 ]; then
    echo "Error: Only one application directory must be changed, but found $COUNT."
    exit 1
fi

echo "::set-output name=changed-application::$CHANGED_DIRECTORIES"
echo "::set-output name=changed-count::$COUNT"
