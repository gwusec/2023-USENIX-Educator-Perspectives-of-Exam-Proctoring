
# Scripts used in this project

This document outlines the scripts directory structure and describes each of the scripts used. 



## Directory Structure:
* __quantitative-analysis__ : Scripts used to analyze Likert response questions and perform additional exploratory analysis.
	* 2021-educator.Rmd  - R script to generate the tables and figures used in the paper.

* __qualitative-analysis__ : Scripts used as part of the qualitative analysis
	* irr.py  - Inter-rater reliability script used to calculate Cohen's Kappa for inter-coder agreement 


## Running the scripts
In general the scripts are written with the assumption that they will be run 
from within the local directory in which they reside rather than from the project's home directory.
(For example to run `2021-educator.Rmd` starting from this directory you will need to:
```
#move to the quantitave-analysis folder
cd quantitative-analysis

#Run the script from there
Rscript -e "rmarkdown::render(2021-educator.Rmd)"
```
