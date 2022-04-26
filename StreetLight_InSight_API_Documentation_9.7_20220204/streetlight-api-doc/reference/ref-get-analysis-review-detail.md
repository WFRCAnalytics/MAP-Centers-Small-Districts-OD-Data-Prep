# API Reference: Query Analysis Review Detail

## Description

This query fetches the review details of an Analyses that are in coverage review.

## HTTP request method and URL

    GET https://insight.streetlightdata.com/api/v2/analyses/<analysis_uuid>/review_detail

## Authentication

You must provide your API key in each request to identify your organization to StreetLight's servers. Provide your API key using a query parameter named `key`. The query parameter is the part of the request URL after the question mark. Alternatively, you can pass the key using the HTTP header `x-stl-key`. The server returns a `401 Unauthorized` status code if authentication fails.

Contact your StreetLight Data representative to obtain an API key.

## HTTP request headers

    Content-Type: application/json

### `analysis_uuid` request query parameter (required, string)

The `analysis_uuid` request parameter specifies the UUID of the Analysis in coverage review to query.

## Example request

This example request and response was generated using the `curl` command-line utility. See the [Data API Quick Start](../quickstart) for instructions to rerun this example against the live server.

    GET /api/v2/analyses/1be1edc3-7575-4003-850c-62145f4986cb/review_detail?key=SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1 HTTP/1.1

## HTTP status codes

Returns `200 OK` on success. Returns `400 Bad Request` with an error message in the response body on input error.

## HTTP response body

The HTTP response body is in JSON format. It contains an `zone_set_review_details` object with details on problematic Zone Sets, as well as `org_name`, `analysis_name`, and `analysis_uuid`.

### Response-body example

The following response body gives processing status for a single analysis whose UUID and name are identical:

    {
      "org_name": "My Organization",
      "analysis_name": "My House ZA",
      "analysis_uuid": "a486a871-c610-4a0e-b87e-9b3c030862a1",
      "zone_set_review_detail": [
        {
          "set_uuid": "a486a871-c610-4a0e-b87e-9b3c030862a1",
          "set_name": "SF Area",
          "set_role": "origin",
          "zones": [
            {
              "area": 137.0,
              "direction": "",
              "is_bidi": false,
              "is_pass": false,
              "zone_id": 7575258,
              "zone_name": "123 Fake Street"
            }
          ]
        }
      ]
    }

### `zone_set_review_details` response-body property

The `zone_set_review_details` response-body property is an array of Zone Set objects. Each zone_set_review_details objects has the following properties:

- `zones`: an array of Zone objects. Each Zone objects contains metadata describing the Zone.
- `set_role`: The function of the Zone Set in the Analysis, `origin`, `destination`, or `middle_filter`
- `set_name`: Name of the Zone Set.
- `set_uuid`: UUID (universally unique ID) for the Zone Set, assigned by the server at the time of Zone Set creation

### `status` response-body property

Will always be `success` when the request is successful.

## Example response

    HTTP/1.1 200 OK
    Date: Mon, 10 Apr 2017 17:35:30 GMT
    Content-Type: application/json
    Content-Length: 351
    Connection: keep-alive
    Set-Cookie: __cfduid=ddb78e21d5641dfae48b8d0f7fa8718311491845730; expires=Tue, 10-Apr-18 17:35:30 GMT; path=/; domain=.streetlightdata.com; HttpOnly
    Signature: 08a12cbd0e03edec92da03abb8ad3d0a17507b63
    Cache-Control: no-cache, no-store, must-revalidate
    Pragma: no-cache
    Expires: 0
    Server: cloudflare-nginx
    CF-RAY: 34d77684c9196e2c-SJC

    {
      "org_name": "My Organization",
      "analysis_name": "My House ZA",
      "analysis_uuid": "a486a871-c610-4a0e-b87e-9b3c030862a1",
      "zone_set_review_detail": [
        {
          "set_uuid": "a486a871-c610-4a0e-b87e-9b3c030862a1",
          "set_name": "SF Area",
          "set_role": "origin",
          "zones": [
            {
              "area": 137.0,
              "direction": "",
              "is_bidi": false,
              "is_pass": false,
              "zone_id": 7575258,
              "zone_name": "123 Fake Street"
            }
          ]
        }
      ],
      "status": "success"
    }

Copyright &copy; 2021, StreetLight Data, Inc. All rights reserved.
