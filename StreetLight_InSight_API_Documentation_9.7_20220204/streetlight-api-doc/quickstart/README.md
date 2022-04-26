# StreetLight InSight® Data API Quick Start

This is a short end-to-end technical example to get you up and running with the StreetLight InSight Data API. With the Data API, you can create zone sets and analyses, query the status of analyses, and download metrics for analyses that the system has made available.

The Data API is a REST+JSON API that uses HTTPS as its network protocol. You are free to use any language to implement the client side of this protocol. In the following example, we will use the [curl](https://curl.haxx.se) command-line utility. In practice, you will probably want to use a full-fledged programming language to implement your API client. The example below has been tested on Linux.

Refer to the [API Reference](../reference) after going through this Quick Start guide for more details about each API operation.

You can download the code samples given here from the [code-samples](../code-samples) folder. Before you can run them, you need to edit them to use your organization's API key instead of the one here (which is invalid and will not work). You also need to update the UUIDs in the requests to match the ones you receive from the server.

# Before You Begin

Before you begin, obtain an API key for your organization from your StreetLight Data representative. Keep this API key secure as it grants access to your organization's data in StreetLight InSight. You must also obtain an application login to the StreetLight InSight® web UI. For debugging purposes, you can use the web UI to view zone sets and analyses that you create using this API.

Note: The API key in the examples below is a sample key and is not valid nor will it work if you use it for implementation.

API keys plus HTTPS provide basic security for API requests. Talk with your StreetLight Data representative if your organization would like to upgrade your API traffic to a token-based authentication scheme for higher security. Note that a token-based authentication scheme may require slightly more programming on the client-side.

# Notes and Limitations

Keep the following in mind when working with the StreetLight Data API:
In this release, analyses that include zones with insufficient coverage will be sent to coverage review by StreetLight Data's Support team. The product does not yet support a workflow that processes the covered subset of analysis zones without human intervention.

In addition, there are rate limits on API routes. Users who are creating multiple analyses using the API will typically use a script to call the endpoints and if no wait time is done between calls then they could run into `HTTP 429` errors. Below are the existing limits:

| Endpoint                                                               | Limit               |
| :-----------                                                           | :-----------        |
| POST /api/v2/analyses                                                  | 10 per minute       |
| POST /api/v2/analyses/status                                           | 3 per 15 seconds    |
| /api/v2/* (default limit on all API routes, including the above two)   | 1 per second        |


# Confirm Connectivity Using Your API Key

You must provide your API key in each request to identify your organization to StreetLight's servers. Provide your API key using a query parameter named `key`. The query parameter is the part of the request URL after the question mark. Alternatively, you can pass the key using the HTTP header `x-stl-key`. The server returns a `401 Unauthorized` status code if authentication fails.

We have provided a debug endpoint that echoes back a message in the request body to help test your connection and authenticate successfully to StreetLight's API server. This endpoint is for debugging only. You do not need to use it in production to create analyses or get metrics.

Create a file called debug-echo.sh with the contents below and make it executable. Substitute your organization's API key in the query string (after the question mark).

    #!/bin/bash

    curl -i -d '{"message": "hello world"}' \
        -H "content-type: application/json" \
        https://insight.streetlightdata.com/api/v2/debug/echo?key=SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1

Run ./debug-echo.sh from the command line to verify that you can connect to StreetLight's server and successfully authenticate using your API key. If you receive a HTTP `200 OK` response, this test was successful.

    $ ./echo.sh
    HTTP/1.1 200 OK
    Date: Sat, 01 Apr 2017 23:42:28 GMT
    Content-Type: application/json
    Content-Length: 55
    Connection: keep-alive
    Set-Cookie: __cfduid=de8ff844541eaa29a65ea6870b508baa71491090148; expires=Sun, 01-Apr-18 23:42:28 GMT; path=/; domain=.streetlightdata.com; HttpOnly
    Signature: 08a12cbd0e03edec92da03abb8ad3d0a17507b63
    Cache-Control: no-cache, no-store, must-revalidate
    Pragma: no-cache
    Expires: 0
    Server: cloudflare-nginx
    CF-RAY: 348f67b478f951ca-SJC

    {
      "message": "hello world",
      "status": "success"
    }


# Create a Zone Set

Create a file called zones.json with the contents below. It defines two zones in a GeoJSON feature collection where each feature is a MultiPolygon. Note that zones can be GeoJSON MultiPolygons or LineStrings. Each zone must have the following four properties: `name` (required), `id` (integer, nullable), `is_pass` (either 0 for no or 1 for yes), and `direction` (decimal degrees from 0 to 360, only applicable if `is_pass` is equal to 1). The property `geom_type` is optional with default value of `polygon`. The property `insight_login_email` is required and the user must have access to the specified organization to create a zone set.

Refer to the GeoJSON spec at [http://geojson.org/](http://geojson.org/) for details on the GeoJSON format.

    {
    "insight_login_email":"testemail@streetlightdata.com",
    "geom_type": "polygon",
    "zones": {
    "type": "FeatureCollection",
    "features": [
    { "type": "Feature", "properties": { "id": 1, "name": "Mission", "is_pass": 0, "direction": null }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -122.426698258661972, 37.769562689936315 ], [ -122.423394859041892, 37.772083876030344 ], [ -122.42225575572462, 37.770418101996292 ], [ -122.411206453547067, 37.769427623969634 ], [ -122.406991771273155, 37.769067446852375 ], [ -122.404656609472752, 37.767716767038294 ], [ -122.405169205965521, 37.762628984940662 ], [ -122.406593085112107, 37.760557752167074 ], [ -122.405795712790038, 37.758441432691242 ], [ -122.403232730326167, 37.75722564731312 ], [ -122.402549268335804, 37.751821915004783 ], [ -122.403346640657901, 37.749390106706535 ], [ -122.407561322931784, 37.748399347080543 ], [ -122.424875693354338, 37.74781389197571 ], [ -122.426698258661972, 37.769562689936315 ] ] ] ] } },
    { "type": "Feature", "properties": { "id": 2, "name": "Financial District", "is_pass": 0, "direction": null }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -122.405425504211919, 37.798033588378779 ], [ -122.398476973976571, 37.798933675051543 ], [ -122.396654408668923, 37.799698740100226 ], [ -122.397024617247041, 37.79929370664977 ], [ -122.396768319000643, 37.798911173018389 ], [ -122.395828558763895, 37.797898574431919 ], [ -122.393607307295227, 37.799113691070012 ], [ -122.392610591892605, 37.797876072083447 ], [ -122.394233814119715, 37.79690846455324 ], [ -122.393037755636598, 37.795670808599994 ], [ -122.3913575782436, 37.796278387822021 ], [ -122.390987369665496, 37.795693311702443 ], [ -122.392439726395011, 37.794500642185817 ], [ -122.389278714689581, 37.791462623416393 ], [ -122.401182344355107, 37.781965196242638 ], [ -122.405824190372982, 37.785701296639232 ], [ -122.406222876534017, 37.785723802695827 ], [ -122.407134159187834, 37.790337399578668 ], [ -122.404058580231194, 37.790764986655553 ], [ -122.405425504211919, 37.798033588378779 ] ] ] ] } }
    ]
    }}

Create a file called create-zone-set.sh with contents like the ones below and make it executable. Substitute your organization's API key in the query string.

    #!/bin/bash

    curl -i -d @zones.json \
        -H "content-type: application/json" \
        https://insight.streetlightdata.com/api/v2/zone_sets?key=SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1

Run ./create-zone-set.sh from the command line:

    $ ./create-zone-set.sh
    HTTP/1.1 100 Continue

    HTTP/1.1 201 CREATED
    Date: Fri, 07 Apr 2017 04:12:20 GMT
    Content-Type: application/json
    Content-Length: 128
    Connection: keep-alive
    Set-Cookie: __cfduid=de80e418234dff51a8a3b431f3cf392081491538339; expires=Sat, 07-Apr-18 04:12:19 GMT; path=/; domain=.streetlightdata.com; HttpOnly
    Signature: 08a12cbd0e03edec92da03abb8ad3d0a17507b63
    Cache-Control: no-cache, no-store, must-revalidate
    Pragma: no-cache
    Expires: 0
    Server: cloudflare-nginx
    CF-RAY: 34ba25df1cca6bf2-SJC

    {
      "name": "a486a871-c610-4a0e-b87e-9b3c030862a1",
      "status": "success",
      "uuid": "a486a871-c610-4a0e-b87e-9b3c030862a1"
    }

If you receive a `201 Created` response code from the server, your zone set creation was successful. You can also log into the application UI and view the zone set there under the Manage Travel Analyses > Manage Zone Sets menu path.

The server assigns your newly created zone set a UUID (universally unique ID) and returns that in the response body. It also assigns a name that is equal to the UUID unless you chose to specify an optional `zone_set_name` in your request body. If you supply the `zone_set_name` in the request, it must be case-insensitive unique and no longer than 50 characters.


# View Available Data Source and Available Date Ranges


The Data API supports looking up the available date ranges for the data sources allowed in your organization. The example below looks up available date ranges.

Create a file called lookup-date-ranges.sh with the following contents and make it executable. Substitute your organization's API key below in the x-stl-key request header.

    #!/bin/bash

    curl -i \
        -H "x-stl-key: SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1" \
        https://insight.streetlightdata.com/api/v2/date_ranges/US/All_Vehicles

Run ./lookup-date-ranges.sh from the command line. You should see results similar to the following:

    $ ./lookup-date-ranges.sh
    HTTP/1.1 200 OK
    Date: Fri, 07 Apr 2017 04:15:37 GMT
    Content-Type: application/json
    Content-Length: 128
    Connection: keep-alive
    Set-Cookie: __cfduid=d7f9ea7c345ce679f5dcdf85a1d668df51491538537; expires=Sat, 07-Apr-18 04:15:37 GMT; path=/; domain=.streetlightdata.com; HttpOnly
    Last-Modified: Fri, 07 Apr 2017 04:20:06 GMT
    Cache-Control: public, max-age=0, no-cache
    Expires: Fri, 07 Apr 2017 04:23:20 GMT
    ETag: "58e71376-235f"
    Accept-Ranges: bytes
    Server: cloudflare-nginx
    CF-RAY: 34ba35fe5a012828-SJC
    {
      "date_ranges": {
        "supports": [
            {
                "start_date": "01/01/2019",
                "end_date": "12/31/2019",
            }
        ],
        "default": [
            {
                "start_date": "03/01/2019",
                "end_date": "04/30/2019",
            },
            {
                "start_date": "09/01/2019",
                "end_date": "10/31/2019",
            }
        ]
      }
    }

You can use the information gathered from above to help you create a analysis with the proper available date ranges.

# Create an O-D Analysis

The Data API supports the following analyses in this release: Origin-Destination, Origin-Destination through Middle Filters, Zone Activity, Trips to or from Pre-set Geography, Segment Analysis, Top Routes between Origin and Destination, Top Routes for Zones, and AADT. The following example creates an Origin-Destination Analysis.

Create a file called create-analysis.json with contents similar to the following. Substitute the zone set UUID you received from the server below in the `oz_sets` (Origin zone sets) and `dz_sets` (Destination zone sets) elements. (They are both one-element arrays containing the same zone set.)

    {
      "insight_login_email":"testemail@streetlightdata.com",
      "analysis_type":"OD_Analysis",
      "travel_mode_type":"Truck",
      "description":"",
      "oz_sets":[{"uuid":"a486a871-c610-4a0e-b87e-9b3c030862a1"}],
      "dz_sets":[{"uuid":"a486a871-c610-4a0e-b87e-9b3c030862a1"}],
      "date_ranges": [{"start_date": "01/01/2016", "end_date": "12/31/2016"}]
      "day_types":"All Days|17,Weekday|14,Weekend Day|67",
      "day_parts":"All Day|0023,Early AM|0005,Peak AM|0609,Mid-Day|1014,Peak PM|1518,Late PM|1923",
      "trip_attributes":false,
      "traveler_attributes":false
    }

The following are some notes on the above example:
- `insight_login_email` is required and the user must have access to the specified organization to create a analysis
- `oz_sets` and `dz_sets` can also be specified by name instead of by UUID. It is possible to refer to zone sets created via the application UI this way.
- `date_ranges` is a list of pairs of start and end dates in MM/DD/YYYY format.
- `day_types` is a comma-separated list of day types in the analysis. Each day type has a name separated by the vertical bar from the start day of week to the end day of week (1 for Monday through 7 for Sunday). Analyses must define All Days as "17" (Monday through Sunday).
- `day_parts` is a comma-separated list of day parts in the analysis. Each day part has a name separated by the vertical bar from the start hour and end hour from 00 (midnight) to 23 (11 PM). For example, 'All Day|0023' ranges from midnight (00:00) to 11:59 PM. Analyses must define All Day as 0023 (midnight to midnight).
- If `trip_attributes` is true, then `trip_duration_bins`, `trip_length_bins`, `trips_speed_bins`, and `trip_circuity_bins` can also be specified. They are comma-separated lists and have the same units and defaults as in the app UI.
- It is optional for an `analysis_name` to be specified in the request body. If specified, it must be case-insensitive unique and must be no more than 50 characters long. The server assigns a UUID-based name if the caller does not supply one.

Create a file called create-analysis.sh with the following contents and make it executable. Substitute your organization's API key below in the x-stl-key request header.

    #!/bin/bash

    curl -i -d @create-analysis.json \
        -H "content-type:application/json" \
        https://insight.streetlightdata.com/api/v2/analyses?key=SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1

Run ./create-analysis.sh from the command line. You should see results similar to the following:

    $ ./create-analysis.sh
    HTTP/1.1 201 CREATED
    Date: Fri, 07 Apr 2017 04:15:37 GMT
    Content-Type: application/json
    Content-Length: 128
    Connection: keep-alive
    Set-Cookie: __cfduid=d7f9ea7c345ce679f5dcdf85a1d668df51491538537; expires=Sat, 07-Apr-18 04:15:37 GMT; path=/; domain=.streetlightdata.com; HttpOnly
    Signature: 08a12cbd0e03edec92da03abb8ad3d0a17507b63
    Cache-Control: no-cache, no-store, must-revalidate
    Pragma: no-cache
    Expires: 0
    Server: cloudflare-nginx
    CF-RAY: 34ba2ab3bdac6e32-SJC

    {
      "name": "1be1edc3-7575-4003-850c-62145f4986cb",
      "status": "success",
      "uuid": "1be1edc3-7575-4003-850c-62145f4986cb"
    }

At this point, in addition to using the following API call to query analysis status, you can also see the analysis and its status by logging into the InSight application UI.


# Query Processing Status of Your Analysis

Create a file called query-analysis-status.json with contents similar to the following. Substitute the Analysis UUID from the previous Create Analysis server response in this request body.

    {
        "analyses":[{"uuid":"1be1edc3-7575-4003-850c-62145f4986cb"}]
    }

Create a file called query-analysis-status.sh with the following contents and make it executable. Substitute your organization's API key.

    #!/bin/bash

    curl -i -d @query-analysis-status.json \
        -H "content-type:application/json" \
        https://insight.streetlightdata.com/api/v2/analyses/status?key=SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1

Run ./query-analysis-status.sh from the command line. At first, you should see results similar to the following:

    $ ./query-analysis-status.sh
    HTTP/1.1 200 OK
    Date: Fri, 07 Apr 2017 04:16:22 GMT
    Content-Type: application/json
    Content-Length: 199
    Connection: keep-alive
    Set-Cookie: __cfduid=d2bfa2766e66a9b14605c3ac3938231641491538582; expires=Sat, 07-Apr-18 04:16:22 GMT; path=/; domain=.streetlightdata.com; HttpOnly
    Signature: 08a12cbd0e03edec92da03abb8ad3d0a17507b63
    Cache-Control: no-cache, no-store, must-revalidate
    Pragma: no-cache
    Expires: 0
    Server: cloudflare-nginx
    CF-RAY: 34ba2bcd1bbe6dde-SJC

    {
      "analyses": [
        {
          "name": "1be1edc3-7575-4003-850c-62145f4986cb",
          "status": "Processing",
          "uuid": "1be1edc3-7575-4003-850c-62145f4986cb"
        }
      ],
      "status": "success"
    }

Eventually, you will see status results showing that the analysis is Available and listing the metrics that it has.

    $ ./query-analysis-status.sh
    HTTP/1.1 200 OK
    Date: Fri, 07 Apr 2017 04:20:40 GMT
    Content-Type: application/json
    Content-Length: 351
    Connection: keep-alive
    Set-Cookie: __cfduid=d1771e701a9bd3300a0e2b8bd7efe9e491491538839; expires=Sat, 07-Apr-18 04:20:39 GMT; path=/; domain=.streetlightdata.com; HttpOnly
    Signature: 08a12cbd0e03edec92da03abb8ad3d0a17507b63
    Cache-Control: no-cache, no-store, must-revalidate
    Pragma: no-cache
    Expires: 0
    Server: cloudflare-nginx
    CF-RAY: 34ba32155e586e2c-SJC

    {
      "analyses": [
        {
          "metrics": [
            "od_pers",
            "od_comm",
            "zone_od_pers",
            "zone_od_comm"
          ],
          "name": "1be1edc3-7575-4003-850c-62145f4986cb",
          "status": "Available",
          "uuid": "1be1edc3-7575-4003-850c-62145f4986cb"
        }
      ],
      "status": "success"
    }


# Get Metrics for Your Analysis

After your analysis becomes available, you can get metrics for it. Create a file called get-od-personal-results.sh with contents similar to the following and make it executable. Substitute the analysis UUID from the previous server responses in the request URL.

    #!/bin/bash

    curl -i \
        -H "x-stl-key: SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1" \
        https://insight.streetlightdata.com/api/v2/analyses/download/uuid/1be1edc3-7575-4003-850c-62145f4986cb/od_pers

Run ./get-od-personal-results.sh from the command line. You should get results that start similar to the server response below (truncated for brevity). Note: you may see different metric values if you are running on a different version than the metric algorithm in this example. Also, this API call is supported only for analyses created via the API, not analyses created via the UI.

    $ ./get-od-personal-results.sh
    HTTP/1.1 200 OK
    Date: Fri, 07 Apr 2017 04:23:20 GMT
    Content-Type: text/csv
    Content-Length: 9055
    Connection: keep-alive
    Set-Cookie: __cfduid=d8b918f95608b9c71fe031233db300df21491539000; expires=Sat, 07-Apr-18 04:23:20 GMT; path=/; domain=.streetlightdata.com; HttpOnly
    Last-Modified: Fri, 07 Apr 2017 04:20:06 GMT
    Cache-Control: public, max-age=0, no-cache
    Expires: Fri, 07 Apr 2017 04:23:20 GMT
    ETag: "58e71376-235f"
    Accept-Ranges: bytes
    Server: cloudflare-nginx
    CF-RAY: 34ba35fe5a012828-SJC

    device_type,origin_zone_id,origin_zone_name,origin_zone_is_pass_through,origin_zone_direction,destination_zone_id,destination_zone_name,destination_zone_is_pass_through,destination_zone_direction,day_type,day_part,o_d_traffic,origin_zone_traffic,destination_zone_traffic,avg_trip_duration
    Personal,1,Mission,no,N/A,1,Mission,no,N/A,0: All Days (M-Su),0: All Day (12am-12am),6635,40580,46777,441
    Personal,1,Mission,no,N/A,1,Mission,no,N/A,0: All Days (M-Su),1: Early AM (12am-6am),116,979,881,402
    Personal,1,Mission,no,N/A,1,Mission,no,N/A,0: All Days (M-Su),2: Peak AM (6am-10am),1017,6954,7933,409
    Personal,1,Mission,no,N/A,1,Mission,no,N/A,0: All Days (M-Su),3: Mid-Day (10am-3pm),2193,12531,14843,446
    Personal,1,Mission,no,N/A,1,Mission,no,N/A,0: All Days (M-Su),4: Peak PM (3pm-7pm),2331,12993,15452,455
    Personal,1,Mission,no,N/A,1,Mission,no,N/A,0: All Days (M-Su),5: Late PM (7pm-12am),977,7122,7668,430
    Personal,1,Mission,no,N/A,1,Mission,no,N/A,1: Weekday (M-Th),0: All Day (12am-12am),6934,42379,48669,435
    Personal,1,Mission,no,N/A,1,Mission,no,N/A,1: Weekday (M-Th),1: Early AM (12am-6am),70,708,696,370
    Personal,1,Mission,no,N/A,1,Mission,no,N/A,1: Weekday (M-Th),2: Peak AM (6am-10am),1240,8758,9756,410
    Personal,1,Mission,no,N/A,1,Mission,no,N/A,1: Weekday (M-Th),3: Mid-Day (10am-3pm),2089,11657,14062,438
    Personal,1,Mission,no,N/A,1,Mission,no,N/A,1: Weekday (M-Th),4: Peak PM (3pm-7pm),2547,14024,16488,450
    Personal,1,Mission,no,N/A,1,Mission,no,N/A,1: Weekday (M-Th),5: Late PM (7pm-12am),987,7233,7666,422

You can run a similar API call to retrieve the other metrics that this analysis supports. The list of available metrics was provided in the response to the *Query Analysis Status* API call. The list can vary by analysis type and analysis options. In this example, it is the following:
- `od_pers`
- `od_comm`
- `zone_od_pers`
- `zone_od_comm`


Copyright &copy; 2021, StreetLight Data, Inc. All rights reserved.
