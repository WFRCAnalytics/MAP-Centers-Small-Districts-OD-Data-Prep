#!/usr/bin/python3

# Sample API client for StreetLight Data API
# This was tested with Python 3 on Ubuntu Linux 16.04.
# Refer to the StreetLight API documentation for more information.

import datetime
import json
import requests
import sys
import time

now = datetime.datetime.utcnow().isoformat()

# Edit the following two constants to a valid key and user login.
STL_KEY = 'abcdefghijklmnop'
INSIGHT_LOGIN_EMAIL = 'edit.this@example.com'

ZONE_SET_NAME = "Two_Neighborhoods_{}".format(now)
ANALYSIS_NAME = "OD_for_TN_{}".format(now)

def print_response(response):
    print("response code: {}".format(response.status_code))
    print("response body: {}".format(response.content))


#----------------------------------------------------------------------------------------
# Create a Zone Set.
#----------------------------------------------------------------------------------------

ZONE_SET_REQUEST = {
    "insight_login_email": INSIGHT_LOGIN_EMAIL,
    "zone_set_name": ZONE_SET_NAME,
    "zones": {
        "type": "FeatureCollection",
        "features": [
            { "type": "Feature", "properties": { "id": 1, "name": "Mission", "is_pass": 0, "direction": None }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -122.426698258661972, 37.769562689936315 ], [ -122.423394859041892, 37.772083876030344 ], [ -122.42225575572462, 37.770418101996292 ], [ -122.411206453547067, 37.769427623969634 ], [ -122.406991771273155, 37.769067446852375 ], [ -122.404656609472752, 37.767716767038294 ], [ -122.405169205965521, 37.762628984940662 ], [ -122.406593085112107, 37.760557752167074 ], [ -122.405795712790038, 37.758441432691242 ], [ -122.403232730326167, 37.75722564731312 ], [ -122.402549268335804, 37.751821915004783 ], [ -122.403346640657901, 37.749390106706535 ], [ -122.407561322931784, 37.748399347080543 ], [ -122.424875693354338, 37.74781389197571 ], [ -122.426698258661972, 37.769562689936315 ] ] ] ] } },
            { "type": "Feature", "properties": { "id": 2, "name": "Financial District", "is_pass": 1, "direction": None }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -122.405425504211919, 37.798033588378779 ], [ -122.398476973976571, 37.798933675051543 ], [ -122.396654408668923, 37.799698740100226 ], [ -122.397024617247041, 37.79929370664977 ], [ -122.396768319000643, 37.798911173018389 ], [ -122.395828558763895, 37.797898574431919 ], [ -122.393607307295227, 37.799113691070012 ], [ -122.392610591892605, 37.797876072083447 ], [ -122.394233814119715, 37.79690846455324 ], [ -122.393037755636598, 37.795670808599994 ], [ -122.3913575782436, 37.796278387822021 ], [ -122.390987369665496, 37.795693311702443 ], [ -122.392439726395011, 37.794500642185817 ], [ -122.389278714689581, 37.791462623416393 ], [ -122.401182344355107, 37.781965196242638 ], [ -122.405824190372982, 37.785701296639232 ], [ -122.406222876534017, 37.785723802695827 ], [ -122.407134159187834, 37.790337399578668 ], [ -122.404058580231194, 37.790764986655553 ], [ -122.405425504211919, 37.798033588378779 ] ] ] ] } }
        ]
    }
}

resp = requests.post(
    'https://insight.streetlightdata.com/api/v2/zone_sets',
    headers = {'content-type': 'application/json', 'x-stl-key': STL_KEY},
    data = json.dumps(ZONE_SET_REQUEST))

print_response(resp)

if (resp.status_code == 201):
    print("Created Zone Set successfully.")
else:
    print("Error creating Zone Set.")
    sys.exit(1)


#----------------------------------------------------------------------------------------
# Create an O-D Analysis.
#----------------------------------------------------------------------------------------

CREATE_ANALYSIS_REQUEST = {
    "insight_login_email": INSIGHT_LOGIN_EMAIL,
    "analysis_name": ANALYSIS_NAME,
    "analysis_type": "OD_Analysis",
    "travel_mode_type": "All_Vehicles",
    "description": "",
    "oz_sets": [{"name":ZONE_SET_NAME}],
    "dz_sets": [{"name":ZONE_SET_NAME}],
    "day_types": "All Days|17, Weekday|14, Weekend Day|67",
    "day_parts": "All Day|0023, Early AM|0005, Peak AM|0609, Mid-Day|1014, Peak PM|1518, Late PM|1923",
    "trip_attributes": False,
    "traveler_attributes": False
}

resp = requests.post(
    'https://insight.streetlightdata.com/api/v2/analyses',
    headers = {'content-type': 'application/json', 'x-stl-key': STL_KEY},
    data = json.dumps(CREATE_ANALYSIS_REQUEST))

print_response(resp)

if (resp.status_code == 201):
    print("Created Analysis successfully.")
else:
    print("Error creating Analysis.")
    sys.exit(1)


#----------------------------------------------------------------------------------------
# Check the processing status of the Analysis.
#
# Note: depending on Analysis size, Analysis processing can take minutes to hours
# (for very large Analyses). A production integration should not block UI input
# from the end user while Analyses are processing, and it should resume
# gracefully when the client application is shut down and restarted while
# Analyses process.
#----------------------------------------------------------------------------------------

CHECK_STATUS_REQUEST = {
    "analyses":[{"name": ANALYSIS_NAME}]
}

while True:
    resp = requests.post(
        'https://insight.streetlightdata.com/api/v2/analyses/status',
        headers = {'content-type': 'application/json', 'x-stl-key': STL_KEY},
        data = json.dumps(CHECK_STATUS_REQUEST))

    print_response(resp)

    if (resp.status_code != 200):
        print("Error checking Analysis Status.")
        sys.exit(1)

    json_result = json.loads(resp.text)
    analysis_status = json_result["analyses"][0]["status"]

    if (analysis_status == "Available"):
        print("Analysis is Available!")
        break
    elif (analysis_status == "Processing"):
        print("Analysis is processing. Trying again after 1 minute...")
        time.sleep(60)
    else:
        print("Error running Analysis.")
        sys.exit(1)


#----------------------------------------------------------------------------------------
# Get the O-D results.
#----------------------------------------------------------------------------------------

resp = requests.get(
    'https://insight.streetlightdata.com/api/v2/analyses/download/name/{}/od_all'.format(ANALYSIS_NAME),
    headers = {'x-stl-key': STL_KEY})

# resp.text contains results in CSV format.

print_response(resp)

if (resp.status_code == 200):
    # Write results to a CSV file.
    with open("od_all.csv", "w") as csv_file:
        csv_file.write(resp.text)
    print("Check CSV file for Personal O-D results.")
else:
    print("Error fetching O-D results.")
    sys.exit(1)
