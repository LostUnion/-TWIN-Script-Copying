import time
from app.sessions import *
from app.agent_train import agent_training

def correct_saving(new_botId, admin_token, admin_xsrf_token, admin_larevel_token, admin_larevel_session):
    URL = f"https://bot.twin24.ai/api/v1/bots/{new_botId}?fields=id,name,companyId,agents,nodes"
    
    payload = {}
    headers = {
        'User-Agent': user_agent,
        "Authorization" : f"Bearer {admin_token}"
    }
    
    res = session_10.get(URL, headers=headers, data=payload, timeout=5)
    
    res_json = res.json()
    agents = res_json.get("agents")
    
    script_name = res_json.get("name")
    company_id = res_json.get("companyId")
    
    cookies_dict = [{"domain" : key.domain, 
                     "name" : key.name, 
                     "path" : key.path, 
                     "value" : key.value} for key in session_10.cookies]
    
    for cookies in cookies_dict:
        session_11.cookies.set(**cookies)
        
    if res.status_code == 200:
        if agents is not None:
            agent = len(agents)
            if agent == 0:
                print(f'[Status {res.status_code}] There are no agents in the script')
                print(f'Сценарий "{script_name}" скопирован в ЛК {company_id}.')
            elif agent != 0:
                print(f'[Status {res.status_code}] {agent} agents were found in the script')
                for agent_id in agents:
                    print(f"[Status {res.status_code}] Agent {agent_id} training started")
                    agent_training(admin_token, admin_xsrf_token, admin_larevel_token, admin_larevel_session, agent_id)
                print(f'[Status {res.status_code}] All agents are trained!')
                print(f'Сценарий "{script_name}" скопирован в ЛК {company_id}.')
            else:
                print(f'Сценарий "{script_name}" скопирован в ЛК {company_id}.')
