import requests
import json

# Set URL to post to and declare authorization header
# Auth header will expire and need to be replaced after some time
url = 'http://localhost:9999/api/pepper/add'
headers = {'Authorization' : '<PASTE HEADER HERE>', 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
fileName = 'pepperList.json'
arrayName = 'peppers'

# Open pepperList.json to iterate through objects
with open(fileName) as data_file:
    json_file = json.load(data_file)

    # For each pepper
    for arrayItem in json_file[arrayName]:

        # Convert to json form
        temp = json.dumps(arrayItem)

        # Print json object to console
        print(temp)

        # Send a post request to the url with the specified json as data and with the appropriate headers
        r = requests.post(url, data=temp, headers=headers)

        # Print response code to console
        print(r)
