# Specification for provision of rangeType information

OGC CIS uses [SWE Common](https://portal.ogc.org/files/?artifact_id=41157) DataRecord types for the provision of rangeType (description of what the numbers provided in the coverage range actually mean)
To date, this element has often been filled with erroneous values, not taking requirements from the SWE Common specification into account.
In order to ensure correct provision of CIS encoded data, we will describe the requirements here, together with examples.

## SWE Common
The OGC Sensor Web Enablement Suite aims to cover requirements pertaining to measured or observed data. 
For CIS encodings, the following requirements classes are of relevance:
- Record Components Package: `The “DataRecord” class is modeled on the definition of ‘Record’ from ISO 11404. In this definition, a record is a composite data type composed of one to many fields, each of which having its own name and type definition.`
- Basic Types and Simple Components Schemas: `XML Schema elements and types defined in the “basic_types.xsd” and “simple_components.xsd” schema files implement all classes defined respectively in the “Basic Types” and “Simple Components” UML packages.`

From the Basic Types and Simple Components, we rely on the Quantity and Category Elements. 
While the Count Element would also be applicable, for the moment we handle Counts as Quantities.

## SWE:DataRecord
SWE:DataRecord, derived from the SWE Common AbstractDataComponent, can be used to group multiple components via the `field` attribute. 
Each field describes one band of the described Coverage.

![grafik](https://github.com/FAIRiCUBE/data-requests/assets/11915304/f943b189-cc85-4ccf-a39e-d85cad4a3e6f)



