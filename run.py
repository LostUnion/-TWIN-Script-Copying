import argparse
from app.authentication import auth
from app.database import db_start
import chromedriver_autoinstaller


if not chromedriver_autoinstaller.get_chrome_version():
    chromedriver_autoinstaller.install()
else:
    pass

def primary_function(script, cabinet):
    db_start()
    auth(script, cabinet)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Copying a script from a superadmin')
    parser.add_argument('-s', '--script', type=str, help='ID of the script to copy')
    parser.add_argument('-c', '--cabinet', type=int, help='ID of the cabinet to copy the script to')
    
    args = parser.parse_args()
    primary_function(args.script,
                     args.cabinet)