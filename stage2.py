import requests
import json

from utils.auth import IntersightAuth, get_authenticated_aci_session
from env import config

# Credentials below are for the always-on sandbox
# config['ACI_BASE_URL'] = "https://sandboxapicdc.cisco.com"
# user = config['ACI_USER'] =
# pw = config['ACI_PASSWORD']

aci_session = get_authenticated_aci_session(config['ACI_USER'], config['ACI_PASSWORD'], config['ACI_BASE_URL'])


if aci_session is not None:
    print("ACI access verified")
else:
    print("Failed")

#https://hostname/api/node/mo/uni/tn-3tierapp.xml?query-target=self&rsp-subtreeinclude=health
base_url = 'https://intersight.com/api/v1'
endpointA="/api/class/fabricHealthTotal"

try:
    response = requests.get(url).json()
    print(json.dumps(response, indent=4))
except Exception as ex:
    print(ex)