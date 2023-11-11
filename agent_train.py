import time
import json
from sessions import *
from requests.exceptions import RequestException
from checking_agent_traing import check_agent_training

def agent_training(super_token, super_refresh_token, script, cabinet, super_xsrf_token, name, uuid, new_botId, admin_user_id, email_user, admin_token, admin_refresh_token, admin_xsrf_token, agent_id):
    URL = "https://tcl.twin24.ai/nlu/nlp/agent/train/"
    
    payload = f"agent_uuid={agent_id}"
    headers = {
        "User-Agent": user_agent,
        "Authorization": f"Bearer {admin_token}"
        }
    
    res = session_10.post(URL, headers=headers, data=payload, timeout=1000)
    print(res.status_code)
    print(res.content)
    print(res.headers)
    
    cookies_dict = [{"domain" : key.domain, 
                     "name" : key.name, 
                     "path" : key.path, 
                     "value" : key.value} for key in session_11.cookies]
    
    for cookies in cookies_dict:
        session_12.cookies.set(**cookies)
        
    if res.status_code == 200:
        print(f"[Status {res.status_code}] Agent {agent_id} training started")
        return check_agent_training(admin_token, admin_xsrf_token, agent_id)
    else:
        print(res.status_code)
