# Web API Parsing
## This is a submission for the Focusrite engineering placement test

I chose to complete this task using Python 3.6. 

The only additional dependency is the [requests library](https://docs.python-requests.org/en/latest/), which I have added to a requirements.txt 
file in this repo.

My code is split into 3 main functions, one to retrieve the contents hosted at https://api.ampifymusic.com/packs , one sort to sort the genres 
alphabetically then return them and one to return all the packs contained in the genre hip-hop. For each of these functions, I have written simple
unit tests. 

In order to improve testing of the parsing functions, I saved a copy of the JSON file from the API to be used in my tests.

### Compilation and running of code
To run both the tests and my script the python environment should have _requests_ installed in it

My script is in a single file called parser.py which can either be run directly from the source folder with ```./web_scraper.py``` or by explicitly calling 
python with ```python web_scraper.py```

The tests have been written and run using unit test but should also run fine with other testing libraries
