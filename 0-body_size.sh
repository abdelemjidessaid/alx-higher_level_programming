#!/usr/bin/env bash
# counts the body responses.
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
