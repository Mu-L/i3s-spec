{
	"featureData": [
		{ // a normal feature using a unique geometry
			"id": 309432971018, // id is a long value.
			"position": [537218.344, 5328647.27], // the x,y offset used by all vertex positions in this feature. Add these values to the feature geometry vertex positions to get absolute projected coordinates in the positionCRS.
			"pivotOffset": [0.0, 0.0, 14.9], // an optional, "semantic" pivot offset that ca. be used to e.g. correctly drape tree symbols.
			"mbb": [537218.283, 5328647.902, 29.821, 5328647.100, 34.155, 537218.098], // xmin, ymin, zmin, xmax, ymax, zmax of the feature's minimum bounding box, expressed in the positionCRS, without offset.
			"layer": "Public Building", // links this feature to a defined layer.
			"geometries": [ // Geometry defintion including materials; note that one Feature can have multiple geometries
				{
					"type": "ArrayBufferView", // type denotes whether the following geometry is defined by using array buffer views (ArrayBufferView), as a reference to a shared Resource (SharedResourceReference) or embedded (Embedded).
					"transformation" : [1.0, 0.0, 0.0, 0.0, -0.0, 1.0, 0.0, 0.0, 0.0, -0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0], // linearized 4x4 transformation matrix. Elements 13-15 of the 16 indicate the translational component.
					"params": { 
						"type": "triangles", // types are: triangle_strip, triangles, lines, points (i.e. GL render primitives)
						"components": [ // a single geometry can have multiple components if different materials are used (i.e. glass for windows, brick texture for walls, ...)
							{
								"material": {
									"id": "Mat01" // ID of the Material, as defined in the shared resources bundle
								}
							},
							{
								"material": {
									"id": "Mat02" // ID of the Material, as defined in the shared resources bundle
								}
							},
							{
								"material": {
									"id": "Mat03" // ID of the Material, as defined in the shared resources bundle
								}
							}
						],
						"vertexAttributes": { // these are the vertex attributes. Each attribute is described by an accessor to the geometry typed array. This is an open list.
							"position": { // the name of the vertex attribute; here: vertex positions
								"byteOffset": 254976, // the starting byte position where the required bytes begin.
								"count": 345, // the number of elements. Multiply by number of bytes used for valueType to know how many bytes need to be read.
								"valueType": "Float32", // the element type, either UInt8, UInt16, Int16, Int32, Int64 or Float32, Float64
								"valuesPerElement": 3  // number of (Float32) values need to make a valid element (here a xyz position)
							},
							"normal": { // the name of the vertex attribute; here: vertex normals
								"byteOffset": 259116, // the starting byte position where the required bytes begin.
								"count": 345, // the number of elements. Multiply by number of bytes used for valueType to know how many bytes need to be read.
								"valueType": "Int16", // the element type, either UInt8, UInt16, Int16, Int32, Int64 or Float32, Float64
								"valuesPerElement": 2 // number of (Int16) values need to make a valid element (here a normal vector)
							},
							"uv0": { // the name of the vertex attribute; here: 1st texture coordinates
								"byteOffset": 260496, // the starting byte position where the required bytes begin.
								"count": 345, // the number of elements. Multiply by number of bytes used for valueType to know how many bytes need to be read.
								"valueType": "Int16", // the element type, either UInt8, UInt16, Int16, Int32, Int64 or Float32, Float64
								"valuesPerElement": 2 // number of (Int16) values need to make a valid element (here a texture coordinate that will be normalized)
							},
							"classification": { // the name of the vertex attribute; here: vertex classification/colors
								"byteOffset": 261876, // the starting byte position where the required bytes begin.
								"count": 345, // the number of elements. Multiply by number of bytes used for valueType to know how many bytes need to be read.
								"valueType": "Int16", // the element type, either UInt8, UInt16, Int16, Int32, Int64 or Float32, Float64
								"valuesPerElement": 3 // number of (UInt8) values need to make a valid element (here a RGB intensity)
							}
						},
						"faces": { // indices for positions, normals, texture coordinates to build faces. This is an open list.
							"position": { // position index array buffer view
								"byteOffset": 165349,
								"count": 345,
								"valueType": "Int16",
								"valuesPerElement": 1,
								"componentIndices": [ // array index where the component starts.
									0,
									36,
									246
								]
							},
							"normal": { // normals index array buffer view
								"byteOffset": 165349,
								"count": 345,
								"valueType": "Int16",
								"valuesPerElement": 1
							},
							"uv0": { // texture coordinates index array buffer view
								"byteOffset": 165349,
								"count": 345,
								"valueType": "Int16",
								"valuesPerElement": 1
							}
						}
					}
				}
			],
			"attributes": [
				{
					"metadata": [ // Special group for default attributes and other metadata.
						{
							"name": "OID",
							"value": 34983
						},
						{
							"name": "area",
							"value": 101131.1435
						},
						{
							"name": "length",
							"value": 390.73893
						}
					]
				},
				{
					"name": "type",
					"value": "Business (Group B)"
				},
				{
					"name": "subtype",
					"value": "Office Building"
				},
				{
					"name": "name",
					"value": "Technopark"
				},
				{
					"name": "description",
					"value": "An office center for high-tech companies and spin-offs"
				},
				{
					"name": "attribution",
					"value": "Stadt Z�rich"
				},
				{
					"name": "totalHeight",
					"value": 30.88
				},
				{
					"name": "eaveHeight",
					"value": 24.35
				},
				{
					"name": "levelsAboveGround",
					"value": 5
				},
				{
					"name": "levelsBelowGround",
					"value": 2
				},
				{
					"name": "status",
					"value": "built"
				},
				{
					"name": "beginLifespan",
					"value": "1993-03-12 00:00:00"
				},
				{
					"name": "endLifespan",
					"value": ""
				},
				{
					"reports": [ // attributes can be grouped!
						{
							"name": "GFA",
							"value": 30000
						}
					]
				}
			]
		},
		{ // a Feature using an instance geometry
			"id": 309432971019,
			"position": [537218.344, 5328647.27], // the x,y offset used by all vertex positions in this feature. Add these values to the feature geometry vertex positions to get absolute projected coordinates in the positionCRS.
			"mbb": [1222178.283, 83371.902, 54758.098, 2242.100, 34.155, 29.821],
			"layer": "Transport Building", 
			"geometries": [ 
				{
					"type": "SharedResourceReference", // type denotes whether the following geometry is defined by using array buffer views (ArrayBufferView), as a reference to a shared Resource (SharedResourceReference) or embedded (Embedded).
					"transformation" : [1.0, 0.0, 0.0, 0.0, -0.0, 1.0, 0.0, 0.0, 0.0, -0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0],
					"params": {
						"id": "Tree_123_Symbol", // ID of the geometry in the shared resource bundle.
					}
				}
			],
			"attributes": [
				{
					"metadata": [ // Special group for default attributes and other metadata.
						{
							"name": "OID",
							"value": 34984
						},
						{
							"name": "area",
							"value": 47472.123
						},
						{
							"name": "length",
							"value": 120.73893
						}
					]
				},
				{
					"name": "type",
					"value": "Business (Group B)"
				},
				{
					"name": "subtype",
					"value": "Office Building"
				},
				{
					"name": "name",
					"value": "Technopark Erweiterung"
				}
			]
		}
	]
}