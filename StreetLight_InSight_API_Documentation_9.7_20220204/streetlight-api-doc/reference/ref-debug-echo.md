# API Reference: Echo a Message for Debugging

## Description

Echo back a message. This endpoint is provided solely for debugging connectivity and authentication to the API server. It is not necessary to use it in production to create analyses and get metrics.

## HTTP request method and URL

    POST https://insight.streetlightdata.com/api/v2/debug/echo

## Authentication

You must provide your API key in each request to identify your organization to StreetLight's servers. Provide your API key using a query parameter named `key`. The query parameter is the part of the request URL after the question mark. Alternatively, you can pass the key using the HTTP header `x-stl-key`. The server returns a `401 Unauthorized` status code if authentication fails.

Contact your StreetLight Data representative to obtain an API key.

## HTTP request headers

    Content-Type: application/json

## HTTP request body

The HTTP request body must be in JSON format. It has one required property, `message`.

### Request-body example

    {"message": "hello world"}

## HTTP status codes

Returns `200 OK` if successful. It can return other status codes on error, including `401 Unauthorized` if the API key was not authenticated successfully or `403 Forbidden` if the API key was authenticated but the organization is not allowed to use the server.

## HTTP response body

The HTTP response body is in JSON format. It echoes back the input message.

### Response-body example

    {
      "message": "hello world",
      "status": "success"
    }

### `message` response-body property

Contains the same value as the `message` request-body property did.

### `status` response-body property

Will always be `success` when the request is successful.

## Example request

This example request and response was generated using the `curl` command-line utility. See the [Data API Quick Start](../quickstart) for instructions to rerun this example against the live server.

    POST /api/v2/debug/echo?key=SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1 HTTP/1.1
    User-Agent: curl/7.35.0
    Host: insight.streetlightdata.com
    Accept: */*
    content-type: application/json
    Content-Length: 26

    {"message": "hello world"}

## Example response

    HTTP/1.1 200 OK
    Date: Mon, 10 Apr 2017 16:57:19 GMT
    Content-Type: application/json
    Content-Length: 55
    Connection: keep-alive
    Set-Cookie: __cfduid=dac4cf29a49dccfe77466b211a67d2ae71491843439; expires=Tue, 10-Apr-18 16:57:19 GMT; path=/; domain=.streetlightdata.com; HttpOnly
    Signature: 08a12cbd0e03edec92da03abb8ad3d0a17507b63
    Cache-Control: no-cache, no-store, must-revalidate
    Pragma: no-cache
    Expires: 0
    Server: cloudflare-nginx
    CF-RAY: 34d73e96aaa76e32-SJC

    {
      "message": "hello world",
      "status": "success"
    }

Copyright &copy; 2021, StreetLight Data, Inc. All rights reserved.
