# Data Requests

This space is used for issues and documentation (until a canonical documentation place has been defined) of data ingestion as part of Fairicube WP5 work.

In a nutshell, data needed by the Use Cases will be imported into the FAIRiCUBE HUB to form datacubes. These make data access easier as they are homogenized in structure and access (if you ever had to go through different data repositories and harvest data, followed by own homogenization work, you will see that pushing that work "behind the curtain" by automating access is a big advantage). Of course, in order to provide data in such a "beautified" manner the homogenization work still needs to be done by somebody. In FC, that is: us. Tools like the data request form and the rasdaman ETL suite assist greatly, but for the final homogenized datacubes human caring hands are still necessary given the vast divergence of data; improving life of data wranglers is a key mission of the project, actually.

Contents of this space:

- [How to Get Data Added](https://github.com/FAIRiCUBE/data-requests/wiki/How-to-Add-Data)
- [Choosing the right pixel type](https://github.com/FAIRiCUBE/data-requests/wiki/Choosing-the-Right-Pixel-Type)
- [Finding data ingested, datacube access how-to](https://github.com/FAIRiCUBE/data-requests/wiki)
- [Use case specific modeling and access](https://github.com/FAIRiCUBE/data-requests/wiki/Data-Overview)

As data ingest is tightly connected with metadata management, use of data, etc., consider also these related spaces:

- [resource-metadata](https://github.com/FAIRiCUBE/resource-metadata): in addition to the issues providing metadata for resources, also used to discuss technical details on resource metadata
- [Fairicube Hub](https://github.com/FAIRiCUBE/FAIRiCUBE-Hub-issue-tracker): for general FAIRiCUBE topics

-----

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
 



