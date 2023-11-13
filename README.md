# Data Requests

Data needed by the Use Cases will be imported into the FAIRiCUBE HUB to form datacubes. These make data accesseasier as they are homogenized in structure and access (if you ever had to go through different data repositories and harvest data, followed by own homogenization work, you will see that pushing that work "behind the curtain" by automating access is a big advantage). Of course, in order to provide data in such a "beautified" manner the homogenization work still needs to be done by somebody. In FC, that is: us. Tools like the data request form and the rasdaman ETL suite assist greatly, but for the final homogenized datacubes human caring hands are still necessary given the vast divergence of data; improving life of data wranglers is a key mission of the project, actually.

## How to Get Data Added

### Modeling

Typically, data have space and often, but not always, a time dimension. A special case is the Drosophila cube which has further dimensions which are neither spatial nor temporal.

### Data

Please hand in your requests for data to be made available within FAIRiCUBE HUB by simply adding an issue in this repository; this will add your request to the queue.

**Make sure the description is correct and complete, otherwise iterations and misinterpretations can occur which lead to delays and extra effort.**

If questions remain open (and this has turned out to be the regular case) a request clearing meeting will be held subsequently. Commonly, details can be clarified this way, or the data requestor gets asked to provide more technical details on the data. After successful data import the requestor will be contacted for verification, after which the git issue gets closed.

### Coverage Naming Conventions

For now, a pragmatic convention has been adopted: the coverage name is a combination of campaign year, reference year, inventory year and release version:
- [Mapping_Campaign]_[CLC_Reference_Year]_[Created_Inventory_Year]_[Version]


Stable version example with name CLC2006_CLC2000_V2018_20 means:
-	CLC2006_ 	That the file came from the 2006 mapping campaign (the file content was last modified in this campaign)
-	_CLC2000_ 	That the file captures Land Cover mapping results for 2000 reference year
-	_V2018_		That this file comes from a delivery created in 2018 inventory year
-	_20		That this is the final stable version


Beta-version example with name CLC2006_CLC2000_V2018_20b2 means:
-	CLC2006_ 	That the file came from the 2006 mapping campaign (the file content was last modified in this campaign)
-	_CLC2000_ 	That the file captures Land Cover mapping results for 2000 reference year
-	_V2018_		That this file comes from a delivery created in 2018 inventory year
-	_20b2		That this is the second beta-version


### Metadata

In order to become visible to all, the new data set also needs to get its twin entry in the catalog (currently: one of  https://catalog.eoxhub.fairicube.eu and https://catalog.fairicube.eu). To this end, the catalog team needs to get contacted (best via mentioning them in the corresponding data upload issue). Note that the catalog typically will require additional descriptive metadata.

[Here](encoding-examples/dominant_leaf_type-metadata.xml) is an example of a metadata record compliant with the OGC coverage standard.

## Finding data

### Listing contents

Services support a direct listing, however not necessarily with the convenience of the planned catalog:

- rasdaman datacubes: [get list of datacubes](http://fairicube.rasdaman.com:8080/rasdaman/ows?&SERVICE=WCS&ACCEPTVERSIONS=2.0.1&REQUEST=GetCapabilities) (requires authentication) - beware: OGC-compliant XML document, search for "CoverageSummary" 
- EOX: (tbd)

### Catalogs

A [list of data catalogs](../../wiki/Data-Catalogs) can be found in the Wiki. Please add data catalogs that are not on the list yet if you feel they are relevant as sources. Note, however, that this does not constintute a data request: no import action is associated with that list per se.

## Limitations

Time stamps have a peculiar mechanics on several datacubes which is not yet supported by rasdaman. Therefore, the time axis for now has ben modelled as an index (Cartesian) axis, meaning that temporal access (such as with the TIME parameter in WMS 1.3) is not yet possible. Full temporal support will become available still within 2023.
