# API Reference: Create an Analysis

## Description

Analyses return metrics to understand travel patterns. An analysis is created with mandatory parameters and additional optional attributes for the analysis zones specified in the call.
The Data API supports the following analyses in this release: Origin-Destination, Origin-Destination through Middle Filters, Zone Activity, Trips to or from Pre-set Geography, Segment Analysis, AADT, Top Routes between Origins and Destinations, and Top Routes for Zones.
An Origin-Destination Analysis analyzes traffic from the Origin zones to the Destination zones.
An Origin-Destination through Middle Filters analyzes traffic from the Origin zones, through the Middle Filter zones, and to the Destination zones.
A Zone Activity Analysis analyzes traffic that starts, ends or passes through the given zones.
A Trips to or from Pre-set Geography Analysis analyzes traffic that starts or passes through the given zones and ends at Pre-set Geographies or starts at Pre-set Geographies and ends or passes through the given zones.
An AADT Analysis analyzes the Average Annual Daily Traffic in the given zones.
A Top Routes between Origins and Destinations Analysis analyzes the routes between the given Origin and Destination zones.
A Top Routes for Zones Analysis analyzes the traffic flows to and from the given zones.

Analyses process asynchronously for some time after the server creates them. When their status becomes available, their metric results can be downloaded.

Note: some analysis options are enabled for an organization's account only on request rather than by default. If you are looking for an analysis option in the list below and do not see it, contact your StreetLight Data representative.

## HTTP request method and URL

    POST https://insight.streetlightdata.com/api/v2/analyses

## Limitations

There is currently a rate limit of 3 calls per 15 seconds.


## Authentication

You must provide your API key in each request to identify your organization to StreetLight's servers. Provide your API key using a query parameter named `key`. The query parameter is the part of the request URL after the question mark. Alternatively, you can pass the key using the HTTP header `x-stl-key`. The server returns a `401 Unauthorized` status code if authentication fails.

Contact your StreetLight Data representative to obtain an API key.

## HTTP request headers

    Content-Type: application/json

## HTTP request body

The HTTP request body must be in JSON format. At a minimum, it specifies the analysis type and at least one zone set. There are additional optional parameters to specify the Destination Zone Set (for Origin-Destination analysis type) and other analysis options.

### Request-body example

The following example creates an Origin-Destination Analysis with GPS data. It has the same Zone Set as both the Origin zone set and the Destination zone set. It specifies the 12 months of 2016 as the date range, and specifies day parts and day types. This analysis does not include the trip attribute or traveler attribute analysis options.

    {
      "insight_login_email":"testemail@streetlightdata.com",
      "analysis_type":"OD_Analysis",
      "travel_mode_type":"Truck",
      "description":"My O-D Analysis",
      "oz_sets":[{"uuid":"a486a871-c610-4a0e-b87e-9b3c030862a1"}],
      "dz_sets":[{"uuid":"a486a871-c610-4a0e-b87e-9b3c030862a1"}],
      "date_ranges": [{"start_date": "01/01/2016", "end_date": "12/31/2016"}],
      "day_types":"All Days|17,Weekday|14,Weekend Day|67",
      "day_parts":"All Day|0023,Early AM|0005,Peak AM|0609,Mid-Day|1014,Peak PM|1518,Late PM|1923",
      "trip_attributes":false,
      "traveler_attributes":false
    }

### `insight_login_email` request-body property (required, string)

The `insight_login_email` request-body property is a required login email associated with the specific organization to check for user access.

### `date_ranges` request-body property (optional, array of date ranges)

Default value for O-D Analysis Projects:

    date_ranges: [{
        start_date: "01/01/2016",
        end_date:   "12/31/2016"
     }]

The `date_ranges` request-body property is a list of date ranges. Each date range is an object containing a pair of MM/DD/YYYY dates, with the `start_date` key containing the start of the date range, and the `end_date` key containing the end of the date range. Both `start_date` and `end_date` are inclusive.

`date_ranges` is supported for all `travel_mode_type` settings. If not provided, the analysis will use the default date ranges for the given `travel_mode_type`.

### `day_parts` request-body property (optional, string)

Default value for O-D Analyses:

    "day_parts": "All Day|0023,Early AM|0005,Peak AM|0609,Mid-Day|1014,Peak PM|1518,Late PM|1923"

`day_parts` is a comma-separated list of day parts in the analysis. Each day part has a name separated by the vertical bar from the start hour and end hour from 00 (midnight) to 23 (11 PM). For example, 'All Day|0023' ranges from midnight (00:00) to 11:59 PM. Analyses must define All Day as 0023 (midnight to midnight) and this day part will be added if it is not present.

### `day_types` request-body property (optional, string)

Default value for Origin-Destination Analyses:

    "day_types": "Weekday|14,Weekend Day|67,All Days|17"

`day_types` is a comma-separated list of day types in the analysis. Each day type has a name separated by the vertical bar from the start day of week to the end day of week (1 for Monday through 7 for Sunday). Analyses must define All Day as "17" (Monday through Sunday) and this day type will be added if it is not present.

### `description` request-body property (optional, string)

The `description` request-body property allows the caller to provide more descriptive information about the analysis. It is optional and defaults to `null`.

### `dz_sets` request-body property (optional, array of Zone Set objects)

The `dz_sets` request-body property is required in the following analyses (and specifies the destination zone sets in the analysis): Origin-Destination, Origin-Destination through Middle Filters, and Top Routes Origin-Destination. It does not apply to the following analyses: Zone Activity, Segment Analysis, Trips to or from Pre-set Geography, or Top Routes for Zones. This property is an array of zone set objects in the same format as the `oz_sets` property.

### `enable_visualization` request-body property (optional, boolean)

Default value `false`.

This property controls whether the Analysis will generate a visualization in StreetLight InSight.

### `mfz_sets` request-body property (optional, array of Zone Set objects)

The `mfz_sets` request-body property is required in Origin-Destination through Middle Filters Analysis and specifies the Middle Filter zone sets in the analysis. It does not apply to the following analyses: Origin-Destination, Zone Activity, Trips to or from to Pre-set Geography, AADT, Segment Analysis, Top Routes for Zones, or Top Routes between Origins and Destinations. This property is an array of zone set objects in the same format as the `oz_sets` property. However, all zones in the zone sets must be pass through.

### `geography_type` request-body property (optional, string)

The `geography_type` request-body property is required in Trips to or from Pre-set Geography Analyses. It does not apply to the following analyses: Origin-Destination, Origin-Destination through Middle Filters, Segment Analysis, or Zone Activity. This property is a string of one of ('zip', 'taz', 'blkgrp', or 'da').

### `oz_sets` request-body property (required, array of Zone Set objects)

In an Origin-Destination Analysis, Origin-Destination through Middle Filters Analysis, and Top Routes between Origins and Destinations Analysis, the `oz_sets` request-body property specifies the origin zone sets in the analysis. In a Zone Activity Analysis, Trips to or from Pre-set Geography Analysis, AADT Analysis, and Top Routes for Zones Analysis, it specifies the zones of analysis. In a Segment Analysis, the property specifies the zone set in the analysis. This property is required and must be an array of zone set objects. A zone set object identifies a Zone Set by either name or UUID (universally unique ID) and must have one of the following two forms:

    {"name": "some name"}

or

    {"uuid": "server assigned UUID"}

### `analysis_name` request-body parameter (optional, string)

The `analysis_name` request-body property is optional. If specified, it must be a string that is case-insensitive unique in your organization's account and no longer than 50 characters. Subsequent _Query Analysis Status_ and _Get Metrics_ requests can refer to analyses by either their name or their UUID. If the caller does not specify this property, the server will assign a name identical to the UUID that it also assigns.

### `analysis_type` request-body property (required, string)

The `analysis_type` request-body parameter must be a string with one of the following values:

- `OD_Analysis`
- `OD_MF_Analysis`
- `Zone_Activity_Analysis`
- `OD_Preset_Geography`
- `Segment_Analysis`
- `AADT`
- `Top_Routes_OD`
- `Top_Routes_ZA`

### `aadt_year` request-body property (integer)

The `aadt_year` request-body parameter is a required integer when creating an AADT Analysis. It must be one of the following values:

- `2017`
- `2018`
- `2019`
- `2020`

### `segment_types` request-body property (array of string)

The `segment_types` request-body parameter is a required array of strings when creating a Top Routes between Origins and Destinations Analysis or Top Routes for Zones Analysis.

It must contain at least one of the following values:

- `Motorway`
- `Trunk`
- `Primary`
- `Secondary`
- `Tertiary`
- `Residential`

### `travel_mode_type` request-body property (required, string)

The `travel_mode_type` is a required parameter except for the AADT Analysis type. The `travel_mode_type` request-body parameter must be a string with one of the following values:

- `All_Vehicles`
- `Truck`
- `Bicycle`
- `Pedestrian`
- `Bus`
- `Rail`

Note that only certain combinations of analysis_type and travel_mode_type are supported. Here is the current set of supported combinations:

| analysis_type          | travel_mode_type | supported |
| ---------------------- | ---------------- | --------- |
| OD_Analysis            | Truck            | yes       |
| OD_MF_Analysis         | Truck            | yes       |
| Zone_Activity_Analysis | Truck            | yes       |
| OD_Preset_Geography    | Truck            | yes       |
| Segment_Analysis       | Truck            | yes       |
| Top_Routes_OD          | Truck            | yes       |
| Top_Routes_ZA          | Truck            | yes       |
| AADT                   | Truck            | no        |
| OD_Analysis            | All_Vehicles     | yes       |
| OD_MF_Analysis         | All_Vehicles     | yes       |
| Zone_Activity_Analysis | All_Vehicles     | yes       |
| OD_Preset_Geography    | All_Vehicles     | yes       |
| Segment Analysis       | All_Vehicles     | yes       |
| Top_Routes_OD          | All_Vehicles     | yes       |
| Top_Routes_ZA          | All_Vehicles     | yes       |
| AADT                   | All_Vehicles     | yes       |
| OD_Analysis            | Bicycle          | yes       |
| OD_MF_Analysis         | Bicycle          | yes       |
| Zone_Activity_Analysis | Bicycle          | yes       |
| OD_Preset_Geography    | Bicycle          | yes       |
| Segment Analysis       | Bicycle          | no        |
| Top_Routes_OD          | Bicycle          | no        |
| Top_Routes_ZA          | Bicycle          | no        |
| AADT                   | Bicycle          | no        |
| OD_Analysis            | Pedestrian       | yes       |
| OD_MF_Analysis         | Pedestrian       | no        |
| Zone_Activity_Analysis | Pedestrian       | yes       |
| OD_Preset_Geography    | Pedestrian       | yes       |
| Segment Analysis       | Pedestrian       | no        |
| Top_Routes_OD          | Pedestrian       | no        |
| Top_Routes_ZA          | Pedestrian       | no        |
| AADT                   | Pedestrian       | no        |
| OD_Analysis            | Bus              | yes       |
| OD_MF_Analysis         | Bus              | yes       |
| Zone_Activity_Analysis | Bus              | yes       |
| OD_Preset_Geography    | Bus              | no        |
| Segment Analysis       | Bus              | no        |
| Top_Routes_OD          | Bus              | no        |
| Top_Routes_ZA          | Bus              | no        |
| AADT                   | Bus              | no        |
| OD_Analysis            | Rail             | yes       |
| OD_MF_Analysis         | Rail             | yes       |
| Zone_Activity_Analysis | Rail             | yes       |
| OD_Preset_Geography    | Rail             | no        |
| Segment Analysis       | Rail             | no        |
| Top_Routes_OD          | Rail             | no        |
| Top_Routes_ZA          | Rail             | no        |
| AADT                   | Rail             | no        |

Also note that for analyses with travel_mode_type of Bicycle or Pedestrian, only date ranges containing full months are supported.

### `traveler_attributes` request-body property (optional, boolean)

Default value: `false` (only applies to the following analysis: Origin-Destination, Origin-Destination through Middle Filters, Trips to or from Pre-set Geography, and Zone Activity)

This property controls whether the analysis results will include the add-on traveler attribute metrics. Traveler attribute metrics include traveler demographics and simple trip purpose.

### `trip_attributes` request-body property (optional, boolean)

Default value: `false` (only applies to the following analysis: Origin-Destination, Origin-Destination through Middle Filters, Trips to or from Pre-set Geography, and Zone Activity)

This property controls whether the analysis results will include the add-on trip attribute metrics: trip time distribution, trip length distribution, trip speed distribution, and trip circuity distribution. If you specify this property, you can also customize the following properties:

- `trip_duration_bins`
- `trip_length_bins`
- `trip_speed_bins`
- `trip_circuity_bins`
- `speed_percentile_bins` (Available only for Origin-Destination, Origin-Destination through Middle Filters)

_For Segment Analysis_, you cannot enable trip attributes or traveler attributes. However, you can specify the following properties:

- `trip_duration_bins`
- `trip_speed_bins`

### `enable_speed_percentile` request-body property (optional, boolean)

Default value: `false` (only supported for the following analysis: Segment Analysis)

This property when enabled will allow you to specify percentile values `speed_percentile_bins`, which takes a `String` containing a list of comma separated integers. Percentile values must be greater than 0 and less than 100.

For example:

    {
      "enable_speed_percentile": true,
      "speed_percentile_bins": "10,20,30,40"
    }

If the setting is enabled without any specific bins defined, then the default percentile values are used:

    "speed_percentile_bins": "5,15,85,95"

### `vehicle_weight` request-body property (optional, string)

Default value: `null` (applies only to Truck Analyses)

Allowed values: `null`, `Medium`, `Heavy`, `Medium,Heavy`

This property controls whether metric results for the analysis are broken down by vehicle weight class (medium duty, heavy duty) for commercial vehicles. If its value is `null`, commercial vehicle results are not broken down by vehicle weight class.

### `output_type` request-body property (optional, string)

Default value: `index`

The `output_type` request-body parameter must be a string with one of the following values:

- `volume`
- `trip_counts`
- `aadt`
- `index`
- `zone_counts`

_For Analyses using `Bus` or `Rail` travel types_, only default output type value `index` is allowed.

### `aadt_calibration_year` request-body property (optional, integer)

The `aadt_calibration_year` request-body parameter is a required integer when creating an analysis with AADT output. It must be one of the following values:

- `2017`
- `2018`
- `2019`
- `2020`

### `az_sets` request-body property (optional, array of zone set objects)

The `az_sets` request-body property is required when creating an Analysis with AADT output. This property is an array of Zone Set objects in the same format as the `oz_sets` property.

### `cz_sets` request-body property (optional, array of zone set objects)

The `cz_sets` request-body property is required when creating an Analysis with Zone Counts output. `cz_sets` must be Zone Sets with calibration values specified. This property is an array of Zone Set objects in the same format as the `oz_sets` property.

### `enable_home_work_locations` request-body property (optional, boolean)

Default value: `false` (applies only to Zone Activity Analysis)

This property controls whether the Analysis results will include Home and Work Locations metrics.

If you specify this, you need at least one of the following properties be set to `True`:

- `hwl_enable_visitor`
- `hwl_enable_resident`
- `hwl_enable_worker`

This property is not supported for travel_mode_type of `Truck`. Home-Work locations are only supported for other modes of travel in Zone Activity Analyses.

### `zone_intersection_type` request-body property (optional, string)

Default value: `trips_by_pass_through_setting` (applies only to Zone Activity Analysis)

The `zone_intersection_type` (applies only to Zone Activity Analysis with Home and Work Locations metrics enabled) request-body parameter must be a string with one of the following two values:

- `all_trips_for_zone`
- `trips_by_pass_through_setting`

### `hwl_enable_visitor` request-body property (optional, boolean)

Default value: `True` (applies only to Zone Activity Analysis)

This property controls whether the Analysis results will include visiting trips that neither reside or work in the zone. It applies only to Zone Activity Analysis with Home and Work Locations metrics enabled.

### `hwl_enable_resident` request-body property (optional, boolean)

Default value: `False` (applies only to Zone Activity Analysis)

This property controls whether the Analysis results will include trips that reside in the zone. It applies only to Zone Activity Analysis with Home and Work Locations metrics enabled.

### `hwl_enable_worker` request-body property (optional, boolean)

Default value: `False` (applies only to Zone Activity Analysis)

This property controls whether the Analysis results will include trips that work in the zone. It applies only to Zone Activity Analysis with Home and Work Locations metrics enabled.

### `is_massive_queue` request-body property (optional, boolean)

Default value: `False`.

The `is_massive_queue` property controls whether the Analysis will process alongside other high volume Analyses in order to optimize calculation time.

### `tags` request-body property (optional, array of Tag names)

The `tags` property is an array of Tag name strings created within an Organization to associate with the created Analysis.

For example: "tags": ["My Tag", "March2020"], where "My Tag" and "March2020" are Tags that exist within the user's Organization.

### `enable_15min` request-body property (optional, boolean)

Default value: `False`(applies only to Origin-Destination, Zone Activity Analysis, and Segment Analysis)

The `enable_15mins` property controls whether the Analysis will analyze in 15-minute day parts.

This property cannot be set to `True` for analyses using `Bus` or `Rail` travel types.

### `enable_upsampling` request-body property (optional, boolean)

Default value: `True`

The `enable_upsampling` property controls whether the Analysis will process with upsampling if it meets the necessary thresholds. This setting only applies to analysis with `enable_15min` enabled.

### `unit_of_measurement` request-body property (optional, string)

The `unit_of_measurement` property controls whether distances in Analysis results will be computed using miles or kilometers.

If the parameter is set, it must be set to one of the following values:

- `miles`
- `km`

By default, the unit will be set as per the organization level flag controlled by the organization administrators. Generally, it will be miles for US-based organizations and kilometers for Canada based organizations unless changed.

### `enable_completion_email` request-body property (optional, boolean)

Default value: `False`

The `enable_completion_email` property controls whether the Analysis will send an email upon its completion.

## HTTP status codes

Returns `201 Created` on success. Returns `400 Bad Request` with an error message in the response body on input error.

## HTTP response body

The HTTP response body is in JSON format. The server assigns your newly created Analysis a UUID (universally unique ID) and returns that in the response body. It also assigns a name that is equal to the UUID unless you chose to specify an optional `analysis_name` in your request body.

### Response-body example

    {
      "name": "a486a871-c610-4a0e-b87e-9b3c030862a1",
      "status": "success",
      "uuid": "a486a871-c610-4a0e-b87e-9b3c030862a1"
    }

### `name` response-body property

The name of the analysis that was created. You can refer to the analysis by either name or UUID in subsequent _Query Analysis Status_ or _Get Metrics_ requests.

### `uuid` response-body property

The UUID (universally unique ID) of the Analysis that was created, assigned by the server. You can refer to the Analysis by either name or UUID in subsequent _Query Analysis Status_ or _Get Metrics_ requests.

### `status` response-body property

Will always be `success` when the request is successful.

## Example request

This example request and response was generated using the `curl` command-line utility. See the [Data API Quick Start](../quickstart) for instructions to rerun this example against the live server.

    POST /api/v2/analyses?SS5OKOrGT4rQw/FCXZs55eEPZd6u0nd1 HTTP/1.1
    User-Agent: curl/7.35.0
    Host: insight.streetlightdata.com
    Accept: */*
    content-type: application/json
    Content-Length: 514

    {
      "insight_login_email":"testemail@streetlightdata.com",
      "analysis_type":"OD_Analysis",
      "travel_mode_type":"Truck",
      "description":"",
      "oz_sets":[{"uuid":"a486a871-c610-4a0e-b87e-9b3c030862a1"}],
      "dz_sets":[{"uuid":"a486a871-c610-4a0e-b87e-9b3c030862a1"}],
      "date_ranges": [{"start_date": "01/01/2016", "end_date": "12/31/2016"}],
      "day_types":"ALl Days|17,Weekday|14,Weekend Day|67",
      "day_parts":"All Day|0023,Early AM|0005,Peak AM|0609,Mid-Day|1014,Peak PM|1518,Late PM|1923",
      "trip_attributes":false,
      "traveler_attributes":false
    }

## Example response

    HTTP/1.1 201 CREATED
    Date: Mon, 10 Apr 2017 16:31:06 GMT
    Content-Type: application/json
    Content-Length: 128
    Connection: keep-alive
    Set-Cookie: __cfduid=dca2d581c8f10c4dde207f0f0da2c5e2e1491841866; expires=Tue, 10-Apr-18 16:31:06 GMT; path=/; domain=.streetlightdata.com; HttpOnly
    Signature: 08a12cbd0e03edec92da03abb8ad3d0a17507b63
    Cache-Control: no-cache, no-store, must-revalidate
    Pragma: no-cache
    Expires: 0
    Server: cloudflare-nginx
    CF-RAY: 34d718306e7b11f5-SJC

    {
      "name": "d91f40fa-afba-4f1a-9442-8cb65f6d5e62",
      "status": "success",
      "uuid": "d91f40fa-afba-4f1a-9442-8cb65f6d5e62"
    }

Copyright &copy; 2021, StreetLight Data, Inc. All rights reserved.
