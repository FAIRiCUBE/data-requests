# Data Requests

Data needed by the Use Cases will be imported into the FAIRiCUBE HUB to form datacubes. These make data accesseasier as they are homogenized in structure and access (if you ever had to go through different data repositories and harvest data, followed by own homogenization work, you will see that pushing that work "behind the curtain" by automating access is a big advantage). Of course, in order to provide data in such a "beautified" manner the homogenization work still needs to be done by somebody. In FC, that is: us. Tools like the data request form and the rasdaman ETL suite assist greatly, but for the final homogenized datacubes human caring hands are still necessary given the vast divergence of data; improving life of data wranglers is a key mission of the project, actually.

## How to Get Data Added

### Modeling

Typically, data have space and often, but not always, a time dimension. A special case is the [Drosophila cube](#Drosophila) which has further dimensions which are neither spatial nor temporal.

### Data

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

## Finding data

### Listing contents

Services support a direct listing, however not necessarily with the convenience of the planned catalog:

- rasdaman datacubes: [get list of datacubes](http://fairicube.rasdaman.com:8080/rasdaman/ows?&SERVICE=WCS&ACCEPTVERSIONS=2.0.1&REQUEST=GetCapabilities) (requires authentication) - beware: OGC-compliant XML document, search for "CoverageSummary" 
- EOX: (tbd)

### Catalog

An easy way to browse datasets available is the catalog  [catalog]((https://catalog.fairicube.eu/). Note that it is still under development and catching up with the datasets available.

## Limitations

- Time stamps have a peculiar mechanics on several datacubes which is not yet supported by rasdaman. Therefore, the time axis for now has ben modelled as an index (Cartesian) axis, meaning that temporal access (such as with the TIME parameter in WMS 1.3) is not yet possible. Full temporal support will become available still within 2023.
- Due to minor misalignments of the OGC standards some facets of the XML schemas do not validate. However, with most tools this is not an issue when using data.


## How-to

In this section we give a brief introduction to datacube wrangling. First, terminology: In standardization world, datacubes are modeled by "coverages". Most relevant are the OGC Coverage Implementation Schema (CIS) as the data model and Web Coverage Service (WCS) as the processing model, containing the Web Coverage Processing Service (WCPS) datacube analytics language. So don't be surprised to see "coverages" mentioned below.

We first present a general overview on standards-based datacube access, and then provide some use-case specific examples. If you want to see further examples added, [contact us](mailto:pbaumann@constructor.university)!

### General

#### Coverages

Coverages are designed to be self-describing. While always more metadata can be added to some object, the coverage contains the essentials for understanding the pixels. The canonical structure of a coverage consists of

-	domain set: where can I find values?
-	range set: the values.
-	range type: what do the values mean?
-	metadata: what else should I know about these data?

Coverages can be encoded in a variety of data formats. Text formats include XML, JSON, and RDF; binary formats include GeoTIFF, NetCDF, and Grib2.

See [this tutorial](https://earthserver.eu/wcs/#cis) for more details on CIS.

#### Coverage Access

The Web Coverage Service (WCS), in its current version 2.1, defines access in a user-selected encoding, spatio-temporal subsetting, scaling, reprojection, as well as processing (see next section). Such Web requests are expressed as http GET or POST requests as this example (using fairicube rasdaman) shows (whitespace only for an easier read, not part of the request):

'''
https://fairicube.rasdaman.com/rasdaman/ows
    ? SERVICE=WCS & VERSION=2.1.0 & REQUEST=GetCoverage
 		& SUBSET=date( "2018-05-22" ) 
 		& SUBSET=E( 332796 : 380817 )
 		& SUBSET=N( 6029000 : 6055000 )
    & FORMAT=image/png
'''

As per OGC syntax, date/time strings need to be quoted.

Note that http requires certain characters to be ["URL-encoded"](https://www.urlencoder.io/) before submission; browsers often do that automatically, but not programmatically generated requests.

See [this tutorial](https://earthserver.eu/wcs/#wcs) for more details on WCS.

#### Coverage Processing

WCPS allows processing, aggregation, fusion, and more on datacubes with a high-level, easy-to-use language which does not require any programming skills like python. The following example inspects coverage A and returns a cutout with a range extent expressed in Easting and Northing (assuming this is the native coordinate reference system of the coverage) and a slice at a time point, returned in PNG format:

'''
for $c in ( A )
return
 	encode( $c [	date( "2018-05-22" ), ( 332796 : 380817 ), N( 6029000 : 6055000 ) ], "png" )
'''

Such a query can be sent through the WCS Processing request:

'''
https://fairicube.rasdaman.com/rasdaman/ows
    ? SERVICE=WCS & VERSION=2.1.0 & REQUEST=ProcessCoverages
 		& QUERY=for $c in ( A ) return encode( $c [	date( "2018-05-22" ), ( 332796 : 380817 ), N( 6029000 : 6055000 ) ], "png" )
   '''

Again, be reminded that ["http URL-encoding"](https://www.urlencoder.io/) needs to be applied before sending.

So far, each coverage has been processed in isolation. Data fusion is possible through “nested loops”:

'''
for	$a in ( A ), $b in ( B )
return encode( $a + $b, "png" )
'''

Aggregation plays an important role for reducing the amount of data transported to the client. With the common aggregation operators – in WCPS called “condensers” – queries like the following are possible (note that no format encoding is needed, numbers are returned in ASCII):

'''
for $a in ( A )
return max( $a )
'''

As a final example, the following WCPS query com¬putes the Inverted Red-Edge Chlorophyll Index (IRECI) on a selected space / time region, performs contrast reduction for visualization, and delivers the result reprojected to EPSG:4326:

'''
for	$c in (S2_L2A_32633_B07_60m),
  	$d in (S2_L2A_32633_B04_60m),
  	$e in (S2_L2A_32633_B05_60m),
  	$f in (S2_L2A_32633_B06_60m)
let $sub := [ date("2018-05-22"), E(332796:380817), N(6029000:6055000) ]
return
 	encode(
 		crsTransform(
 			( $c - $d ) / ( $e / $f ) [ $sub ],
 			{ E: " EPSG:4326", N: “EPSG:4326” }
 		) / 50,  
 		"png"
 	)
'''

See [this tutorial](https://earthserver.eu/wcs/#wcps) for more details on WCPS.

### ML Use Case

tbd

### Drosophila Use Case

tbd - [Corresponding data request issue](issues/86) 
