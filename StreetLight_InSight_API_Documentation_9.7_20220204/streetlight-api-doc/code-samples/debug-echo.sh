#!/bin/bash

curl -i -d '{"message": "hello world"}' \
     -H "content-type: application/json" \
     https://insight.streetlightdata.com/api/v2/debug/echo?key=SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1
