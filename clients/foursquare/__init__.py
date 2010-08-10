from autocheckin import settings
from google.appengine.api import urlfetch
import simplejson as json
import oauth2 as oauth
import urllib
import logging

class FoursquareClient(object):
    
    def __init__(self, token, secret):
        self._token = token
        self._secret = secret
    
    def _invoke(self, method, path, params=None):
        resource_url = "http://api.foursquare.com/v1/%s" % (path.lstrip('/'))
    
        token = oauth.Token(self._token, self._secret)
        consumer = oauth.Consumer(settings.foursquare_key, settings.foursquare_secret)
        oauth_request = oauth.Request.from_consumer_and_token(consumer, token, method, resource_url, params)
        oauth_request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, token)

        headers = {}
        headers.update(oauth_request.to_header())
        headers['user-agent'] = 'autocheckin'
        headers['content-type'] = 'application/json; charset=UTF-8'
        
        if params:
            resource_url = "%s?%s" % (resource_url, urllib.urlencode(params))
            
        response = urlfetch.fetch(url = resource_url, method = method, headers = headers, deadline=10)
        
        return json.loads(response.content)
    
    def history(self, limit = 20):    
        return self._invoke("GET", "/history.json", { 'l' : limit})

    def venues(self, lat, lng, limit = 10):    
        return self._invoke("GET", "/venues.json", { 'l' : limit, 'geolat' : lat, 'geolong' : lng})

    def checkin(self, vid, venue, shout, lat, lng, private = 0, twitter = 0, facebook = 0):    
        return self._invoke("POST", "/checkin.json", { 'vid' : vid, 'venue' : venue, 'shout' : shout, 'private' : private,  'twitter' : twitter,  'facebook' : facebook, 'geolat' : lat, 'geolong' : lng })
        
