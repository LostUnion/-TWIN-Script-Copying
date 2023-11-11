import requests
from fake_useragent import UserAgent

session_1 = requests.Session()
session_2 = requests.Session()
session_3 = requests.Session()
session_4 = requests.Session()
session_5 = requests.Session()
session_6 = requests.Session()
session_7 = requests.Session()
session_8 = requests.Session()
session_9 = requests.Session()
session_10 = requests.Session()
session_11 = requests.Session()
session_12 = requests.Session()
session_13 = requests.Session()

user_agent = UserAgent().random

update_cookies_called = False
get_script_info_called = False