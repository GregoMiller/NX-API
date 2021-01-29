import requests
import json
import re

url = "http://192.168.1.37/ins"
username = "cisco"
password = "cisco"

myheaders = {"content-type": "application/json"}
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
response = requests.post(url, data=json.dumps(
    payload), headers=myheaders, auth=(username, password), verify=False).json()

print(json.dumps(response, indent=2, sort_keys=True))

### LOGIN WITH NX-API REST #########

auth_url = 'https://192.168.1.37/api/mo/aaaLogin.json'
auth_body = {"aaaUser": {"attributes" : {"name": username, "pwd": password}}}

auth_response = requests.post(auth_url, data=json.dumps(auth_body), timeout=5, verify=False).json()
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']
cookies = {}
cookies['APIC-cookie'] = token

headers = {"content-type": "application/json"}

print(token)

counter = 0

nei_count = response['ins_api']['outputs']['output']['body']['neigh_count']
print(nei_count)

while counter < nei_count:
    hostname = response['ins_api']['outputs']['output']['body'][
        'TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['device_id']
    local_int = response['ins_api']['outputs']['output']['body'][
        'TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['intf_id']
    # print(local_int)
    remote_int = response['ins_api']['outputs']['output']['body'][
        'TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info'][counter]['port_id']
    #OUTPUT COPIADO DE SHOW CDP NEI CON REST CONFIG https://{{h}}/api/node/mo/sys/intf/phys-[eth1/1].json

    body = {
        "l1PhysIf":{
            "attributes":{
                "descr": 'Connected to '+hostname+' Remote if is '+remote_int
            }
        }
    }

    counter += 1
    print (hostname)

    if local_int != 'mgmt0': 
        int_name = str.lower(str(local_int[:3]))
        int_num = re.search(r'[1-9]/[1-9]*', local_int)
        int_url = 'https://192.168.1.37/api/mo/sys/intf/phys-['+int_name+str(
            int_num.group(0))+'].json'
        post_response = requests.post(int_url, data=json.dumps(
            body), headers=headers, cookies=cookies, verify=False).json()
        print(post_response)

   body2 ¿ 
               "l1PhysIf": {
                "attributes": {
                    "accessVlan": "vlan-1",

#{
#  "aaaUser":{
#   "attributes":{
#      "name":"georgewa",
#      "pwd":"paSSword1"
#    }
#  }ww
#}