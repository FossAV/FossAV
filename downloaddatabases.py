# clone https://github.com/Pyran1/MalwareDatabase and put it in db/db1
import urllib.request
import urllib.parse
import urllib.error
import json
import os
import sys
import time
import hashlib
import zipfile
import shutil
import sqlite3
import sqlite3.dbapi2 as sqlite
import datetime
# create db folder
if not os.path.exists('db'):
    os.makedirs('db')
# clone the repo to db/db1
if not os.path.exists('db/db1'):
    os.system('git clone https://github.com/Pyran1/MalwareDatabase db/db1')
# copy the avlib.py to db/db1/avlib.py
if not os.path.exists('db/db1/avlib.py'):
    shutil.copyfile('avlib.py', 'db/db1/avlib.py')
