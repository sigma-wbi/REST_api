import os
import environ
from cryptography.fernet import Fernet
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))
key = env('FERNET_KEY')

fernet = Fernet(key)

with open(BASE_DIR/'logs/encrypt.txt', 'r') as f:
    wf = open(BASE_DIR/'logs/decrypt.json', 'w', encoding='utf8')

    lines = f.readlines()
    for line in lines:
        decrypt_str = fernet.decrypt(line)
        wf.write(decrypt_str.decode('utf8'))
    
    wf.close()
