from google.appengine.api import urlfetch
import settings
import simplejson as json
import oauth2 as oauth
import urllib
import logging

class LatitudeClient(object):
    
    realm = 'http://*.kenneth.io'
    
    def __init__(self, token, secret):
        self._token = token
        self._secret = secret
    
    def _invoke(self, path, params=None):
        resource_url = "https://www.googleapis.com/latitude/v1/%s" % (path.lstrip('/'))
    
        token = oauth.Token(self._token, self._secret)
        consumer = oauth.Consumer(settings.latitude_key, settings.latitude_secret)
        oauth_request = oauth.Request.from_consumer_and_token(consumer, token, 'GET', resource_url, params)
        oauth_request.sign_request(oauth.SignatureMethod_HMAC_SHA1(), consumer, token)

        headers = {}
        headers.update(oauth_request.to_header(realm = realm))
        headers['user-agent'] = 'python-latitude'
        headers['content-type'] = 'application/json; charset=UTF-8'
        
        if params:
            resource_url = "%s?%s" % (resource_url, urllib.urlencode(params))
            
        response = urlfetch.fetch(url = resource_url, method = urlfetch.GET, headers = headers)
        
        return json.loads(response.content)
    
    def current_location(self):    
        return self._invoke("/currentLocation", {'granularity': 'best'})

