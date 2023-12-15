# Data Requests

This space is used for issues and documentation (until a canonical documentation place has been defined) of data ingestion as part of Fairicube WP5 work.

As data ingest is tightly connected with metadata management, use of data, etc., consider also these related spaces:

- [resource-metadata](https://github.com/FAIRiCUBE/resource-metadata): in addition to the issues providing metadata for resources, also used to discuss technical details on resource metadata
- [Fairicube Hub](https://github.com/FAIRiCUBE/FAIRiCUBE-Hub-issue-tracker): for general FAIRiCUBE topics

In a nutshell, data needed by the Use Cases will be imported into the FAIRiCUBE HUB to form datacubes. These make data access easier as they are homogenized in structure and access (if you ever had to go through different data repositories and harvest data, followed by own homogenization work, you will see that pushing that work "behind the curtain" by automating access is a big advantage). Of course, in order to provide data in such a "beautified" manner the homogenization work still needs to be done by somebody. In FC, that is: us. Tools like the data request form and the rasdaman ETL suite assist greatly, but for the final homogenized datacubes human caring hands are still necessary given the vast divergence of data; improving life of data wranglers is a key mission of the project, actually.

Contents of this space:

- [How to Get Data Added](#how-to-get-data-added)
- [Further details](https://github.com/FAIRiCUBE/data-requests/wiki) like finding data, datacube access how-to, and use case specific modeling and access


## How to Get Data Added

Please hand in your requests for data to be made available within FAIRiCUBE HUB by simply [adding an issue](https://github.com/FAIRiCUBE/data-requests/issues/new/choose) in this repository; this will add your request to the queue. You need to provide the agreed slate of description elements so that data can be downloaded, understood, and the datacube can be created.

**Make sure the description is correct and complete, otherwise iterations and misinterpretations can occur which lead to delays and extra effort on all sides.**

If questions remain open (and this has turned out to be the regular case) a request clearing meeting will be held subsequently. Commonly, details can be clarified this way, or the data requestor gets asked to provide more technical details on the data. After successful data import the requestor will be contacted for verification, after which the git issue gets closed.

### Coverage Naming Conventions

Ultimately, the catalog of the FAIRiCUBE hub will allow convenient search across data. For now, until this catalog becomes available, a pragmatic convention has been adopted: the coverage name is a combination of campaign year, reference year, inventory year and release version:
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


