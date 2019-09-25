from omf_client import OmfClient
from authentication_helper import AuthenticationHelper
from container_message import Container
from data_point import DataPoint
from data_message import DataMessage
import datetime
import json
import jsonpickle

base_url = ""
tenant_id = ""
namespace_id = ""
type_id = ""
stream_id = ""

client_id = ""
client_secret = ""

omf_client = OmfClient(base_url, tenant_id, namespace_id, client_id, client_secret)

def send_type(omf_client):
	with open('parse_simple_test_type.json', 'r') as type_file:
		payload = type_file.read();
	omf_client.send_omf_message("type", "create", payload)

def send_container(omf_client):
	container_message = Container(stream_id, type_id)
	payload = jsonpickle.encode([container_message], unpicklable=False)
	print(payload)
	omf_client.send_omf_message("container", "create", payload)

def send_values(omf_client):
	value = 0
	while (True):
		value+=1
		data_point = DataPoint(datetime.datetime.now(), value)
		data_message = DataMessage(stream_id, [data_point])
		payload = jsonpickle.encode([data_message], unpicklable=False)
		omf_client.send_omf_message("data", "create", payload)

send_type(omf_client)
send_container(omf_client)
send_values(omf_client)