# Geo_event-QA

This is a part of Geo-event QA project used to demonstrate the sysnthesis functionality provided by APE (the Automated Pipeline Explorer) for answering geo-event questions. 

This includes:

APE software (.jar)

config.json: configuration files

constraints.json: constraint files 

GeoTaxonomy.rdf: a combined ontology of CCD ontology and tool onotlogy based on geooperator categories.

GeooperatorsAnnotation.json: the tool annotation file as input to APE.

solutions.txt: solution workflows in the text format

GroupingEqWfs-Intensional.py : Grouping equivalent workflows using intensional approach


## Installation
In order to run the synthesis using APE-1.17.jar Java 1.8 or higher should be installed on the system.

## Runing the program

In order to execute the synthesis you should run the following command:

java -jar APE-<version>-executable.jar [path_to_ape_configuration_file]

The results of the synthesis would be:
Spec1/sat_solutions.txt	-	First X candidate solutions in textual format
Spec1/Figures/		-	Data-flow figures corresponding to the first X solutions

For more information see APE GitHub repo (https://github.com/sanctuuary/APE/) or APE readme page (https://ape-framework.readthedocs.io/en/latest/).

