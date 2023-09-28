#!/usr/bin/env bash
# counts the body responses.
url=$1
response=$(curl -s -o /dev/null -w "%{size_download}" $url)
echo "$response"
