from app.sessions import *
from app.waiting_for_a_new_script import check_script

def shift_snapshot(super_token, cabinet, super_xsrf_token, name, uuid):
    URL = f"https://tcl.twin24.ai/superadmin/scripts/snapshot/new/company/{uuid}"
    
    payload = {'company_id' : cabinet}
    headers = {
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json;charset=UTF-8",
        "User-Agent": user_agent,
        "x-xsrf-token": super_xsrf_token,
        "Authorization": f"Bearer {super_token}"}
    res = session_5.post(URL, headers=headers, json=payload, timeout=1000)
    
    res_json = res.json()
    new_botId = res_json.get('id')
    
    cookies_dict = [{"domain" : key.domain, 
                     "name" : key.name, 
                     "path" : key.path, 
                     "value" : key.value} for key in session_5.cookies]
    for cookies in cookies_dict:
        session_6.cookies.set(**cookies)
    
    print(f'[Status {res.status_code}] [~] Copying the script "{name}" to the cabinet {cabinet}...')
    check_script(super_token, cabinet, super_xsrf_token, name, new_botId)
    