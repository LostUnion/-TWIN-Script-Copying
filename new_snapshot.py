import time
import json
from sessions import *
from requests.exceptions import RequestException
from move_snapshot import shift_snapshot

def snapshot(super_token, super_refresh_token, script, cabinet, super_xsrf_token, name):
    from update_cookies import cookies_update
    URL = f"https://tcl.twin24.ai/superadmin/scripts/snapshot/new/{script}"
    
    payload = {'comment' : name}
    headers = {
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json;charset=UTF-8",
        "User-Agent": user_agent,
        "x-xsrf-token": super_xsrf_token,
        "Authorization": f"Bearer {super_token}"}
    
    res = session_4.post(URL, headers=headers, json=payload, timeout=1000)
    StatusCode = res.status_code
    
    if StatusCode == 201:
        res_json = res.json()
        uuid = res_json.get('uuid')

        cookies_dict = [{"domain" : key.domain,
                         "name" : key.name,
                         "path" : key.path,
                         "value" : key.value} for key in session_4.cookies]
        for cookies in cookies_dict:
            session_5.cookies.set(**cookies)

        print(f'[Status {res.status_code}] [+] A new snapshot has been created')
        shift_snapshot(super_token, super_refresh_token, script, cabinet, super_xsrf_token, name, uuid)
    else:
        cookies_update(super_token, super_refresh_token, script, cabinet)