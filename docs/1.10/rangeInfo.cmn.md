# rangeInfo [common profiles]

Range information allows to filter features of a layer within a minimum and maximum range. Range is often used to visualize indoor spaces like picking a floor of a building or visualize rooms belonging to a specific occupation.

### Related:

[cmn::3DSceneLayer](3DSceneLayer.cmn.md), [psl::3DSceneLayer](3DSceneLayer.psl.md)
### Properties

| Property | Type | Description |
| --- | --- | --- |
| field | string | Field name to used for the range. The statistics of the field will contain the min and max values of all features for this rangeInfo. |
| name | string | A unique name that can be referenced by an application to represent the range. |

### Examples 

#### Example: rangeInfo 

```json
 {
  "rangeInfo": {
    "field": "LongField",
    "name": "LongField"
  }
} 
```

#### Example: Statistics required to define the full range extent 

Besides rangeInfo client application require a full range extent. The min and max value can be fetched from of the statistics. 

```json
 {
  "stats": {
    "min": 1,
    "max": 5,
    "avg": 2.625,
    "stddev": 1.407885953173359,
    "sum": 21,
    "variance": 1.9821428571428574,
    "histogram": {
      "minimum": 1,
      "maximum": 6,
      "counts": [
        2,
        2,
        2,
        1,
        1
      ]
    },
    "mostFrequentValues": [
      {
        "value": 1,
        "count": 2
      },
      {
        "value": 2,
        "count": 2
      },
      {
        "value": 3,
        "count": 2
      },
      {
        "value": 4,
        "count": 1
      },
      {
        "value": 5,
        "count": 1
      }
    ]
  }
} 
```

