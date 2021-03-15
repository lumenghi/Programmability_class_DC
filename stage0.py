import requests
import json

from utils.auth import IntersightAuth, get_authenticated_aci_session
from env import config

auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'],
                      api_key_id=config['INTERSIGHT_API_KEY'])

#https://intersight.com/apidocs/apirefs/api/v1/ntp/Policies/get/
BASE_URL='https://www.intersight.com/api/v1'

#NTP policies request
url_ntp = f"{BASE_URL}/ntp/Policies"

try:
    response = requests.get(url_ntp, auth=auth).json()
    for r in response['Results']:
        #print(r['AccountMoid'])
        print("The name of the policy is " + r['Name'] + " and the IP address of the NTP server is " + r['NtpServers'][0])
    print(json.dumps(response, indent=4))
except Exception as ex:
    print(ex)