# coding: utf-8

import urllib
import urllib2
import json
import time
import tweet as tw

url = 'https://itunes.apple.com/search?term=pokemon+go&country=jp&media=software&entity=software&lang=ja_jp'
def func():
    while True:
        try:
            r = urllib2.urlopen(url)
            root = json.loads(r.read())
            for data in root['results']:
                if u'Niantic, Inc.' in data[u'sellerName']:
                    print "Gotcha!"
                    tw.tweet()
                    return
            print "has not been released yet in Japan"
        finally:
            r.close()
        time.sleep(30.0)

func()
