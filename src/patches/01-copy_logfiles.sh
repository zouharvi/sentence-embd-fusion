#!/usr/bin/env bash

if [ $# -lt 1 ]; then
    EXTENSION="json"
else
    EXTENSION=$1
fi

# download from server
rsync -avh lsv_pc:sentence-embd-fusion/computed/*.$EXTENSION computed/

# upload to server
# scp computed/*.json lsv_pc:sentence-embd-fusion/computed/