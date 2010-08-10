import settings
import oauth2 as oauth
import client
import logging

access_token = 'something'
access_secret = 'sccchh'

client = client.LatitudeClient(access_token, access_secret)
currentLocation = client.current_location()