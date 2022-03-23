#!/usr/bin/env bash

# download from server
scp lsv_pc:sentence-embd-fusion/computed/*.json computed/

# upload to server
# scp computed/*.json lsv_pc:sentence-embd-fusion/computed/