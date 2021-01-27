import requests
import json

url = "http://192.168.1.37:80/ins"
username = "cisco"
password = "cisco"

myheader = {"content-type": "application/json"}
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show cdp nei",
        "output_format": "json",
    }
}
response = requests.post(
    url,
    data=json.dumps(payload),
    headers=myheader,
    auth=(username, password),
    verify=False,
).json()

print(json.dumps(response, indent=2, sort_keys=True))

### LOGIN WITH NX-API REST #########

auth_url = `https://192.168.1.37/api/mo/aaaLogin.json`
auth_body = {"aaaUser": {"attributes" : {"name": username, "pwd": password}}}

auth_response = requests.post(auth_url,body=json.dumps(auth_body),timeout=5,verify=False).json()
token = auth_response['imdata'][0]['aaaLogin']