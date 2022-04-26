# API Reference: Query Analysis Status

## Description

This query provides the status when processing an array of analyses. Analyses process asynchronously after the server creates them. When their status becomes `Available`, their metrics can be downloaded in a subsequent *Get Metrics* call.

Note: If status needs to be queried for a large number of analyses, please use the array input of this endpoint to do so with fewer server calls to reduce resource consumption. StreetLight reserves the right to rate-limit this endpoint or bill additionally per API call if request volume is high.

## HTTP request method and URL

    POST https://insight.streetlightdata.com/api/v2/analyses/status

## Limitations

There is currently a rate limit of 1 call per second.

## Authentication

You must provide your API key in each request to identify your organization to StreetLight's servers. Provide your API key using a query parameter named `key`. The query parameter is the part of the request URL after the question mark. Alternatively, you can pass the key using the HTTP header `x-stl-key`. The server returns a `401 Unauthorized` status code if authentication fails.

Contact your StreetLight Data representative to obtain an API key.

## HTTP request headers

    Content-Type: application/json

## HTTP request body

The HTTP request body must be in JSON format. It has one required property, `analyses`.

### Request-body example

    {
        "analyses":[{"uuid":"1be1edc3-7575-4003-850c-62145f4986cb"}]
    }

### `analyses` request-body property (required, array of Analysis objects)

The `analyses` request-body property identifies an array of analyses for which to query processing status.

This property is required and must be an array of analysis objects. An analysis object identifies an analysis by either name or UUID (universally unique ID) and must have one of the following two forms:

    {"name": "some name"}

or

    {"uuid": "server assigned UUID"}

## HTTP status codes

Returns `200 OK` on success. Returns `400 Bad Request` with an error message in the response body on input error.

## HTTP response body

The HTTP response body is in JSON format. It contains an `analyses` property with an array value that gives the processing status of each analysis listed in the request body. Analyses that are in `Available` status also include a list of their metrics that can be downloaded in subsequent *Get Metrics* calls.

### Response-body example

The following response body gives processing status for a single analysis whose UUID and name are identical:

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

The above analysis has status `Available` and supports *Get Metrics* requests for the following four metrics:
- `od_pers`
- `od_comm`
- `zone_od_pers`
- `zone_od_comm`

### `analyses` response-body property

The `analyses` response-body property is an array of analysis-status objects. Each analysis-status objects has the following properties:
- `metrics`: an array of metrics that can be downloaded for this Aaalysis (included only if the status of the analysis is `Available`)
- `name`: name of the analysis
- `status`: processing status of the analysis
- `uuid`: UUID (universally unique ID) for the analysis, assigned by the server at the time of analysis creation

### `status` response-body property

Will always be `success` when the request is successful.

## Example request

This example request and response was generated using the `curl` command-line utility. See the [Data API Quick Start](../quickstart) for instructions to rerun this example against the live server.

    POST /api/v2/analyses/status?key=SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1 HTTP/1.1
    User-Agent: curl/7.35.0
    Host: insight.streetlightdata.com
    Accept: */*
    content-type:application/json
    Content-Length: 66

    {
        "analyses":[{"uuid":"1be1edc3-7575-4003-850c-62145f4986cb"}]
    }

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


Copyright &copy; 2021, StreetLight Data, Inc. All rights reserved.
