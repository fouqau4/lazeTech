#!/usr/bin/python -tt

import json
import requests
import time
import webbrowser

with open('comics.json') as f:
    comics = json.load(f)

modified = False
chrome_app_path = '/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe'
while True:
    print 'check'

    for comic in comics:
        protocol = 'https://'
        url = 'www.comicbus.com/html/' + str(comic['comic_id']) + '.html'
        request = protocol + url

        response = requests.get(request, verify=False)

        while(True):
            pattern = str(comic['comic_id']) + '-' + \
                str(comic['newest'] + 1) + '.html'
            pos = response.content.find(pattern)

            if pos == -1:
                break
#			print comic['name'].encode('utf8') + ' is not updated.'
            else:
                comic['newest'] = comic['newest'] + 1
                print '[updated]' + comic['name'].encode('utf8') + '[' + str(comic['newest']) + '] is now available.'
                modified = True
                open_url = 'http://v.comicbus.com/online/comic-' + \
                    str(comic['comic_id']) + '.html?ch=' + \
                    str(comic['newest']) + ''
                webbrowser.Chrome(chrome_app_path).open_new_tab(open_url)

    if modified == True:
        with open('comics.json', 'w') as f:
            f.write(json.dumps(comics, indent=4))
        modified = False
    print 'END'
    break
