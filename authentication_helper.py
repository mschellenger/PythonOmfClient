import requests
import datetime

class AuthenticationHelper:

	identity_suffix = "/identity/connect/token"

	def __init__(self, base_url, client_id, client_secret):
		self.base_url = base_url
		self.client_id = client_id
		self.client_secret = client_secret
		self.request_data = {
			"grant_type":"client_credentials",
			"client_id":client_id,
			"client_secret":client_secret
		}
		self.access_token = ""
		self.expiry = 0
		self.last_refresh_time = (datetime.datetime.now() - datetime.timedelta(hours = 6))

	def get_token(self):
		if (self.access_token == "" or self.cached_token_expired()):
			self.refresh_token()
		return self.access_token

	def refresh_token(self):
		url = "https://" + self.base_url + AuthenticationHelper.identity_suffix
		response = requests.post(url, self.request_data).json()
		self.access_token = response['access_token']
		self.expiry = response['expires_in']

	def cached_token_expired(self):
		return (datetime.datetime.now() - datetime.timedelta(seconds = self.expiry)) > self.last_refresh_time