import ipdb
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
    # add on some random milliseconds to the end so we don't get exact matches
    return int(unix_time(dt) * 1000.0) + random.randint(0,1000)

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

        randKey = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(16))

        entryJSON['date_journal'] = milli
        entryJSON['date_modified'] = milli + 1000*120 #two minutes
        id = str(milli) + '-' + randKey
        entryJSON['id'] = id

        entryJSON['music_artist'] = ''
        entryJSON['music_title'] = ''

        entryText =  line_soup.select('span.sNote')[0].getText('\n\n',strip=True).replace('"','\"')
        entryJSON['text'] = entryText

        if len(entryText) > 512:
            prevEnd = 512
        else:
            prevEnd = len(entryText)
        entryJSON['preview_text']=entryText[0:prevEnd]

        entryJSON['mood']=0

        entryJSON['photos'] = []

        # get list of tags, lowercase and no spaces
        tagText = line_soup.select('span.sTags')[0].getText().lower().split(',')
        tags = [x.strip().replace(' ','') for x in tagText]

        if len(tags) > 1:
            entryJSON['tags'] = tags
        else:
            if tags[0] == '':
                entryJSON['tags'] = []
            else:
                entryJSON['tags'] = tags

        geoText = line_soup.select('p.sLocation')[0].get_text('&&').split('&&')

        entryJSON['address'] = geoText[1]

        # deafult weather information
        entryJSON['weather']={'id':-1, 'icon':'','place':'','degree_c':1.7976931348623157E308, 'description':''}
        entryJSON['lat'] = 1.7976931348623157E308
        entryJSON['lon'] = 1.7976931348623157E308

        # If there is data for weather, lat/lon etc..
        if len(geoText) == 8:
            lat, lon, ele = [float(x) for x in geoText[3].replace(',',' ').replace('alt:',' ').replace('m','').split()]

            entryJSON['lat'] = lat * 10**4
            entryJSON['lon'] = lon * 10**4

            weatherText = geoText[5]
            degC = float(weatherText.split()[0].replace('C',''))
            s_ind = weatherText.find('C')
            e_ind = weatherText.find(',')
            desc = weatherText[s_ind+1:e_ind].strip().lower()

            entryJSON['weather']['degree_c'] = degC
            entryJSON['weather']['description'] = desc

        with open('output/'+id+'.json', 'w') as outfile:
            json.dump(entryJSON, outfile, sort_keys=True, indent=2)
