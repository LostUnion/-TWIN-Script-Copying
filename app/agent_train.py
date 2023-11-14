from app.sessions import *
from app.checking_agent_traing import check_agent_training

def agent_training(admin_token, admin_xsrf_token, admin_larevel_token, admin_larevel_session, agent_id):
    URL = "https://tcl.twin24.ai/nlu/nlp/agent/train/"
    
    payload = f"agent_uuid={agent_id}"
    headers = {
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie" : f"XSRF-TOKEN={admin_xsrf_token}; io=none; laravel_session={admin_larevel_session}; laravel_token={admin_larevel_token}; token={admin_token}; sessionid=none",
        "User-Agent" : user_agent,
        "Authorization": f"Bearer {admin_token}"
        }
    
    res = session_11.post(URL, headers=headers, data=payload, timeout=1000)
    
    res_json = res.json()
    agent_uuid = res_json['data']['uuid']
    
    cookies_dict = [{"domain" : key.domain, 
                     "name" : key.name, 
                     "path" : key.path, 
                     "value" : key.value} for key in session_11.cookies]
    
    for cookies in cookies_dict:
        session_12.cookies.set(**cookies)
        
    if res.status_code == 200:
        return check_agent_training(admin_token, admin_xsrf_token, admin_larevel_token, admin_larevel_session, agent_id, agent_uuid)
    else:
        print(res.status_code)
