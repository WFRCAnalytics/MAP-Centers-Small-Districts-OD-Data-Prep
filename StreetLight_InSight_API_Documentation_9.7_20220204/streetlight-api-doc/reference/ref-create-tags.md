# API Reference: Create a Tag

## Description

Tags are an organizational tool for Analyses. One or more Tags can be to an Analysis. Analyses can be filtered by assigned Tags.

## HTTP request method and URL

    POST https://insight.streetlightdata.com/api/v2/analyses/tags

## Authentication

You must provide your API key in each request to identify your organization to StreetLight's servers. Provide your API key using a query parameter named `key`. The query parameter is the part of the request URL after the question mark. Alternatively, you can pass the key using the HTTP header `x-stl-key`. The server returns a `401 Unauthorized` status code if authentication fails.

Contact your StreetLight Data representative to obtain an API key.

## HTTP request headers

    Content-Type: application/json

## HTTP request body

The HTTP request body must be in JSON format. It has a required property `tag_name`.

### Request-body example

    {
        "insight_login_email":"testemail@streetlightdata.com",
        "tag_name": "San Francisco"
    }

### `insight_login_email` request-body property(required, string)

The `insight_login_email` request-body property is a required login email associated with the specific organization to check for user access.

### `tag_name` request-body property (required, string)

The `tag_name` request-body property is a required string that contains the user defined descriptor associated with this Tag. The `tag_name` value should be unique within an Organization.

## HTTP status codes

Returns `201 Created` on success. Returns `400 Bad Request` with an error message in the response body on input error.

## HTTP response body

The HTTP response body is in JSON format. It includes the request `status` and `tag_name` of the newly created Tag.

### Response-body example

    {
      "status": "success",
      "tag_name": "San Francisco",
    }

### `status` response-body property

Will always be `success` when the request is successful.

### `tag_name` response-body property

The `tag_name` property of the created Tag.

## Example request

This example request and response was generated using the `curl` command-line utility. See the [Data API Quick Start](../quickstart) for instructions to rerun this example against the live server.

    POST /api/v2/analyses/tags?key=SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1 HTTP/1.1
    User-Agent: curl/7.35.0
    Host: insight.streetlightdata.com
    Accept: */*
    content-type:application/json
    Content-Length: 92

    {
        "insight_login_email":"testemail@streetlightdata.com",
        "tag_name": "San Francisco"
    }

## Example response

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
      "tag_name": "San Francisco",
      "status": "success"
    }


Copyright &copy; 2021, StreetLight Data, Inc. All rights reserved.

