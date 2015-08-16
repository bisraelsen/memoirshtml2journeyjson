# Note
Before you proceed, it is good to work on an empty account in case you accidentally corrupt your Journey storage in Google Drive. If your Journey storage is corrupted, go to Drive Settings , find Journey and clear the in-app data.

# ID
The ID of an entry is in the format of
`UNIX_TIME_IN_MILLISEC-SIXTHEEN_RAND_CHARS.JSON`
The Random characters are limited to: a-z, A-Z, 0-9  

* Example of ID: 1413889453143-3fb32c66c4bd4cd0  
* Example of JSON file: 1413889453143-3fb32c66c4bd4cd0.JSON

# MEDIA
Only 1 media file is allowed to be attached to an entry.
The filename of a media is in the format of
`ID-SIXTHEEN_RAND_CHARS.FILE_EXT`
The Random characters are limited to: a-z, A-Z, 0-9  
The extensions are accepted: JPEG, JPG, BMP, GIF, PNG, WEBP, MP4, 3GP (case-insensitive)
* Example of Media filename: 1412653984567-3fc21e15f45bf4c4-6d222822b15b9062.JPG
* Remember to include the media filename into the `photos` array in the JSON file.

# JSON
The filename of a JSON is in the format of
`ID.JSON`

The format of JSON looks like this:
```
{"tags":[],"lon":144.96420277777779,"text":"# Melbourne\nMelbourne is a beautiful city especially at night.\nLook at the *night skyline*.  🏢🌟💗","music_artist":"","preview_text":"# Melbourne\nMelbourne is a beautiful city especially at night.\nLook at the *night skyline*.  🏢🌟💗","date_modified":1413170513031,"mood":1,"date_journal":1412653984567,"photos":["1412653984567-3fc21e15f45bf4c4-6d222822b15b9062.JPG"],"id":"1412653984567-3fc21e15f45bf4c4","address":"7 Riverside Quay, Southbank VIC 3006, Australia","music_title":"","weather":{"id":803,"icon":"04d","place":"Melbourne","degree_c":16.37,"description":"broken clouds"},"lat":-37.8214}
```

# Default Values
* lon: 1.7976931348623157E308
* music_artist: ""
* preview_text: limit to 512 OR length of text (whichever is minimum)
* date_modified, date_journal: Date in UNIX ms (13 digits)
* photos: []
* mood: 0
* address: ""
* music_title: ""
* id: ID has to be self-generated, and tally to JSON file name!
* weather.id: -1
* weather.icon: ""
* weather.place: ""
* weather.degree_c: 1.7976931348623157E308
* weather.description: ""
* lat: 1.7976931348623157E308
* tags: []
* text: ""

# Weather
Please follow the open weather codes [Link](http://openweathermap.org/weather-conditions). If the weather condition sunny day with broken clouds, then weather.id = 803, weather.icon = w01d, weather.description = "broken clouds". You can assume for weather condition if there is any missing information. Temperature is in degree celsius.

# ZIP Hierarchy  
ZIP filename should start with "Journey-" and end with ".zip"
All entries, including media files are stored in the same root folder.
Example:
```
|- ROOT
|---- 1413889453143-3fb32k66c4bd4fef.JSON
|---- 1413889453143-3fb32k66c4bd4fef-8f232e66c4r0dert.JPEG
|---- 1413889453145-4fb32e66c4rd43r4.JSON
|---- 1413889453147-gfb3jc66c4bd4bgh.JSON
|---- 1413889453149-1fbg2c66c4bd4bnm.JSON
|---- 1413889453152-9fv32c66c4bd4cvg.JSON
|---- 1413889453152-9fv32c66c4bd4cvg-55b32e66c4rd3333.MP4
...

```
