i3s-spec
========

*Indexed 3D Scene Format Specification*

This repository hosts the specification for the ArcGIS Scene Service and its delivery format I3S (Indexed 3D Scene). These are the core resources:

-	[Indexed 3d Scene Format](./format/Indexed%203d%20Scene%20Format%20Specification.md) – Main specification for the I3S Format
-	[Specification for the REST endpoint](./service/SceneService.md) of the Scene Service with resources and operations
-	A set of example JSON resources for each profile
-   Validator rule files for each profile

The structure of this specification is as follows:
- Format: Full logical format specification, including  physical format specification for packaged i3s caches (*.i3p)
- Profiles: Subsets the full format specification for different data structures: 
    - Features (Meshes, Points, Lines, Polygons)
	- Meshpyramids 
    - Analytics 
    - Pointclouds
- Service: Contains the REST API specification for the Scene Service.

We are also building a [Validation Toolkit](https://devtopia.esri.com/Zurich-R-D-Center/i3s-validator) to support developers.

There is also a set of informative and explorative articles on implementation details and usage strategies for the format available in the [i3s wiki](https://devtopia.esri.com/Zurich-R-D-Center/i3s-spec/wiki/_pages) that includes client traversal patterns, suggestions on optimizations and approaches to steps of the cooking process, such as texture atlas generation.

