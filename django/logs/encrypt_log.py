import os
import environ
from cryptography.fernet import Fernet
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))
key = env('FERNET_KEY')

fernet = Fernet(key)

with open(BASE_DIR/'logs/log.json', 'r', encoding='utf8') as f:
    wf = open(BASE_DIR/'logs/encrypt.txt', 'w')

    lines = f.readlines()
    for line in lines:
        encrypt_str = fernet.encrypt(f'{line}'.encode('utf8'))
        wf.write(encrypt_str.decode('utf8')+'\n')
    
    wf.close()
