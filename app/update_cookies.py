import time
from app.sessions import *
from app.get_script_info import get_info_script

def cookies_update(super_token, super_refresh_token, script, cabinet):
    global update_cookies_called
    URL = "https://tcl.twin24.ai/"

    payload = {}
    headers = {
        "User-Agent": user_agent,
        "Authorization" : f"Bearer {super_token}"}

    res = session_2.get(URL, headers=headers, data=payload, timeout=100)
    super_xsrf_token = res.cookies.get('XSRF-TOKEN')
        
    cookies_dict = [{"domain" : key.domain, 
                     "name" : key.name, 
                     "path" : key.path, 
                     "value" : key.value} for key in session_2.cookies]
    for cookies in cookies_dict:
        session_3.cookies.set(**cookies)
    
    if not update_cookies_called:
        update_cookies_called = True
        print(f'[Status {res.status_code}] Update Cookies')
        
    time.sleep(3)
    get_info_script(super_token, super_refresh_token, script, cabinet, super_xsrf_token)