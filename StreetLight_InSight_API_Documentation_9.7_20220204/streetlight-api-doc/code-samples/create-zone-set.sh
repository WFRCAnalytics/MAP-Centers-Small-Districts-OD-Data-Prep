#!/bin/bash

curl -i -d @zones.json \
     -H "Content-Type: application/json" \
     https://insight.streetlightdata.com/api/v2/zone_sets?key=SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1
