import time
from app.sessions import *

def check_agent_training(admin_token, admin_xsrf_token, admin_larevel_token, admin_larevel_session, agent_id, agent_uuid):
    while True:
        URL = "https://tcl.twin24.ai/nlu/nlp/agent_train_queue/read/"
    
        payload = f"uuid={agent_uuid}"
        
        headers = {
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie" : f"XSRF-TOKEN={admin_xsrf_token}; io=none; laravel_session={admin_larevel_session}; laravel_token={admin_larevel_token}; token={admin_token}; sessionid=none",
            "User-Agent" : user_agent,
            "Authorization": f"Bearer {admin_token}"
        }
    
        res = session_12.post(URL, headers=headers, data=payload)
        res_json = res.json()
        
        result_uuid = res_json['data']['result_uuid']
        
        if res.status_code == 200:
            if result_uuid is not None:
                return True
            else:
                time.sleep(60)
                pass
        else:
            pass