# API Reference: Get Metrics for an Available Analysis by UUID

## Description

This call returns metric result for an analysis by analysis UUID. The Analysis must have been created by a previous Create Analysis request, and its processing status must be available. Each metric for an analysis must be retrieved in a separate API call.

The *Query Analysis Status* API call returns the list of metrics that can be retrieved for each available analysis using this endpoint. The list of metrics varies by analysis type and analysis options.

## HTTP request method and URL

    GET https://insight.streetlightdata.com/api/v2/analyses/download/uuid/{uuid}/{metric}

## Authentication

You must provide your API key in each request to identify your organization to StreetLight's servers. Provide your API key using a query parameter named `key`. The query parameter is the part of the request URL after the question mark. Alternatively, you can pass the key using the HTTP header `x-stl-key`. The server returns a `401 Unauthorized` status code if authentication fails.

Contact your StreetLight Data representative to obtain an API key.

## HTTP status codes

Returns `200 OK` on success. Can return other status codes on error.

## HTTP response body

The HTTP response body is in CSV format.

## Example request

This example request and response was generated using the `curl` command-line utility. See the [Data API Quick Start](../quickstart) for instructions to rerun this example against the live server.

    GET /api/v2/analyses/download/uuid/1be1edc3-7575-4003-850c-62145f4986cb/za_pers?key=SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1 HTTP/1.1

## Example response

Note: response-body content is truncated for brevity.

    HTTP/1.1 200 OK
    Date: Mon, 10 Apr 2017 18:02:53 GMT
    Content-Type: text/csv
    Content-Length: 9055
    Connection: keep-alive
    Set-Cookie: __cfduid=d496fa281a93825a191898d095bf65f3f1491847373; expires=Tue, 10-Apr-18 18:02:53 GMT; path=/; domain=.streetlightdata.com; HttpOnly
    Last-Modified: Fri, 07 Apr 2017 04:20:06 GMT
    Cache-Control: public, max-age=0, no-cache
    Expires: Mon, 10 Apr 2017 18:02:53 GMT
    ETag: "58e71376-235f"
    Accept-Ranges: bytes
    Server: cloudflare-nginx
    CF-RAY: 34d79ea33c17515e-SJC

    Mode of Travel,Intersection Type,Zone ID,Zone Name,Zone Is Pass-Through,Zone Direction (degrees),Zone is Bi-Direction,Day Type,Day Part,Average Daily Zone Traffic (StL Index),Avg Travel Time (sec),Avg All Travel Time (sec),Avg Trip Length (mi),Avg All Trip Length (mi)
    All Vehicles - StL All Vehicles Index,Trip Start,14000012,zone 14000012,yes,180,no,0: All Days (M-Su),0: All Day (12am-12am),93,22,37,78.1,33.8
    All Vehicles - StL All Vehicles Index,Trip Start,14000012,zone 14000012,yes,180,no,0: All Days (M-Su),1: Early AM (12am-6am),13,49,62,68.6,16.2
    All Vehicles - StL All Vehicles Index,Trip Start,14000012,zone 14000012,yes,180,no,0: All Days (M-Su),2: Peak AM (6am-10am),55,30,11,97.7,54.9
    All Vehicles - StL All Vehicles Index,Trip Start,14000012,zone 14000012,yes,180,no,0: All Days (M-Su),3: Mid-Day (10am-3pm),16,23,70,92.5,73.0
    All Vehicles - StL All Vehicles Index,Trip Start,14000012,zone 14000012,yes,180,no,0: All Days (M-Su),4: Peak PM (3pm-7pm),42,63,75,38.0,11.7
    All Vehicles - StL All Vehicles Index,Trip Start,14000012,zone 14000012,yes,180,no,0: All Days (M-Su),5: Late PM (7pm-12am),75,57,44,55.9,74.5
    All Vehicles - StL All Vehicles Index,Trip Start,14000012,zone 14000012,yes,180,no,1: Weekday (M-Th),0: All Day (12am-12am),84,25,94,34.3,73.0
    All Vehicles - StL All Vehicles Index,Trip Start,14000012,zone 14000012,yes,180,no,1: Weekday (M-Th),1: Early AM (12am-6am),45,72,82,95.4,52.6
    All Vehicles - StL All Vehicles Index,Trip Start,14000012,zone 14000012,yes,180,no,1: Weekday (M-Th),2: Peak AM (6am-10am),17,20,87,19.5,81.6
    All Vehicles - StL All Vehicles Index,Trip Start,14000013,zone 14000013,yes,180,no,1: Weekday (M-Th),3: Mid-Day (10am-3pm),18,35,31,29.6,93.1
    All Vehicles - StL All Vehicles Index,Trip Start,14000013,zone 14000013,yes,180,no,1: Weekday (M-Th),4: Peak PM (3pm-7pm),14,75,61,96.0,51.7
    All Vehicles - StL All Vehicles Index,Trip Start,14000013,zone 14000013,yes,180,no,1: Weekday (M-Th),5: Late PM (7pm-12am),29,68,81,27.5,76.9


Copyright &copy; 2021, StreetLight Data, Inc. All rights reserved.
