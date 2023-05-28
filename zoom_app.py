import requests
from flask import Flask, request

app = Flask(__name__)

# OAuth 2.0 Configuration
CLIENT_ID = 'THBngT8TR0CSE19Qm1dv1Q'
CLIENT_SECRET = 'CN2LYNoMiKcx6dWaAbhLaN2U60ZCNDKO'
REDIRECT_URI = 'http://localhost:5000/zoom/callback'


@app.route('/zoom/authorize')
def authorize():
    # Redirect the user to the Zoom authorization URL
    authorization_url = f'https://zoom.us/oauth/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}'
    return redirect(authorization_url)


@app.route('/zoom/callback')
def callback():
    # Exchange the authorization code for an access token
    code = request.args.get('code')
    token_url = 'https://zoom.us/oauth/token'
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI
    }
    response = requests.post(token_url, data=data)
    access_token = response.json()['access_token']

    # Store the access_token securely for future use

    return 'Authorization successful!'


@app.route('/zoom/event', methods=['POST'])
def event_handler():
    event = request.json

    # Handle meeting.ended event
    if event['event'] == 'meeting.ended':
        meeting_id = event['payload']['object']['id']

        # Retrieve the meeting transcript
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        transcript_url = f'https://api.zoom.us/v2/meetings/{meeting_id}/recordings/transcripts'
        response = requests.get(transcript_url, headers=headers)
        transcript = response.json()

        # Process the transcript and generate the meeting recap
        ### PLACEHOLDER ###
        ### PLACEHOLDER ###
        ### PLACEHOLDER ###
        ### PLACEHOLDER ###
        ### PLACEHOLDER ###

    return 'Event received'


if __name__ == '__main__':
    app.run()

