# Data Requests

This space is used for issues and documentation (until a canonical documentation place has been defined) of data ingestion as part of Fairicube WP5 work.

In a nutshell, data needed by the Use Cases will be imported into the FAIRiCUBE HUB to form datacubes. These make data access easier as they are homogenized in structure and access (if you ever had to go through different data repositories and harvest data, followed by own homogenization work, you will see that pushing that work "behind the curtain" by automating access is a big advantage). Of course, in order to provide data in such a "beautified" manner the homogenization work still needs to be done by somebody. In FC, that is: us. Tools like the data request form and the rasdaman ETL suite assist greatly, but for the final homogenized datacubes human caring hands are still necessary given the vast divergence of data; improving life of data wranglers is a key mission of the project, actually.

Contents of this space:

- [How to Get Data Added](https://github.com/FAIRiCUBE/data-requests/wiki/How-to-Add-Data)
- [Finding data ingested, datacube access how-to](https://github.com/FAIRiCUBE/data-requests/wiki)
- [Use case specific modeling and access](https://github.com/FAIRiCUBE/data-requests/wiki/Data-Overview)

As data ingest is tightly connected with metadata management, use of data, etc., consider also these related spaces:

- [resource-metadata](https://github.com/FAIRiCUBE/resource-metadata): in addition to the issues providing metadata for resources, also used to discuss technical details on resource metadata
- [Fairicube Hub](https://github.com/FAIRiCUBE/FAIRiCUBE-Hub-issue-tracker): for general FAIRiCUBE topics

-----

# Range Type

(this will go on a separate page later)

Responding to requirements phrased in the project the range type in coverages has been extended in rasdaman. As this is a new feature it is documented here to ease understanding and use.

Of particular interest are the components:

- **field name**: the record component name under which range values are known and can be extracted, such as `$c.red` in WCPS; this must follow the usual syntax conventions of program variable names
- **definition**: the technical data type (int, float, etc.), expressed through OGC URIs as OGC requires
- **description**: a human-readable text explaining the meaning
- **nil values**, as pairs of reason (some text) and a value (taken from the data type definition, see above)
- **unit of measure**: OGC has no guidance on this; earlier UCUM was used, but it appears inconvenient. In Fairicube QUDT seems preferred - more to come once agreed, stay tuned.

Importantly, datacubes (as data in general) fall into one of several different categories, as statistics teaches: *numerical*, *ordinal*, and *categorial*. SWE Common (upon which the coverage range type relies) supports that halfways, therefore an activity is planned to reflect these categories in a statistically correct way in the OGC/ISO coverage standards.

In XML, the complete range type structure is as in the following example:

```
<gmlcov:rangeType>
    <swe:DataRecord>
        <swe:field name="red">
            <swe:Quantity definition="http://www.opengis.net/def/dataType/OGC/0/unsignedByte">
                <swe:label>red</swe:label>
                <swe:description>Band 1 description</swe:description>
                <swe:nilValues>
                    <swe:NilValues>
                        <swe:nilValue reason="I don't know">25</swe:nilValue>
                    </swe:NilValues>
                </swe:nilValues>
                <swe:uom code="10^0"/>
            </swe:Quantity>
        </swe:field>
        <swe:field name="...">...</swe:field>
    </swe:DataRecord>
</gmlcov:rangeType>
```

Further, FC-specific metadata go into the metadata bag of the coverage. To this end, a separate schema has been developed with an FC schema location.

# FAIRiCUBE User Management

(this will go on a separate page later)

Once the F'Hub gets active it will offer a single entry to the data and services of the projcet. For their access control a common governance concept and its technical realization is needed, in particular in view of the two distinct, independent platform technology stacks of EOX and rasdaman.
This section is a (currently) living document for the evolution of the high-level governance rules and their lower-level implementation.

## Project Access Policy

- Entities under discussion: Data(cubes) (local on the projet store ore remotely linked in), (python) processing code, ML models
- Possible rights:
  - write: create a new object or modify an existing one
  - read: read out an object, ie: download it
  - use: make use of an object, but without getting direct access to it (eg, for IP protection on python code and models)
- Impact factors: project decisions, individual partner constraints (such as on federated data), 3rd party contributions (such as EEA data, models from HuggingFace, etc.)

Governance adopted: TODO
- ex: who has authority to manage access rights?
- ex: what roles, what rights?

## Implementation
### EOX User Management
- authentication: TODO
- authorization: TODO

### rasdaman User Management
- authentication: The rasdaman platform comes with built-in user/password management, but can tap into remote identity providers.
- authorization: Based on standard Role-based Access Control, rasdaman offers basic privileges over which roles can be created which can be assigned to named users. 

### Integration Approach
- system components requiring access protection: catalog, EOX data, rasdaman data
- questions to be resolved:
  - how to map the project governance model to the three components? Options:
    - central identity manager (who will setup and maintain?)
    - (simple) mapping to both models via a WebGUI? (who?)
    - manual mapping (undesirable)
  - implementation approach?
 



