from app.sessions import *
from app.new_snapshot import snapshot

def get_info_script(super_token, super_refresh_token, script, cabinet, super_xsrf_token):
    from app.update_cookies import cookies_update
    global get_script_info_called
    URL = f"https://bot.twin24.ai/api/v1/bots/{script}?fields=id,name,companyId"
    
    payload = {}
    headers = {
        "Authorization": f"Bearer {super_token}",
        "User-Agent": user_agent,
        "Content-Length" : "0"}
    
    res = session_3.get(URL, headers=headers, data=payload, timeout=100)
    
    try:
        res_json = res.json()
    
        script_id = res_json.get('id')
        name = res_json.get('name')
        companyId = res_json.get('companyId')
    except:
        cookies_update(super_token, super_refresh_token, script, cabinet)
    
    cookies_dict = [{"domain" : key.domain, 
                     "name" : key.name, 
                     "path" : key.path, 
                     "value" : key.value} for key in session_3.cookies]
    for cookies in cookies_dict:
        session_4.cookies.set(**cookies)
    
    if not get_script_info_called:
        get_script_info_called = True
        print(f'[Status {res.status_code}] {companyId} | {name} | {script_id}')
    
    if res.status_code == 200:
        snapshot(super_token, super_refresh_token, script, cabinet, super_xsrf_token, name)
    else:
        cookies_update(super_token, super_refresh_token, script, cabinet)