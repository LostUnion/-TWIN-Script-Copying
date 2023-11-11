import argparse
from authentication import auth
import chromedriver_autoinstaller


if not chromedriver_autoinstaller.get_chrome_version():
    chromedriver_autoinstaller.install()
else:
    pass

def primary_function(login, password, script, cabinet):
    auth(login, password, script, cabinet)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Copying a script from a superadmin')
    parser.add_argument('-l', '--login', type=str, required=True, help='Your superuser login from the Twin cabinet')
    parser.add_argument('-p', '--password', type=str, required=True, help='Your superuser password from the Twin cabinet')
    parser.add_argument('-s', '--script', type=str, help='ID of the script to copy')
    parser.add_argument('-c', '--cabinet', type=int, help='ID of the cabinet to copy the script to')
    
    args = parser.parse_args()
    primary_function(args.login,
                     args.password,
                     args.script,
                     args.cabinet)