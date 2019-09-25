import http.client
from authentication_helper import AuthenticationHelper

class OmfClient:

	http_client = None

	headers = {
	    'messagetype': "",
	    'messageformat': "json",
	    'omfversion': "1.1",
	    'action': "",
	    'content-type': "application/json",
	    'authorization': ""
    }

	def __init__(self, base_url, tenant_id, namespace_id, client_id, client_secret):
		self.base_url = base_url
		OmfClient.http_client = http.client.HTTPSConnection(self.base_url)
		self.authentication_helper = AuthenticationHelper(base_url, client_id, client_secret)
		self.omf_endpoint = "/api/tenants/" + tenant_id + "/namespaces/" + namespace_id + "/omf"

	def send_omf_message(self, messagetype, action, payload):	
	    OmfClient.headers["messagetype"] = messagetype
	    OmfClient.headers["action"] = action
	    OmfClient.headers["authorization"] = "Bearer " + self.authentication_helper.get_token()
	    self.http_client.request("POST", self.omf_endpoint, payload, OmfClient.headers)
	    result = self.http_client.getresponse()
	    data = result.read()
	    print(data.decode("utf-8"))