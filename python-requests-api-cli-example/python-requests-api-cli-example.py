import requests # it is an external module, use `pip install requests`
import json
import os

accountId = os.environ['DOPPLERRELAY_ACCOUNT_ID']
apikey = os.environ['DOPPLERRELAY_APIKEY']

url = 'http://api.dopplerrelay.com/accounts/' + accountId + '/messages'

data = {
    'from_name': 'Your Name',
    'from_email': 'test@example.com',
    'recipients': [
        {
            'type': 'to',
            'email': 'test@example.com',
            'name': 'Test Recipient'
        }
    ],
    'subject': 'Testing Doppler Relay',
    'html': '<strong>Doppler Relay</strong> is great!'  
}

headers = {
    'Authorization': 'token ' + apikey,
    'Content-type': 'application/json'
}

req = requests.post(url, data=json.dumps(data), headers=headers)

print(req.text)

req.raise_for_status()