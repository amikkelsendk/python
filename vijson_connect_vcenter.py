"""
SYNOPSIS
    Code sample on on how to connect to vCenter, create a VM snapshot and get Task status, via VIJSON REST API
DESCRIPTION
    Code sample on on how to connect to vCenter, create a VM snapshot and get Task status, via VIJSON REST API
NOTES
    Website:        www.amikkelsen.com
    Author:         Anders Mikkelsen
    Creation Date:  2024-09-10

    Code is created based om William Lam's Shell example and example from Broadcom
    - https://github.com/lamw/vmware-scripts/blob/master/shell/create_snapshot_for_vm.sh
    - https://developer.broadcom.com/xapis/virtual-infrastructure-json-api/latest/
    
    Latest supported 'vc_api_release' version can be found in the TOP RIGHT of https://developer.broadcom.com/xapis/virtual-infrastructure-json-api/latest/
"""

import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


## Variables ##
vcenter_fqdn    = '<vcenter ip or fqdn>'
username        = 'administrator@vsphere.local'
password        = '<password>'
userpass        = username + ':' + password
vc_api_release  = '8.0.2.0'
vm_id           = 'vm-123'                      # ID of VM


# Get Session Manager MoRef ID
url = f'https://{vcenter_fqdn}/sdk/vim25/{vc_api_release}/ServiceInstance/ServiceInstance/content'
response = requests.request( 'GET', url, verify=False )
if response.status_code == 200:
    session_manager_moid = ( response.json() )['sessionManager']['value']
    print( f'SESSION_MANAGER_MOID: {session_manager_moid}' )
else:
    print( response.status_code, response.text )



# Get auth Session ID
url = f'https://{vcenter_fqdn}/sdk/vim25/{vc_api_release}/SessionManager/{session_manager_moid}/Login'
auth_headers = {
    'Content-type': 'application/json'
}
payload = json.dumps(
    {
        'userName': username, 
        'password': password
    }
)
response = requests.request( 'POST', url, headers=auth_headers, data=payload, verify=False )
if response.status_code == 200:
    vijson_api_session_id = response.headers.get('vmware-api-session-id')
    print( f'VIJSON_API_SESSION_ID: {vijson_api_session_id}' )
else:
    print(response.status_code, response.text)


# Create new snapshot
url = f"https://{vcenter_fqdn}/sdk/vim25/{vc_api_release}/VirtualMachine/{vm_id}/CreateSnapshotEx_Task"
headers = {
    'vmware-api-session-id': vijson_api_session_id,
    'Content-type': 'application/json'
}
payload = json.dumps(
    {
        "name": "Snapshot 001",
        "description": "Snapshot taken by VIJSON REST API", 
        "memory": False
    }
)
response = requests.request( 'POST', url, headers=headers, data=payload, verify=False )
if response.status_code == 200:
    print( 'Snapshot requested' )
    if response.content:
        # Convert 'b' (bytes) to json (dict) -- https://stackoverflow.com/questions/40059654/convert-a-bytes-array-into-json-format
        snapshots_task = json.loads( ( response.content.decode('utf-8').replace("'", '"') ) )
        print( f'Task ID: { snapshots_task["value"] }' )
    else:
        print( 'Snapshot request failed' )
else:
    print(response.status_code, response.text)


# Get Task status
url = f'https://{vcenter_fqdn}/sdk/vim25/{vc_api_release}/Task/{ snapshots_task["key"] }/info'
headers = {
    'vmware-api-session-id': vijson_api_session_id,
    'Content-type': 'application/json'
}
response = requests.request( "GET", url, headers=headers, verify=False )
if response.status_code == 200:
    # Convert 'b' (bytes) to json (dict) -- https://stackoverflow.com/questions/40059654/convert-a-bytes-array-into-json-format
    task = json.loads( ( response.content.decode('utf-8').replace("'", '"') ) )
    print( f'Task status: { task["state"] }' )
elif response.status_code == 500:
    print('Task complete or deleted')
    print(response.text)
else:
    print(response.status_code, response.text)
