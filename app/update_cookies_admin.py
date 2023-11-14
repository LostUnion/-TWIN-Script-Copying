from app.sessions import *
from app.opening_a_script_for_saving import script_saving

def admin_cookies_update(new_botId, email_user, admin_token):
    
    URL = "https://tcl.twin24.ai/"
    
    payload = {}
    headers = {
        'User-Agent': user_agent,
        "Authorization" : f"Bearer {admin_token}"}
    
    res = session_9.get(URL, headers=headers, data=payload, timeout=5)
    admin_xsrf_token = res.cookies.get('XSRF-TOKEN')
    admin_larevel_token = res.cookies.get('laravel_token')
    admin_larevel_session = res.cookies.get('laravel_session')
    
    cookies_dict = [{"domain" : key.domain,
                     "name" : key.name,
                     "path" : key.path,
                     "value" : key.value} 
                    for key in session_9.cookies]
    
    for cookies in cookies_dict:
            session_10.cookies.set(**cookies)
    
    
    print(f'[Status {res.status_code}] Updating the cookies of the administrator {email_user}')
    script_saving(new_botId, admin_token, admin_xsrf_token, admin_larevel_token, admin_larevel_session)
    
