import time
import json
from sessions import *
from requests.exceptions import RequestException

def check_agent_training(admin_token, admin_xsrf_token, agent_id):
    while True:
        URL = "https://tcl.twin24.ai/nlu/nlp/agent_train_queue/read/"
    
        payload = f"uuid={agent_id}"
        headers = {
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json;charset=UTF-8',
            'User-Agent': user_agent,
            'x-xsrf-token': admin_xsrf_token,
            'Authorization': f'Bearer {admin_token}'
        }
    
        res = session_12.post(URL, headers=headers, data=payload)
        print(f"[+] {res.status_code}")
        
        if res.status_code == 200:
            return f"[Status {res.status_code}] Agent {agent_id} is trained!"
        if res.status_code == 404:
            time.sleep(10)
            pass