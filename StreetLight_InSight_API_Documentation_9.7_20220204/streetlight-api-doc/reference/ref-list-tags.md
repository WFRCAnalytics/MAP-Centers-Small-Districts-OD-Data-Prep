# API Reference: List Tags within an Organization

## Description

Retrieve a list of Tags that are available in user's Organization.

## HTTP request method and URL

    GET https://insight.streetlightdata.com/api/v2/tags

## Authentication

You must provide your API key in each request to identify your organization to StreetLight's servers. Provide your API key using a query parameter named `key`. The query parameter is the part of the request URL after the question mark. Alternatively, you can pass the key using the HTTP header `x-stl-key`. The server returns a `401 Unauthorized` status code if authentication fails.

Contact your StreetLight Data representative to obtain an API key.

## HTTP status codes

Returns `200 OK` on success. Can return other status codes on error.

## HTTP response body

The HTTP response body is in json format. It includes the request `status` and an array of Tag objects `tags` available in an Organization.

### Response-body example

    {
      "status": "success",
      "tags": [{
        "tag_name":"San Francisco",
        "analysis_num": 2,
        "created_by": "user1@sample_company.com",
        "created_date": "2020-05-20T05:11:40.962576+00:00",
      }]
    }

### `status` response-body property

Will always be `success` when the request is successful.

### `tags` response-body property

The `tags` property contains an array of Tag objects that are currently available in an Organization. It includes the following information:
- `tag_name`: name of the tag
- `created_by`: creator of the tag
- `created_date`: created date of the tag
- `analysis_num`: number of analysis tagged by this tag

## Example request

This example request and response was generated using the `curl` command-line utility. See the [Data API Quick Start](../quickstart) for instructions to rerun this example against the live server.

    GET /api/v2/tags?key=SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1 HTTP/1.1

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
      "status": "success",
      "tags": [{
        "tag_name":"San Francisco",
        "analysis_num": 2,
        "created_by": "user1@sample_company.com",
        "created_date": "2020-05-20T05:11:40.962576+00:00",
      }]
    }


Copyright &copy; 2021, StreetLight Data, Inc. All rights reserved.
