HEADERS = {
    'content-type': 'application/x-www-form-urlencoded'
}

latitude_key = ''
latitude_secret = ''

latitude_request_token_url = 'https://www.google.com/accounts/OAuthGetRequestToken?scope=https://www.googleapis.com/auth/latitude'
latitude_authorize_url = 'https://www.google.com/latitude/apps/OAuthAuthorizeToken?domain=autocheckin.appspot.com&granularity=best&location=all'
latitude_access_token_url = 'https://www.google.com/accounts/OAuthGetAccessToken'
