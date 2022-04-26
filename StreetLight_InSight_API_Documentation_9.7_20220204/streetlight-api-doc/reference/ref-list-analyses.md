# API Reference: List and Search Analyses

## Description

Retrieve a list of Analyses by the specified search criteria.

## HTTP request method and URL

    GET https://insight.streetlightdata.com/api/v2/analyses/search


## Authentication

You must provide your API key in each request to identify your organization to StreetLight"s servers. Provide your API key using a query parameter named `key`. The query parameter is the part of the request URL after the question mark. Alternatively, you can pass the key using the HTTP header `x-stl-key`. The server returns a `401 Unauthorized` status code if authentication fails.

Contact your StreetLight Data representative to obtain an API key.

### `created_date_from` request parameter (optional, string)

The `created_date_from` request parameter is a string representing date with format `MM/DD/YYYY`. If present, the `analyses` list will be filtered to include Analyses that were created after the specified date inclusively.

    /api/v2/analyses/search?created_date_from="01/01/2021"

### `created_date_to` request parameter (optional, string)

The `created_date_to` request parameter is a string representing date with format `MM/DD/YYYY`. If present, the `analyses` list will be filtered to include Analyses that were created before the specified date inclusively.

    /api/v2/analyses/search?created_date_to="01/01/2021"

### `name_contains` request parameter (optional, string)

The `name_contains` request parameter is a string that is supposed to be included in the analysis name. If present, the `analyses` list will be filtered to include Analyses that"s names contain a string specified in this parameter. The search is case insensitive and the order of words in the specified string does not matter, ie. "Test Segment Analysis" allow for matching "Segment Analysis Test".

    /api/v2/analyses/search?name_contains="Test Segment Analysis"

### `analysis_type` request parameter (optional, string)

The `analysis_type` request parameter is a string representing analysis type. If present, the `analyses` list will be filtered to include Analyses of a certain type.
The `analysis_type` request-body parameter must be a string with one of the following values:

- `OD_Analysis`
- `OD_MF_Analysis`
- `Zone_Activity_Analysis`
- `OD_Preset_Geography`
- `Segment_Analysis`
- `AADT`
- `Top_Routes_OD`
- `Top_Routes_ZA`


    /api/v2/analyses/search?analysis_type="OD_Analysis"

### `travel_mode_type` request parameter (optional, string)

The `travel_mode_type` request parameter is a string representing analysis travel mode type. If present, the `analyses` list will be filtered to include Analyses of a certain travel mode type.
The `travel_mode_type` request-body parameter must be a string with one of the following values:

- `All_Vehicles`
- `Truck`
- `Bicycle`
- `Pedestrian`
- `Bus`
- `Rail`


    /api/v2/analyses/search?travel_mode_type="All_Vehicles"

## HTTP status codes

Returns `200 OK` on success. Can return other status codes on error.

## HTTP response body

The HTTP response body is in JSON format. It includes the request `status` and an array of Analysis objects.

### Response-body example

    {
        "status": "success"
        "analyses": 
        [
            {
                "analysis_name": "project 2",
                "analysis_type": "OD_MF",
                "analysis_uuid": "71721353-abb0-4463-98d7-50b4265fcdb5",
                "created_by_uuid": 801,
                "created_date": "07/13/2021",
                "data_period": [{"month_num": 8, "year_num": 2014},
                                {"month_num": 1, "year_num": 2015},
                                {"month_num": 3, "year_num": 2015}],
                "number_of_zones": 0,
                "travel_mode": "Truck"
            },
            {
                "analysis_name": "project 1",
                "analysis_type": "OD_MF",
                "analysis_uuid": "50345d18-66cd-4352-bbb7-09e272234cdb",
                "created_by_uuid": 801,
                "created_date": "07/13/2021",
                "data_period": [{"month_num": 8, "year_num": 2014},
                                {"month_num": 1, "year_num": 2015},
                                {"month_num": 3, "year_num": 2015}],
                "number_of_zones": 0,
                "travel_mode": "Truck"
            }
        ],
    }

### `status` response-body property

Will always be `success` when the request is successful.

### `analyses` response-body property

The `analyses` property contains an array of Analysis objects that are currently available in an Organization.

## Example request

This example request and response was generated using the `curl` command-line utility. See the [Data API Quick Start](../quickstart) for instructions to rerun this example against the live server.

    GET /api/v2/analyses/search?created_date_from="01/01/2021"&created_date_to="03/01/2021"&travel_mode_type="Pedestrian" HTTP/1.1

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
        "status": "success"
        "analyses": 
        [
            {
                "analysis_name": "project 2",
                "analysis_type": "OD_MF",
                "analysis_uuid": "71721353-abb0-4463-98d7-50b4265fcdb5",
                "created_by_uuid": 801,
                "created_date": "07/13/2021",
                "data_period": [{"month_num": 8, "year_num": 2014},
                                {"month_num": 1, "year_num": 2015},
                                {"month_num": 3, "year_num": 2015}],
                "number_of_zones": 0,
                "travel_mode": "Truck"
            },
            {
                "analysis_name": "project 1",
                "analysis_type": "OD_MF",
                "analysis_uuid": "50345d18-66cd-4352-bbb7-09e272234cdb",
                "created_by_uuid": 801,
                "created_date": "07/13/2021",
                "data_period": [{"month_num": 8, "year_num": 2014},
                                {"month_num": 1, "year_num": 2015},
                                {"month_num": 3, "year_num": 2015}],
                "number_of_zones": 0,
                "travel_mode": "Truck"
            }
        ],
    }


Copyright &copy; 2021, StreetLight Data, Inc. All rights reserved.
