# API Reference: Tag an Analysis

## Description

Assign a Tag to one or more Analyses.

## HTTP request method and URL

    POST https://insight.streetlightdata.com/api/v2/tags/tag_analyses

## Authentication

You must provide your API key in each request to identify your organization to StreetLight's servers. Provide your API key using a query parameter named `key`. The query parameter is the part of the request URL after the question mark. Alternatively, you can pass the key using the HTTP header `x-stl-key`. The server returns a `401 Unauthorized` status code if authentication fails.

Contact your StreetLight Data representative to obtain an API key.

## HTTP request headers

    Content-Type: application/json

## HTTP request body

The HTTP request body must be in JSON format. It has a required propertits `tag_name` and `analyses`.

### Request-body example

    {
        "insight_login_email":"testemail@streetlightdata.com",
        "tags": ["San Francisco"],
        "analyses":[{"uuid":"1be1edc3-7575-4003-850c-62145f4986cb"}]
    }

### `insight_login_email` request-body property(required, string)

The `insight_login_email` request-body property is a required login email associated with the specific organization to check for user access.

### `tags` request-body property (required, array of Tag names)

The `tags` request-body property is array of Tag name that refers to Tags created within the user's Organization.

### `analyses` request-body property (required, array of Analysis objects)

The `analyses` request-body property identifies an array of analyses for which assign the specicified `tag_name`.

This property is required and must be an array of analysis objects. An analysis object identifies an analysis by either name or UUID (universally unique ID) and must have one of the following two forms:

    {"name": "some name"}

or

    {"uuid": "server assigned UUID"}

## HTTP status codes

Returns `200 OK` on success. Returns `400 Bad Request` with an error message in the response body on input error.

## HTTP response body

The HTTP response body is in JSON format. It includes the request `status`.

### Response-body example

    {
      "status": "success"
    }

### `status` response-body property

Will always be `success` when the request is successful.

## Example request

This example request and response was generated using the `curl` command-line utility. See the [Data API Quick Start](../quickstart) for instructions to rerun this example against the live server.

    POST /api/v2/analyses/tags/tag_analyses?key=SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1 HTTP/1.1
    User-Agent: curl/7.35.0
    Host: insight.streetlightdata.com
    Accept: */*
    content-type:application/json
    Content-Length: 92

    {
        "insight_login_email":"testemail@streetlightdata.com",
        "tags": ["San Francisco"],
        "analyses":[{"uuid":"1be1edc3-7575-4003-850c-62145f4986cb"}]
    }

## Example response

    HTTP/1.1 200 OK
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
      "status": "success"
    }


Copyright &copy; 2021, StreetLight Data, Inc. All rights reserved.

