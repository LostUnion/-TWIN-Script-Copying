import time
import json
from sessions import *
from requests.exceptions import RequestException
from checking_agent_traing import check_agent_training

def agent_training(super_token, super_refresh_token, script, cabinet, super_xsrf_token, name, uuid, new_botId, admin_user_id, email_user, admin_token, admin_refresh_token, admin_xsrf_token, admin_larevel_token, admin_larevel_session, agent_id):
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
        print(f"[Status {res.status_code}] Agent {agent_id} training started")
        return check_agent_training(super_token, super_refresh_token, script, cabinet, super_xsrf_token, name, uuid, new_botId, admin_user_id, email_user, admin_token, admin_refresh_token, admin_xsrf_token, admin_larevel_token, admin_larevel_session, agent_id, agent_uuid)
    else:
        print(res.status_code)





# 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'Accept': '*/*',
                # 'Sec-Fetch-Site': 'same-origin',
                # 'Accept-Language': 'en-GB,en;q=0.9',
                # 'Accept-Encoding': 'gzip, deflate, br',
                # 'Sec-Fetch-Mode': 'cors',
                # 'Host': 'tcl.twin24.ai',
                # 'Origin': 'https://tcl.twin24.ai',
                # 'Content-Length': '47',
                # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
                # 'Referer': 'https://tcl.twin24.ai/nlu/',
                # 'Connection': 'keep-alive',
                # 'Sec-Fetch-Dest': 'empty',
                # 'X-Requested-With': 'XMLHttpRequest',
                # 'Cookie': f'XSRF-TOKEN={admin_xsrf_token}; io=none; laravel_session={admin_larevel_session}; laravel_token={admin_larevel_token}; token={admin_token}; sessionid=none',
                # 'Authorization': f'Bearer {admin_token}'