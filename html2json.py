from bs4 import BeautifulSoup
import sys
import json
import datetime
import re
import random

def unix_time(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    delta = dt - epoch
    return delta.total_seconds()

def unix_time_millis(dt):
    return int(unix_time(dt) * 1000.0)

#fname = sys.argv[1]
#output = sys.argv[2]

fname = 'test_memories.html'

with open (fname, "r") as myfile:
    data=myfile.readlines()

for line in data:
    if line.startswith('\t<p>&nbsp;</p>\t'):
        entryJSON = {}
        line_soup = BeautifulSoup(line,'html.parser')

        dateText = line_soup.select('p.sDateCreated')[0].getText()
        dateTime = datetime.datetime.strptime(dateText, '%A, %B %d, %Y at %H:%M')
        milli = unix_time_millis(dateTime)
        entryJSON['date_journal'] = milli
        entryJSON['date_modified'] = milli + 1000*120 #two minutes

        entryJSON['address'] = 'testing'

        entryJSON['music_artist'] = ''
        entryJSON['music_title'] = ''

        entryText =  line_soup.select('span.sNote')[0].getText('\n\n',strip=True)
        entryJSON['text'] = entryText

        if len(entryText) > 25:
            prevEnd = 25
        else:
            prevEnd = len(entryText)
        entryJSON['preview_text']=entryText[0:prevEnd]

        entryJSON['mood']=0

        entryJSON['photos'] = []

        # get list of tags, lowercase
        tagText = line_soup.select('span.sTags')[0].getText().lower().split(',')
        tags = [x.strip() for x in tagText]
        if len(tags) > 0:
            entryJSON['tags'] = tags
        else:
            entryJSON['tags'] = []

        geoText = line_soup.select('p.sLocation')[0].get_text('&&').split('&&')
        entryJSON['weather']={'id':-1, 'icon':'','place':'','degree_c':1.7, 'description':''}
        # if len(geoText) > 8:
        #     addrText = geoText[1]
        #     lat, lon, ele = [float(x) for x in geoText[3].replace(',',' ').replace('alt:',' ').replace('m','').split()]
        #     entryJSON['lat'] = lat * 10**4
        #     entryJSON['lon'] = lon * 10**4
        #     weatherText = geoText[5]
        #     degC = float(weatherText.split()[0].replace('C',''))
        #     desc = weatherText.split()[1]
        #     entryJSON['weather']={'degree_c':degC, 'description':desc }


        import random
        randKey = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(16))
        entryJSON["id"] = str(milli) + '-' + randKey
        with open('output/'+entryJSON['id']+'.json', 'w') as outfile:
            json.dump(entryJSON, outfile, sort_keys=True)
