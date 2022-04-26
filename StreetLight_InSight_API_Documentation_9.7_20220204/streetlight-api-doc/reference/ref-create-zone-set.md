# API Reference: Create a Zone Set

## Description

Create a zone set. Zone sets are analyzed by analyses. They specify a set of Zones as GeoJSON feature collections of either MultiPolygons or LineStrings.

## HTTP request method and URL

    POST https://insight.streetlightdata.com/api/v2/zone_sets

## Authentication

You must provide your API key in each request to identify your organization to StreetLight's servers. Provide your API key using a query parameter named `key`. The query parameter is the part of the request URL after the question mark. Alternatively, you can pass the key using the HTTP header `x-stl-key`. The server returns a `401 Unauthorized` status code if authentication fails.

Contact your StreetLight Data representative to obtain an API key.

## HTTP request headers

    Content-Type: application/json

## HTTP request body

The HTTP request body must be in JSON format. It has a required property `zones` and optional properties `zone_set_name`, `geom_type`, and `with_calibration`.

### Request-body example

The following example creates a polygon zone set with two Zones. One zone has the ID 1 and is named "Mission", and it is not a pass-through zone. The second zone has the ID 2 and is named "Financial District", and it is a pass-through zone.

    {
    "insight_login_email":"testemail@streetlightdata.com",
    "geom_type":"polygon",
    "zones": {
    "type": "FeatureCollection",
    "features": [
    { "type": "Feature", "properties": { "id": 1, "name": "Mission", "is_pass": 0, "direction": null }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -122.426698258661972, 37.769562689936315 ], [ -122.423394859041892, 37.772083876030344 ], [ -122.42225575572462, 37.770418101996292 ], [ -122.411206453547067, 37.769427623969634 ], [ -122.406991771273155, 37.769067446852375 ], [ -122.404656609472752, 37.767716767038294 ], [ -122.405169205965521, 37.762628984940662 ], [ -122.406593085112107, 37.760557752167074 ], [ -122.405795712790038, 37.758441432691242 ], [ -122.403232730326167, 37.75722564731312 ], [ -122.402549268335804, 37.751821915004783 ], [ -122.403346640657901, 37.749390106706535 ], [ -122.407561322931784, 37.748399347080543 ], [ -122.424875693354338, 37.74781389197571 ], [ -122.426698258661972, 37.769562689936315 ] ] ] ] } },
    { "type": "Feature", "properties": { "id": 2, "name": "Financial District", "is_pass": 1, "direction": null }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -122.405425504211919, 37.798033588378779 ], [ -122.398476973976571, 37.798933675051543 ], [ -122.396654408668923, 37.799698740100226 ], [ -122.397024617247041, 37.79929370664977 ], [ -122.396768319000643, 37.798911173018389 ], [ -122.395828558763895, 37.797898574431919 ], [ -122.393607307295227, 37.799113691070012 ], [ -122.392610591892605, 37.797876072083447 ], [ -122.394233814119715, 37.79690846455324 ], [ -122.393037755636598, 37.795670808599994 ], [ -122.3913575782436, 37.796278387822021 ], [ -122.390987369665496, 37.795693311702443 ], [ -122.392439726395011, 37.794500642185817 ], [ -122.389278714689581, 37.791462623416393 ], [ -122.401182344355107, 37.781965196242638 ], [ -122.405824190372982, 37.785701296639232 ], [ -122.406222876534017, 37.785723802695827 ], [ -122.407134159187834, 37.790337399578668 ], [ -122.404058580231194, 37.790764986655553 ], [ -122.405425504211919, 37.798033588378779 ] ] ] ] } }
    ]
    }}

The following example creates a line zone set including one zone. The zone has the ID 10 and is named "Market Street", it is a pass-through zone with direction 46.0. The road type and gate details (gate latitude, gate longitude and gate size) are also specified.

```
{
"insight_login_email":"testemail@streetlightdata.com",
"geom_type":"line",
"zones": {
"type": "FeatureCollection",
"features": [
{ "type": "Feature", "properties": { "id": 10, "name": "Market Street", "is_pass": 1, "direction": 46.0, "gate_lat": 34.40, "gate_lng": 34.40, "gate_size": 50 }, "geometry": { "type": "LineString", "coordinates": [ [ -118.485925533,34.0397217471],[-118.484005071,34.0412686707] ] } }
]
}}
```

### `insight_login_email` request-body property(required, string)

The `insight_login_email` request-body property is a required login email associated with the specific organization to check for user access.

### `zones` request-body property (required, GeoJSON feature collection object)

The `zones` request-body property must be a GeoJSON feature collection where the features are either all MultiPolygons or all LineStrings. Refer to the GeoJSON spec at [http://geojson.org/](http://geojson.org/) for details on the GeoJSON format.

Each feature in the GeoJSON feature collection must have the following five properties (optional properties can be omitted):

- `name` (required): Zone Name is required, and will be used to reference that zone in the metric results. It must be case-insensitive unique within the zone set and must be no longer than 50 characters.
- `id` (optional): Zone ID as non-null can be optional. If non-null, it must be an integer greater than zero, and it will be used in addition to the Zone Name to reference that zone in the metric results. It must be unique within the zone set.
- `is_pass` (optional): null, 0, or 1. `is_pass` is always set to 1 for Line Zones. If 1, the zone will be analyzed in terms of traffic that passes through the Zone. Otherwise, depending on analysis type, the zone will be analyzed in terms of traffic that starts or stops in the zone.
- `direction` (optional): integer from 0 to 359. This can be non-null only for pass-through zones. If specified, traffic passing through the zone is included in analyses only if it is traveling in that direction.
- `is_bidi` (optional): null, 0, or 1. Default value is 0. If `is_bidi` is set, `direction` is defined and `is_pass` is set, then traffic going to and from the specified `direction` will be captured in the zone's metric values.

Features with `LineString` geometry can define the following optional properties:

- `road_type` (optional): Primary, Secondary, Local, or Ramp. Road type describe the type of the road segment.
- `gate_lat` (optional): float number from -90 to 90. Latitude of line segemnt custom gate.
- `gate_lng` (optional): float number from -180 to 180. Longitude of line segment custom gate.
- `gate_size` (optional): integer. Size of line segment custom gate.

Features may also contain properties to specify Zone Calibration settings. If `with_calibration` is set to `true` in the Zone Set parameters, the following parameters can be added to a pass-through (`is_pass` enabled) Zone's feature properties in order to specify Zone Calibration settings:

- `calibration_type` (optional): String with value `ADT`, `AADT`, `AWDT`, or `AADWT`. Specify the type of calibration for this Zone.
- `calibration_value` (optional): Integer with a value between 0 and 1,000,000. Required if `calibration_type` is set. Specifies the traffic at the Zone based on the `calibration_type`.
- `personal_traffic_ratio` (optional): Float number between 0.000 and 1.000. The recommended value is 0.96. Required if `calibration_type` is set. Specifies the ratio of traffic for this Zone that is due to personal vehicles.
- `medium_commercial_ratio` (optional): Float number between 0.000 and 1.000. The recommended value is 0.02. Required if `calibration_type` is set. Specifies the ratio of traffic for this Zone that due is to medium-duty vehicles.
- `heavy_commercial_ratio` (optional): Float number between 0.000 and 1.000. The recommended value is 0.02. Required if `calibration_type` is set. Specifies the ratio of traffic for this Zone that due is to heavy-duty vehicles.

Note that if specified, the sum of `personal_traffic_ratio`, `medium_commercial_ratio` and `heavy_commercial_ratio` should be 1.0. e.g
{
...
"personal_traffic_ratio": 0.96,
"medium_commercial_ratio": 0.02,
"heavy_commercial_ratio": 0.02,
}

The following properties can be set to specify Pedestrian Calibration:

- `has_pedestrian_calibration` (optional): Boolean. Set to `true` to enable Pedestrian Calibration.
- `pedestrian_calibration_value` (optional): Integer with a value between 0 and 999,999. Required if `has_pedestrian_calibration` is set. Specifies the pedestrian traffic at the Zone.

The following properties can be set to specify Bicycle Calibration:

- `has_bike_calibration` (optional): Boolean. Set to `true` to enable Bicycle Calibration.
- `bike_calibration_value` (optional): Integer with a value between 0 and 10,000. Required if `has_bike_calibration` is set. Specifies the bicycle traffic at the Zone.

### `zone_set_name` request-body property (optional, string)

The `zone_set_name` request-body property is optional. If specified, it must be a string that is case-insensitive unique in your organization's account and no longer than 50 characters. Subsequent Create Analysis requests can refer to zone sets by either their name or their UUID. If the caller does not specify this property, the server will assign a name identical to the UUID that it also assigns.

### `geom_type` request-body property (optional, string)

The `geom_type` request-body property is optional and represents the zone set geometry type. The default value is `polygon`. If specified, it must be a string with possible values: `polygon` or `line` and the `zones` feature collection must have the corresponding GeoJSON geometry type of MultiPolygon or LineString.

### `with_calibration` request-body property (optional, Boolean)

The `with_calibration` request-body property is optional. The default value is `false`. Set `with_calibration` to `true` to indicate that the Zone Set contains Calibration Zones.

## HTTP status codes

Returns `201 Created` if successful. Returns `400 Bad Request` with an error message in the response body on input error.

## HTTP response body

The HTTP response body is in JSON format. The server assigns your newly created zone set a UUID (universally unique ID) and returns that in the response body. It also assigns a name that is equal to the UUID unless you chose to specify an optional `zone_set_name` in your request body.

### Response-body example

    {
      "name": "a486a871-c610-4a0e-b87e-9b3c030862a1",
      "status": "success",
      "uuid": "a486a871-c610-4a0e-b87e-9b3c030862a1"
    }

### `name` response-body property

The name of the zone set that was created. You can refer to the zone set by either name or UUID in subsequent Create Analysis requests.

### `uuid` response-body property

The UUID (universally unique ID) of the zone set that was created, assigned by the server. You can refer to the zone set by either name or UUID in subsequent Create Analysis requests.

### `status` response-body property

Will always be `success` when the is request successful.

## Example request

This example request and response was generated using the `curl` command-line utility. See the [Data API Quick Start](../quickstart) for instructions to rerun this example against the live server.

    POST /api/v2/zone_sets?SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1 HTTP/1.1
    User-Agent: curl/7.35.0
    Host: insight.streetlightdata.com
    Accept: */*
    Content-Type: application/json
    Content-Length: 2004
    Expect: 100-continue

    {
        "geom_type":"polygon",
        "with_calibration": 1,
        "zones":{
            "type":"FeatureCollection",
            "features":[
                {
                    "type":"Feature",
                    "properties":{
                        "id":1,
                        "name":"Mission",
                        "is_pass":0,
                        "direction":null
                    },
                    "geometry":{
                        "type":"MultiPolygon",
                        "coordinates": [ [ [ [ -122.426698258661972, 37.769562689936315 ], [ -122.423394859041892, 37.772083876030344 ], [ -122.42225575572462, 37.770418101996292 ], [ -122.411206453547067, 37.769427623969634 ], [ -122.406991771273155, 37.769067446852375 ], [ -122.404656609472752, 37.767716767038294 ], [ -122.405169205965521, 37.762628984940662 ], [ -122.406593085112107, 37.760557752167074 ], [ -122.405795712790038, 37.758441432691242 ], [ -122.403232730326167, 37.75722564731312 ], [ -122.402549268335804, 37.751821915004783 ], [ -122.403346640657901, 37.749390106706535 ], [ -122.407561322931784, 37.748399347080543 ], [ -122.424875693354338, 37.74781389197571 ], [ -122.426698258661972, 37.769562689936315 ] ] ] ]
                    }
                },
                {
                    "type":"Feature",
                    "properties":{
                        "id":2,
                        "name":"Financial District",
                        "is_pass":1,
                        "direction": 0.0,
                        "calibration_type": "AADT",
                        "calibration_value": 10000,
                        "personal_traffic_ratio": 0.96,
                        "medium_commercial_ratio": 0.02,
                        "heavy_commercial_ratio": 0.02,
                    },
                    "geometry":{
                        "type":"MultiPolygon",
                        "coordinates":[ [ [ [ -122.405425504211919, 37.798033588378779 ], [ -122.398476973976571, 37.798933675051543 ], [ -122.396654408668923, 37.799698740100226 ], [ -122.397024617247041, 37.79929370664977 ], [ -122.396768319000643, 37.798911173018389 ], [ -122.395828558763895, 37.797898574431919 ], [ -122.393607307295227, 37.799113691070012 ], [ -122.392610591892605, 37.797876072083447 ], [ -122.394233814119715, 37.79690846455324 ], [ -122.393037755636598, 37.795670808599994 ], [ -122.3913575782436, 37.796278387822021 ], [ -122.390987369665496, 37.795693311702443 ], [ -122.392439726395011, 37.794500642185817 ], [ -122.389278714689581, 37.791462623416393 ], [ -122.401182344355107, 37.781965196242638 ], [ -122.405824190372982, 37.785701296639232 ], [ -122.406222876534017, 37.785723802695827 ], [ -122.407134159187834, 37.790337399578668 ], [ -122.404058580231194, 37.790764986655553 ], [ -122.405425504211919, 37.798033588378779 ] ] ] ]
                    }
                }
            ]
        }
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
      "name": "a486a871-c610-4a0e-b87e-9b3c030862a1",
      "status": "success",
      "uuid": "a486a871-c610-4a0e-b87e-9b3c030862a1"
    }

Copyright &copy; 2021, StreetLight Data, Inc. All rights reserved.
