# Manege-Tool

Tool to help with the assignment the different teachers to the trainigs, with regard to their disciplines and preferences.

Originally written by Tim Wisotzki for the [ASVZ Manege](https://asvz.ch/sport/45680-manege),
adapted by Daniel Meier for processing nuudel polls instead of doodle

## Features

* divide teachers into disciplines
* assign them according to preferences into 'want' and 'can' teach
* automaticly creacte assigment template per training day with teachers prefernces
* easy configuration of in and output directories
* automaticly finds and processes files according to configuration

## Installation

1. load project from [github](https://github.com/danteme/Manege-Tool)
2. recommended: setup virtual environment
3. install requirements: `$ pip install -r requirements.txt`

## Usage

1. Go to your poll on [nuudel](https://nuudel.digitalcourage.de/) and select "Deutsch" as the language 
2. Press the "CSV-Export" button and download the poll as csv-file (*.csv)
3. store the poll in the directory specified in the config file (default is "./polls/")
4. run the tool `$ python main.py`
5. the tool creates the assignment template into the output directory specified in the config file (default is "./assignments/")


## Licence

* GNU [GLPv3](https://www.gnu.org/licenses/gpl-3.0.txt)


## Further Information

Further information can be found in the docs directory of the Project.

* Manege: https://asvz.ch/sport/45680-manege
* github: https://github.com/danteme/Manege-Tool
* nuudel: https://nuudel.digitalcourage.de/
* GLPv3: https://www.gnu.org/licenses/gpl-3.0.txt
