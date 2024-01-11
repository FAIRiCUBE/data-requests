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

- field name: the record component name under which range values are known and can be extracted, such as `$c.red` in WCPS; this must follow the usual syntax conventions of program variable names
- definition: the technical data type (int, float, etc.), expressed through OGC URIs as OGC requires
- description: a human-readable text explaining the meaning
- nil values, as pairs of reason (some text) and a value (taken from the data type definition, see above)
- unit of measure: OGC has no guidance on this; earlier UCUM was used, but it appears inconvenient. In Fairicube QUDT seems preferred - more to come once agreed, stay tuned.

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
