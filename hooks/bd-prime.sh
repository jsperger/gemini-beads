#!/bin/bash

# Note: bd prime only prints instructions if .beads/ exists
CONTENT=$(bd prime --full 2>/dev/null)
if [ -n "$CONTENT" ]; then
  jq -n --arg msg "$CONTENT" '{"systemMessage": $msg}'
fi
