#!/bin/bash
# A script that sends a request and displays the status code of the response
curl -o /dev/null -w '%{http_code}' -sLI "$1"
