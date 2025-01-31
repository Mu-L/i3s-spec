Version History

===============================================
Last updated 11/05/2024

### Version 1.10

- Added timeInfo to 3D object (cmn profile) and point scene layer. The timeInfo property defines the start and end time as well as the full time extent of a layer. This property is often used to time enable a layer for example to participate in a time slider and animate feature to be visible at specific times.
- Added rangeInfo to 3D object (cmn profile) and point scene layer. The rangeInfo property defines min and max range of a feature. This property can be used to show individual floors of a building,for example.

### Version 2.1 (Point Cloud Scene Layer)

- Added capablity "Extract" to point cloud scene layers. The indication of the capability extract allows client application clip part of a layer to create a new SLPK, for example. 

### Version 1.9

- Added capablity "Extract" to integrated mesh, 3D objects, points, and building scene layers. The indication of the capability extract allows client application clip part of a layer to create a new SLPK, for example.
- Defining time as [ISO 8601](docs/1.9/ECMA_ISO8601.md) to provide well defined, unambigious representation of calendar dates and times.

### Version 1.8

Released 5/21/2021 1.8 Versions of [3D Object Scene Layer](docs/1.8/3Dobject_ReadMe.md), [Integrated Mesh Scene Layer](docs/1.8/IntegratedMesh_ReadMe.md), [Building Scene Layer](docs/1.8/BSL_ReadMe.md) and [Point Scene Layer](docs/1.8/Point_ReadMe.md)

 - Upgrade [I3S Converter Tool](i3s_converter/i3s_converter_ReadMe.md) to convert I3S 1.4 - 1.7 to 1.8 versions
 - Minor updates

### Version 1.7

Released 9/29/2020 [Point Scene Layer 1.7](docs/1.7/Point_ReadMe.md)
 - [I3S Converter Tool](i3s_converter/i3s_converter_ReadMe.md) upgraded support to convert Point Scene Layers to 1.7.

Released 7/28/2020 [ESLPK and I3SREST Formats](format/Indexed&#32;3d&#32;Scene&#32;Layer&#32;Format&#32;Specification.md#i3s-scene-layer-packages)
 - [I3S Converter Tool](i3s_converter/i3s_converter_ReadMe.md) upgrade to support these formats

Released 12/15/2019 [Building Scene Layer](docs/1.7/BSL_ReadMe.md) Specification upgrade to 1.7.
- Upgrade [tooling slpk](i3s_converter/i3s_converter_ReadMe.md) to convert 1.6 building scene layer to I3S 1.7.

Released 06/30/2019 - (applies to [MeshPyramids](docs/1.7/store.cmn.md) profile)

#### [3D Object Scene Layer](docs/1.7/3Dobject_ReadMe.md) and [Integrated Mesh Scene Layer](docs/1.7/IntegratedMesh_ReadMe.md)

  - Nodes are now accessible as pages using a [node page](docs/1.7/nodePageDefinition.cmn.md) - significantly reducing server-client traffic.
  - Support for [draco geometry compression](docs/1.7/compressedAttributes.cmn.md) - more compact geometry allows for smaller payloads.
  - Support for [advanced material](docs/1.7/materialDefinitions.cmn.md) such as physically based materials.
  - Deprecated [SharedResource](docs/1.7/sharedResource.cmn.md) - sharedResource properties are readily available in the node index resource.
  - New [tooling to validate existing slpk](i3s_converter/i3s_converter_ReadMe.md) and convert Integrated Mesh or 3D Object scene layers to I3S 1.7.

I3S specification version 1.7 is backwards compatible with I3S Version 1.6 and is currently supported by ArcGIS Pro 2.4 and ArcGIS Online.  More support of I3S 1.7 across the ArcGIS platform will roll out in upcoming releases.

### Version 1.6

Released 03/01/2019 - (applies to [MeshPyramids](docs/1.6/store.cmn.md profile) and officially submitted to the OGC in August 2019.

#### [3D Object Scene Layer](docs/1.6/3Dobject_ReadMe.md)
- [oriented bounding boxes](docs/1.6/obb.cmn.md) - Introduces support for oriented bounding boxes as a bounding volume.
- [attribute domain](docs/1.6/domain.cmn.md) (i.e. field) - Attribute domains are rules that describe the allowed values of a field type, providing a method for enforcing data integrity.  For example, domain values can be used in pop-ups with definition queries.
- [serviceUpdateTimeStamp](docs/1.6/serviceUpdateTimeStamp.cmn.md) - Provides the time stamp when the I3S service or the source of the service was created or updated. This property can be used in conjunction with the associated feature layer for editing.

#### [Building Scene Layer](docs/1.6/BSL_ReadMe.md)
- [Building Scene Layer](docs/1.6/BSL_ReadMe.md) profile specification. The Building Scene Layer is used to visualize and work with buildings.

### Version 2.0 (Point Cloud Scene Layer)

Released 03/01/2019  - (applies to [Point Cloud](docs/1.6/store.cmn.md) profile)

#### [Point Cloud Scene Layer](docs/2.0/pcsl_ReadMe.md)

- [Point Cloud Scene Layer](docs/2.0/pcsl_ReadMe.md) profile specification.  The Point Cloud Scene Layer is used to visualize sensor data, including LiDAR.
