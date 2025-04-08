import requests
import streamlit as st


auth = requests.auth.HTTPBasicAuth(st.secrets['UserID']['UserID'], st.secrets['reddit_secret']['secret'])

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': st.secrets['username']['username'],
        'password': st.secrets['password']['password']}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'scraper/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
# print(res.json())

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
# res = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

# get 5 new posts from wallstreetbets
params = {'limit': 5}
res = requests.get("https://oauth.reddit.com/r/wallstreetbets/new", headers=headers, params=params)
print(res.json())