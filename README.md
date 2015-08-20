# memoirshtml2journeyjson
### Under Construction!!

Utility to convert from memoirs html output to json output used in Journey

# Requirements
* Python3
* BeautifulSoup4 (this might be useful [link](http://stackoverflow.com/questions/26511791/ubuntu-how-to-install-a-python-module-beautifulsoup-on-python-3-3-instead-of) )
* json
* datetime

# The Basics
* `html2json.py` is the script that you need to run. Currently the information is hardcoded, but it will accept command line arguments after it is proven to work.

* Currently it is looking for the folder `output` in the base directory to put the .json files in. You will need to create that folder by hand.

Also, it does not do anything with attached media right now. This is because Memoirs allows storage of multiple images/videos/recordings per entry while Journey only allows 1 image/video. Doing this in an automatic fashion would likely not please people and should be done by hand for now.
