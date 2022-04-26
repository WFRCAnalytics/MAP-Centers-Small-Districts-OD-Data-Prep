# API Reference: Lookup Date Ranges Available to an Organization

## Description

Look up the date ranges that can be used in the current organization to create an analysis.

## HTTP request method and URL

    GET https://insight.streetlightdata.com/api/v2/date_ranges/<country>/<travel_mode_type>

## Authentication

You must provide your API key in each request to identify your organization to StreetLight's servers. Provide your API key using a query parameter named `key`. The query parameter is the part of the request URL after the question mark. Alternatively, you can pass the key using the HTTP header `x-stl-key`. The server returns a `401 Unauthorized` status code if authentication fails.

Contact your StreetLight Data representative to obtain an API key.

## HTTP status codes

Returns `200 OK` on success. Can return other status codes on error.

## HTTP response body

The HTTP response body is in json format. It echoes the available date ranges and the defaults.

When creating an analysis, note that the mode of travel selected must be available for each date range in the analysis. For example, if running an analysis for All_Vehicles between January 2019 - March 2019, check that the `supports` field contains the Jan, Feb and March before creating the analysis.

## Example request

This example request and response was generated using the `curl` command-line utility. See the [Data API Quick Start](../quickstart) for instructions to rerun this example against the live server.

    GET /api/v2/date_ranges/US/All_Vehicles?key=SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1 HTTP/1.1

## Example response

    HTTP/1.1 200 OK
    Date: Mon, 10 Apr 2017 18:02:53 GMT
    Content-Type: application/json
    Content-Length: 128
    Connection: keep-alive
    Set-Cookie: __cfduid=d496fa281a93825a191898d095bf65f3f1491847373; expires=Tue, 10-Apr-18 18:02:53 GMT; path=/; domain=.streetlightdata.com; HttpOnly
    Last-Modified: Fri, 07 Apr 2017 04:20:06 GMT
    Cache-Control: public, max-age=0, no-cache
    Expires: Mon, 10 Apr 2017 18:02:53 GMT
    ETag: "58e71376-235f"
    Accept-Ranges: bytes
    Server: cloudflare-nginx
    CF-RAY: 34d79ea33c17515e-SJC
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

## `country` request query parameter (required, string)

The `country` parameter is a required string and must be one of the following values:
- `US`
- `CA`

## `travel_mode_type` request query parameter (required, string)

The `travel_mode_type` parameter is a required string and must be one of the following values:
- `All_Vehicles`
- `Truck`
- `Bicycle`
- `Pedestrian`
- `Bus`
- `Rail`


Copyright &copy; 2021, StreetLight Data, Inc. All rights reserved.
