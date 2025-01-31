# timeInfo [common profiles]

Time info represents the temporal data of a time-aware layer. The time info provides information such as date fields storing the start and end times for each feature. The statistic of the time fields defines the time extent as a period of time with a definite start and end time. The time encoding is [ECMA ISO8601](ECMA_ISO8601.md). The date time values can be UTC time or local time with offset to UTC. Temporal data is data that represents a state in time. You can to step through periods of time to reveal patterns and trends in your data.

### Related:

[cmn::3DSceneLayer](3DSceneLayer.cmn.md), [psl::3DSceneLayer](3DSceneLayer.psl.md)
### Properties

| Property | Type | Description |
| --- | --- | --- |
| endTimeField | string | The name of the field containing the end time information. |
| startTimeField | string | The name of the field that contains the start time information. |

### Examples 

#### Example: Time with start and end time 

```json
 {
  "timeInfo": {
    "endTimeField": "end",
    "startTimeField": "start"
  }
} 
```

#### Example: Stastics required to define the full time extent. 

Besides timeInfo client application require a full time extent. The min start time and the max end time can be fetched from the statsInfo of the endTimeField and startTimeField. 

```json
 {
  "stats": {
    "minTimeStr": "1944-05-05T23:30:00.000-08:00",
    "maxTimeStr": "2023-09-05T17:30:21.000-08:00",
    "totalValuesCount": 32,
    "mostFrequentValues": [
      {
        "value": "2022-09-02T14:00:00.000-08:00",
        "count": 6
      },
      {
        "value": "2023-09-05T17:30:21.000-08:00",
        "count": 6
      },
      {
        "value": "1944-05-05T23:30:00.000-08:00",
        "count": 5
      },
      {
        "value": "1977-03-15T00:00:00.000-08:00",
        "count": 5
      },
      {
        "value": "2022-08-30T01:00:00.000-08:00",
        "count": 5
      },
      {
        "value": "2022-10-15T23:30:00.000-08:00",
        "count": 5
      }
    ]
  }
} 
```

