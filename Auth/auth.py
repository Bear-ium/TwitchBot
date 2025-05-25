# app.py
from flask import Flask, redirect, request, session, url_for
from dotenv import load_dotenv
import requests
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = 'http://localhost:8080/callback'
SCOPES = 'chat:read chat:edit'

@app.route('/')
def home():
    return '''
        <h1>Twitch OAuth Login</h1>
        <a href="/login">Log in with Twitch</a>
    '''

@app.route('/login')
def login():
    return redirect(
        f"https://id.twitch.tv/oauth2/authorize"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope={SCOPES}"
    )

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return 'No code provided', 400

    token_url = 'https://id.twitch.tv/oauth2/token'
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URI,
    }

    response = requests.post(token_url, data=data)
    if response.status_code != 200:
        return f"Error getting token: {response.text}", 500

    token_info = response.json()
    access_token = token_info.get('access_token')

    return f'''
        <h2>OAuth Token Received</h2>
        <p><b>Access Token:</b> {access_token}</p>
        <p>Copy this and use it in your bot code as <code>oauth:{access_token}</code></p>
    '''

if __name__ == '__main__':
    app.run(port=8080)
