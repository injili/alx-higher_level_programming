#!/bin/bash
# A script that takes in a URL and displays all HTTP methods the serer will accept
curl -sI $1 | grep -i Allow: | cut -b 8-
