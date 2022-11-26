Manege-Tool
===========
Tool to help with the assignment the different teachers to the trainigs, with regard to their disciplines and preferences.

Written by Tim Wisotzki for the ASVZ Manege_
adapted by Daniel Meier for processing nuudel polls instead of doodle

Features
--------
* divide teachers into disciplines
* assign them according to preferences into 'want' and 'can' teach
* automaticly prepares basic document and enters information
* easy configurations of in and output directories
* automaticly finds and processes files according to configuration


.. role:: bash(code)
   :language: bash


Installation
------------
1. load project from github_
2. recommended: setup virtual environment
3. install requirements :bash:`$ pip install -r requirements.txt`


Usage
-----
1. download/export polls from nuudel_ as csv-file (\*.csv)
2. store the file(s) in the directory specified in the config file (default is "./polls/")
3. run the tool :bash:`$ python main.py`
4. the program writes the prepared documents into the output directory specified in the config file (default is "./assignments/")


Licence
-------
* GNU GLPv3_


Further Information
-------------------
Further information can be found in the docs directory of the Project.

.. _Manege: https://asvz.ch/sport/45680-manege
.. _github: https://github.com/danteme/Manege-Tool
.. _nuudel: https://nuudel.digitalcourage.de/
.. _GLPv3: https://www.gnu.org/licenses/gpl-3.0.txt
