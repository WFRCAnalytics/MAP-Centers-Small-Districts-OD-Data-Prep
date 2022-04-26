#!/bin/bash

curl -i -d @query-analysis-status.json \
     -H "content-type:application/json" \
     https://insight.streetlightdata.com/api/v2/analyses/status?key=SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1
