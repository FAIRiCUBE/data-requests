File C:\Users\Kathi\Dropbox\cove\FAIRiCUBE\WP5\Untitled8.xml is not valid.
	Neither an element declaration nor a type definition is known for element <wcs:CoverageDescriptions>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <wcs:CoverageDescriptions>. Strict assessment failed.
	Neither an element declaration nor a type definition is known for element <wcs:CoverageDescription>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <wcs:CoverageDescription>. Strict assessment failed.
	Value '"2011-01-01T00:00:00.000Z" -90.25 -179.75' is not allowed for element <gml:lowerCorner>.
		Annotations of type 'gml:DirectPositionType' (see below)
			Direct position instances hold the coordinates for a position within some coordinate reference system (CRS). Since direct positions, as data types, will often be included in larger objects (such as geometry elements) that have references to CRS, the srsName attribute will in general be missing, if this particular direct position is included in a larger element with such a reference to a CRS. In this case, the CRS is implicitly assumed to take on the value of the containing object's CRS.
			if no srsName attribute is given, the CRS shall be specified as part of the larger context this geometry element is part of, typically a geometric object like a point, curve, etc.
		Annotations of type 'gml:doubleList' (see below)
			A type for a list of values of the respective simple type.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gml:boundedBy / gml:Envelope / gml:lowerCorner / [TEXT]
		Details
			cvc-datatype-valid.1.2.1: For type definition 'double' the string '"2011-01-01T00:00:00.000Z"' does not match a literal in the lexical space of built-in type definition 'double'.
			cvc-datatype-valid.1.2.2: Substring '"2011-01-01T00:00:00.000Z"' of string '"2011-01-01T00:00:00.000Z" -90.25 -179.75' is not datatype valid with respect to item type definition 'double' of simple type definition 'gml:doubleList'.
			cvc-simple-type.1: For type definition 'gml:doubleList' the string '"2011-01-01T00:00:00.000Z" -90.25 -179.75' is not valid.
			cvc-complex-type.2.2: Content of element <gml:lowerCorner> must be valid with respect to its type definition 'gml:DirectPositionType'.
			cvc-type.3.2: Element <gml:lowerCorner> is not valid with respect to type definition 'gml:DirectPositionType'.
			cvc-elt.5.2.1: The element <gml:lowerCorner> is not valid with respect to the actual type definition 'gml:DirectPositionType'.
			cvc-assess-elt.1.1: Strict assessment of element <gml:lowerCorner> with governing element declaration 'gml:lowerCorner' failed.
	Value '"2018-12-31T00:00:00.000Z" 89.75 180.25' is not allowed for element <gml:upperCorner>.
		Annotations of type 'gml:DirectPositionType' (see below)
			Direct position instances hold the coordinates for a position within some coordinate reference system (CRS). Since direct positions, as data types, will often be included in larger objects (such as geometry elements) that have references to CRS, the srsName attribute will in general be missing, if this particular direct position is included in a larger element with such a reference to a CRS. In this case, the CRS is implicitly assumed to take on the value of the containing object's CRS.
			if no srsName attribute is given, the CRS shall be specified as part of the larger context this geometry element is part of, typically a geometric object like a point, curve, etc.
		Annotations of type 'gml:doubleList' (see below)
			A type for a list of values of the respective simple type.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gml:boundedBy / gml:Envelope / gml:upperCorner / [TEXT]
		Details
			cvc-datatype-valid.1.2.1: For type definition 'double' the string '"2018-12-31T00:00:00.000Z"' does not match a literal in the lexical space of built-in type definition 'double'.
			cvc-datatype-valid.1.2.2: Substring '"2018-12-31T00:00:00.000Z"' of string '"2018-12-31T00:00:00.000Z" 89.75 180.25' is not datatype valid with respect to item type definition 'double' of simple type definition 'gml:doubleList'.
			cvc-simple-type.1: For type definition 'gml:doubleList' the string '"2018-12-31T00:00:00.000Z" 89.75 180.25' is not valid.
			cvc-complex-type.2.2: Content of element <gml:upperCorner> must be valid with respect to its type definition 'gml:DirectPositionType'.
			cvc-type.3.2: Element <gml:upperCorner> is not valid with respect to type definition 'gml:DirectPositionType'.
			cvc-elt.5.2.1: The element <gml:upperCorner> is not valid with respect to the actual type definition 'gml:DirectPositionType'.
			cvc-assess-elt.1.1: Strict assessment of element <gml:upperCorner> with governing element declaration 'gml:upperCorner' failed.
	Neither an element declaration nor a type definition is known for element <wcs:CoverageId>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / wcs:CoverageId
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <wcs:CoverageId>. Strict assessment failed.
	Neither an element declaration nor a type definition is known for element <gmlcov:metadata>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gmlcov:metadata
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <gmlcov:metadata>. Strict assessment failed.
	Attribute 'gmlrgrid:id' is not allowed in element <gmlrgrid:ReferenceableGridByVectors>
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gml:domainSet / gmlrgrid:ReferenceableGridByVectors / @gmlrgrid:id
		Details
			cvc-complex-type.3.2.1: Complex type definition 'gmlrgrid:ReferenceableGridByVectorsType' of element <gmlrgrid:ReferenceableGridByVectors> does not allow attribute 'gmlrgrid:id' and has no attribute wildcard.
			cvc-type.3.2: Element <gmlrgrid:ReferenceableGridByVectors> is not valid with respect to type definition 'gmlrgrid:ReferenceableGridByVectorsType'.
			cvc-elt.5: The element <gmlrgrid:ReferenceableGridByVectors> is not valid with respect to the actual type definition 'gmlrgrid:ReferenceableGridByVectorsType'.
			cvc-assess-elt.1.1: Strict assessment of element <gmlrgrid:ReferenceableGridByVectors> with governing element declaration 'gmlrgrid:ReferenceableGridByVectors' failed.
	Value '"2011-01-01T00:00:00.000Z" 89.5 -179.5' is not allowed for element <gml:pos>.
		Annotations of type 'gml:DirectPositionType' (see below)
			Direct position instances hold the coordinates for a position within some coordinate reference system (CRS). Since direct positions, as data types, will often be included in larger objects (such as geometry elements) that have references to CRS, the srsName attribute will in general be missing, if this particular direct position is included in a larger element with such a reference to a CRS. In this case, the CRS is implicitly assumed to take on the value of the containing object's CRS.
			if no srsName attribute is given, the CRS shall be specified as part of the larger context this geometry element is part of, typically a geometric object like a point, curve, etc.
		Annotations of type 'gml:doubleList' (see below)
			A type for a list of values of the respective simple type.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gml:domainSet / gmlrgrid:ReferenceableGridByVectors / gmlrgrid:origin / gml:Point / gml:pos / [TEXT]
		Details
			cvc-datatype-valid.1.2.1: For type definition 'double' the string '"2011-01-01T00:00:00.000Z"' does not match a literal in the lexical space of built-in type definition 'double'.
			cvc-datatype-valid.1.2.2: Substring '"2011-01-01T00:00:00.000Z"' of string '"2011-01-01T00:00:00.000Z" 89.5 -179.5' is not datatype valid with respect to item type definition 'double' of simple type definition 'gml:doubleList'.
			cvc-simple-type.1: For type definition 'gml:doubleList' the string '"2011-01-01T00:00:00.000Z" 89.5 -179.5' is not valid.
			cvc-complex-type.2.2: Content of element <gml:pos> must be valid with respect to its type definition 'gml:DirectPositionType'.
			cvc-type.3.2: Element <gml:pos> is not valid with respect to type definition 'gml:DirectPositionType'.
			cvc-elt.5.2.1: The element <gml:pos> is not valid with respect to the actual type definition 'gml:DirectPositionType'.
			cvc-assess-elt.1.1: Strict assessment of element <gml:pos> with governing element declaration 'gml:pos' failed.
	Value '"2011-01-01T00:00:00.000Z" "2011-01-02T00:00:00.000Z" "2011-01-03T00:00:00.000Z" "2011-01-04T00:00:0...' is not allowed for element <gmlrgrid:coefficients>.
		Annotations of type 'gml:doubleList' (see below)
			A type for a list of values of the respective simple type.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gml:domainSet / gmlrgrid:ReferenceableGridByVectors / gmlrgrid:generalGridAxis / gmlrgrid:GeneralGridAxis / gmlrgrid:coefficients / [TEXT]
		Details
			cvc-datatype-valid.1.2.1: For type definition 'double' the string '"2011-01-01T00:00:00.000Z"' does not match a literal in the lexical space of built-in type definition 'double'.
			cvc-datatype-valid.1.2.2: Substring '"2011-01-01T00:00:00.000Z"' of string '"2011-01-01T00:00:00.000Z" "2011-01-02T00:00:00.000Z" "2011-01-03T00:00:00.000Z" "2011-01-04T00:00:00.000Z" "2011-01-05T00:00:00.000Z" "2011-01-06T00:00:00.000Z" "2011-01-07T00:00:00.000Z" "2011-01-08T00:00:00.000Z" "2011-01-09T00:00:00.000Z" "2011-0...' is not datatype valid with respect to item type definition 'double' of simple type definition 'gml:doubleList'.
			cvc-simple-type.1: For type definition 'gml:doubleList' the string '"2011-01-01T00:00:00.000Z" "2011-01-02T00:00:00.000Z" "2011-01-03T00:00:00.000Z" "2011-01-04T00:00:0...' is not valid.
			cvc-type.3.1.3: The normalized value '"2011-01-01T00:00:00.000Z" "2011-01-02T00:00:00.000Z" "2011-01-03T00:00:00.000Z" "2011-01-04T00:00:0...' is not valid with respect to the type definition 'gml:doubleList'.
			cvc-elt.5.2.1: The element <gmlrgrid:coefficients> is not valid with respect to the actual type definition 'gml:doubleList'.
			cvc-assess-elt.1.1: Strict assessment of element <gmlrgrid:coefficients> with governing element declaration 'gmlrgrid:coefficients' failed.
	Neither an element declaration nor a type definition is known for element <gmlcov:rangeType>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gmlcov:rangeType
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <gmlcov:rangeType>. Strict assessment failed.
	Neither an element declaration nor a type definition is known for element <swe:DataRecord>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gmlcov:rangeType / swe:DataRecord
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <swe:DataRecord>. Strict assessment failed.
	Neither an element declaration nor a type definition is known for element <swe:field>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gmlcov:rangeType / swe:DataRecord / swe:field
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <swe:field>. Strict assessment failed.
	Neither an element declaration nor a type definition is known for element <swe:Quantity>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gmlcov:rangeType / swe:DataRecord / swe:field / swe:Quantity
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <swe:Quantity>. Strict assessment failed.
	Neither an element declaration nor a type definition is known for element <swe:label>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gmlcov:rangeType / swe:DataRecord / swe:field / swe:Quantity / swe:label
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <swe:label>. Strict assessment failed.
	Neither an element declaration nor a type definition is known for element <swe:description>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gmlcov:rangeType / swe:DataRecord / swe:field / swe:Quantity / swe:description
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <swe:description>. Strict assessment failed.
	Neither an element declaration nor a type definition is known for element <swe:nilValues>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gmlcov:rangeType / swe:DataRecord / swe:field / swe:Quantity / swe:nilValues
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <swe:nilValues>. Strict assessment failed.
	Neither an element declaration nor a type definition is known for element <swe:NilValues>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gmlcov:rangeType / swe:DataRecord / swe:field / swe:Quantity / swe:nilValues / swe:NilValues
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <swe:NilValues>. Strict assessment failed.
	Neither an element declaration nor a type definition is known for element <swe:nilValue>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gmlcov:rangeType / swe:DataRecord / swe:field / swe:Quantity / swe:nilValues / swe:NilValues / swe:nilValue
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <swe:nilValue>. Strict assessment failed.
	Neither an element declaration nor a type definition is known for element <swe:uom>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gmlcov:rangeType / swe:DataRecord / swe:field / swe:Quantity / swe:uom
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <swe:uom>. Strict assessment failed.
	Neither an element declaration nor a type definition is known for element <swe:constraint>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / gmlcov:rangeType / swe:DataRecord / swe:field / swe:Quantity / swe:constraint
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <swe:constraint>. Strict assessment failed.
	Neither an element declaration nor a type definition is known for element <wcs:ServiceParameters>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / wcs:ServiceParameters
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <wcs:ServiceParameters>. Strict assessment failed.
	Neither an element declaration nor a type definition is known for element <wcs:CoverageSubtype>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / wcs:ServiceParameters / wcs:CoverageSubtype
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <wcs:CoverageSubtype>. Strict assessment failed.
	Neither an element declaration nor a type definition is known for element <wcs:nativeFormat>. Strict assessment failed.
		Error location: wcs:CoverageDescriptions / wcs:CoverageDescription / wcs:ServiceParameters / wcs:nativeFormat
		Details
			cvc-assess-elt.1: Neither an element declaration nor a type definition is known for element <wcs:nativeFormat>. Strict assessment failed.