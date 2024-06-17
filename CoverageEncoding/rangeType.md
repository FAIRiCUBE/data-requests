# Specification for provision of rangeType information

OGC CIS uses [SWE Common](https://portal.ogc.org/files/?artifact_id=41157) DataRecord types for the provision of rangeType (description of what the numbers provided in the coverage range actually mean).
To date, it is not always entirely clear how to use this DataRecord element in a coverage context, one reason being the known complexity of SWE; also, in a coverage context not all sensor acquisition information may be of equal relevance.
In order to clarify and exemplify use of SWE Common in CIS encoded data, we will describe the requirements here, together with examples.

A challenge in this context is that many of the detail metadata are not readily available in machine-readable format. In FAIRiCUBE, and likely in many EO data services, data sources used typically require human interpretation of descriptions written in HTML, PDF, or similar, with varying mileage of completeness and conciseness. As both FAIRiCUBE platforms, EOxHub and rasdaman, support the OGC coverage standards, goal is to achieve the same level of (SWE and other) metadata on both. This exercise is considered useful for establishing general best practices useful in other projects, too.  

## SWE Common
The OGC Sensor Web Enablement Suite (SWE) aims to cover requirements pertaining to measured or observed data. 
For CIS encodings, the following requirements classes are of relevance:
- Record Components Package: `The “DataRecord” class is modeled on the definition of ‘Record’ from ISO 11404. In this definition, a record is a composite data type composed of one to many fields, each of which having its own name and type definition.`
- Basic Types and Simple Components Schemas: `XML Schema elements and types defined in the “basic_types.xsd” and “simple_components.xsd” schema files implement all classes defined respectively in the “Basic Types” and “Simple Components” UML packages.`

From the Basic Types and Simple Components, we rely on the Quantity and Category Elements. 
While the Count Element would also be applicable, for the moment we will handle Counts as Quantities with a uom of "1" for "unitless".

## SWE:DataRecord
SWE:DataRecord, derived from the SWE Common AbstractDataComponent, can be used to group multiple components via the `field` attribute. 
Each field describes one band of the described Coverage.

![grafik](https://github.com/FAIRiCUBE/data-requests/assets/11915304/f943b189-cc85-4ccf-a39e-d85cad4a3e6f)

The name attribute of the swe:field must be provided, whereby Req 39 stipulates that `Each “field” attribute in a given instance of the “DataRecord” class shall be identified by a name that is unique to this instance.`

Depending on the nature of the data provided in each band, the correct Simple Component must be provided in the corresponding DataRecord.field.

## SWE:SimpleComponent Elements
All SWE:SimpleComponent types are derived from the SWE:AbstractSimpleComponent. Elements defined for SWE:AbstractSimpleComponent apply to all SWE:SimpleComponent types, thus are described jointly in this section.

![grafik](https://github.com/FAIRiCUBE/data-requests/assets/11915304/04029405-8c1d-4b67-a210-7ce1288423c4)

### definition 
`definition` is a mandatory attribute of the SWE:SimpleComponent types.

Requirement - http://www.opengis.net/spec/SWE/2.0/req/xsd-simple-components/definition-resolvable
`Req 62. The “definition” attribute shall contain a URI that can be resolved to the complete human readable definition of the property that is represented by the data component.`

Additional information on the definition attribute is provided in clause 7.2.2 as follows:
`The “definition” attribute identifies the property (often an observed property in our context) that the data component represents by using a scoped  ame. It should map to a controlled term defined in an (web accessible) dictionary, registry or ontology. Such terms provide the formal textual  efinition agreed upon by one or more communities, eventually illustrated by pictures and diagrams as well as additional semantic information such as relationships to units and other concepts, ontological mappings, etc. `

As Observed Property registers covering FAIRiCUBE requirements have not been identified, alternative solutions may be required. A simple solution would be the use of the [QUDT Quantity Kind Vocabulary](http://qudt.org/2.1/vocab/quantitykind), e.g. [velocity](https://qudt.org/vocab/quantitykind/Velocity) or [radiance](https://qudt.org/vocab/quantitykind/Radiance) in order to provide basic information on the property being conveyed. When re-providing data from Copernicus Services, a reference to the page describing this dataset can be used, e.g. [High Resolution Layer Dominant Leaf Type](https://land.copernicus.eu/en/products/high-resolution-layer-dominant-leaf-type)
If a reference to an Observed Property register is available, this should be used.

When working from a data request, the `Definition` field in the Bands section provides the required content.
If this is missing, and there is only one band, the text from the dataset `Documentation Link` or `Data Source` may be used.

### label
The `label` element is a short descriptive human readable label describing what property the component represents.

When working from a data request, the `cell components` field in the Bands section provides the required content.
If this is missing, and there is only one band, the text from the dataset `Title` may be used.

### description
The `description` element is a longer more descriptive human readable description describing what property the component represents.

When working from a data request, the `Description` field in the Bands section provides the required content.
If this is missing, and there is only one band, the text from the dataset Description may be used.

### nilValues
The `nilValues` element is defined on the SWE:AbstractSimpleComponentType. If nil values are used in the coverage, they must be provided here, together with a reason. The swe:NilValuesType must be used.

When working from a data request, the `Null values` field in the Bands section provides the required content.

## SWE:Quantity
The SWE:Quantity type adds a mandatory `Unit of Measure` element of type swe:UnitReference

When working from a data request, the `Null values` field in the Bands section provides the required content.

Requirement - http://www.opengis.net/spec/SWE/2.0/req/xsd-simple-components/ucum-code-used
Req 64. The UCUM code for a unit of measure shall be used as the value of the “code” XML attribute whenever it can be constructed using the UCUM 1.8 specification. Otherwise the “href” XML attribute shall be used to reference an external unit definition.

Note: UCUM 1.8 has been deprecated, current version is [UCUM 2.1](https://ucum.org/ucum). Thus, we will use UCUM 2.1 in FAIRiCUBE.

The following shows an example of a Quantity rangeType taken from the Demography dataset. Note that ideally we would use the swe:Count type for this purpose.

```
<cis11:RangeType>
	<swe:DataRecord>
		<swe:field name="Population_total">
			<swe:Quantity definition="https://ec.europa.eu/eurostat/web/gisco/geodata/population-distribution/geostat">
				<swe:label>Population total</swe:label>
				<swe:description>The 2021 census contained a major innovation with the presentation of key census topics on an EU-wide 1 km² grid.</swe:description>
				<swe:nilValues>
					<swe:NilValues>
						<swe:nilValue reason="">65535</swe:nilValue>
					</swe:NilValues>
				</swe:nilValues>
				<swe:uom code="1"/>
			</swe:Quantity>
		</swe:field>
	</swe:DataRecord>
</cis11:RangeType>
```

## SWE:Category
The SWE:Category type adds a `codeSpace` element of type swe:UnitReference. This element utilizes xlink:href to reference an external dictionary, taxonomy or ontology representing the code space. This element is implicitely mandatory, as Req 25 stipulates the alternative provision of a `constraint` with a list of allowed values; as the constraint alternative does not allow for additional semantics on the individual entries, the `codeSpace` approach is prefered.

However, the `codeSpace` approach requires the availability of a URI that resolves to information on the categorization used in the data, often not the case. While a machine readable approach would be preferable, in lieu of identified standards in this area, a simple [GitHub page](https://github.com/FAIRiCUBE/data-requests/blob/main/CoverageEncoding/CategoryInformation.md) can suffice.

When working from a data request, the `Category List` field in the Bands section provides the required content.

The following shows an example of a Category rangeType taken from the DominantLeafType dataset

```
<cis11:RangeType>
	<swe:DataRecord>
		<swe:field name="DominantLeafType">
			<swe:Category definition="https://land.copernicus.eu/en/products/high-resolution-layer-dominant-leaf-type">
				<swe:label>Dominant Leaf Type</swe:label>
				<swe:description>The HRL Forest 2018 primary status layer Dominant Leaf Type (DLT) has been created in frame of the tender “EEA/IDM/R0/18/009 - High Resolution land cover characteristics for the 2018 reference year” as part of the EEA Copernicus Land Monitoring Service (CLMS, https://land.copernicus.eu). The DLT raster product provides a basic land cover classification with 3 thematic classes (all non-tree covered areas / broadleaved / coniferous) at 10m spatial resolution and covers the full of EEA39 area. More about the High Resolution Layers and CLMS datasets can be found at https://land.copernicus.eu/pan-european.</swe:description>
				<swe:nilValues>
					<swe:NilValues>
						<swe:nilValue reason="no data">240</swe:nilValue>
						<swe:nilValue reason="outside area">255</swe:nilValue>
					</swe:NilValues>
				</swe:nilValues>
				<swe:codeSpace xlink:href="https://github.com/FAIRiCUBE/data-requests/blob/main/CoverageEncoding/CategoryInformation.md/"/>
			</swe:Category>
		</swe:field>
	</swe:DataRecord>
</cis11:RangeType>
```

