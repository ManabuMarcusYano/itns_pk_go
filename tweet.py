# coding: utf-8
from requests_oauthlib import OAuth1Session
import json

def tweet():
    twitter = OAuth1Session("rWu5MoGW0aT7HFXOmIUSQ", client_secret="aLt0csvuVYnEbu5Q9pASCFe56GQfQwn71dOlNYoe7Y", resource_owner_key="78032372-3dIBcXJj1Keqh7GaSwVLCgH9NSf1OWvORypPC8YY", resource_owner_secret="LiiUW7UjVDIbvzKNButSOQCYiOX2gl00yVFS3SRQs")
    params = {"status": u"日本でついにPokemon Goがリリースされたっぽい! @DJ_YANOS @SkYk929 http://goo.gl/Srf35Z http://goo.gl/n9ive7"}
    req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params=params)
    print req.status_code
