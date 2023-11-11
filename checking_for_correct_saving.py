import time
import json
from sessions import *
from requests.exceptions import RequestException
from agent_train import agent_training

def correct_saving(super_token, super_refresh_token, script, cabinet, super_xsrf_token, name, uuid, new_botId, admin_user_id, email_user, admin_token, admin_refresh_token, admin_xsrf_token):
    URL = f"https://bot.twin24.ai/api/v1/bots/{new_botId}?fields=id,name,companyId,agents,nodes"
    
    payload = {}
    headers = {
        'User-Agent': user_agent,
        "Authorization" : f"Bearer {admin_token}"}
    
    res = session_10.get(URL, headers=headers, data=payload, timeout=5)
    
    print(res.cookies)
    res_json = res.json()
    agent_uuid = res_json.get("agents")
    
    cookies_dict = [{"domain" : key.domain, 
                     "name" : key.name, 
                     "path" : key.path, 
                     "value" : key.value} for key in session_10.cookies]
    for cookies in cookies_dict:
        session_11.cookies.set(**cookies)
        
    if res.status_code == 200:
        for agent_id in agent_uuid:
            print(f"[Status {res.status_code}] Starting agent {agent_id} Training")
            time.sleep(2)
            agent_training(super_token, super_refresh_token, script, cabinet, super_xsrf_token, name, uuid, new_botId, admin_user_id, email_user, admin_token, admin_refresh_token, admin_xsrf_token, agent_id)

    
    