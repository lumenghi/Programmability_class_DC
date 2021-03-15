import requests
import json

from utils.auth import IntersightAuth
from env import config

privatekey=config['INTERSIGHT_CERT']
publickey=config['INTERSIGHT_API_KEY']

auth=IntersightAuth(secret_key_filename=privatekey, api_key_id=publickey)

base_url = 'https://intersight.com/api/v1'
endpoint = '/cond/Alarms'

try:
    response = requests.get(url=f"{base_url}{endpoint}", auth=auth)
    if response.status_code==200:
        response_json = json.loads(response.text)
        print("---------------Alarms--------------")
        for name in response_json["Results"]:
            print(name["Name"])
            print(name["Description"])
            print("\n")
except Exception as ex:
    print(ex)


endpoint2="/compute/PhysicalSummaries"
try:
    response = requests.get(url=f"{base_url}{endpoint2}", auth=auth)
    if response.status_code==200:
        response_json = json.loads(response.text)
        print("---------------Physical Infrastructure--------------")
        for name in response_json["Results"]:
            print(name["ManagementMode"])
            print(name["MgmtIpAddress"])
            print(name["Name"])
            print(name["NumCpus"])
            print(name["NumCpuCores"])
            print(name["OperPowerState"])
            print(name["Firmware"])
            print(name["Model"])
            print(name["Serial"])
            print(name["SharedScope"])
except Exception as ex:
    print(ex)


endpoint3="/hcl/CompatibilityStatuses"
try:
    response = requests.get(url=f"{base_url}{endpoint3}", auth=auth)
    if response.status_code==200:
        response_json = json.loads(response.text)
        print("---------------Hardware Compatibility List--------------")
        for name in response_json["Results"]:
            print(name["OsVendor"])
            print(name["OsVersion"])

except Exception as ex:
    print(ex)



endpoint4="/kubernetes/Clusters"
try:
    response = requests.get(url=f"{base_url}{endpoint4}", auth=auth)
    if response.status_code==200:
        response_json = json.loads(response.text)
        print("---------------Hardware Compatibility List--------------")
        for name in response_json["Results"]:
            print(name["Name"])

except Exception as ex:
    print(ex)


endpoint5="/kubernetes/Deployments"
try:
    response = requests.get(url=f"{base_url}{endpoint5}", auth=auth)
    print(response.status_code)
    if response.status_code==200:
        response_json = json.loads(response.text)
        num=0
        print("---------------Hardware Compatibility List--------------")
        for name in response_json["Results"]:
            num=num+1
        print(f"The number of the Kubernetes deployments is {num}")

except Exception as ex:
    print(ex)