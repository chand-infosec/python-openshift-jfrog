import random
import requests
import os, re, logging, json
import sys
from bs4 import BeautifulSoup
from pathlib import Path

# crawl IMDB Top 250 and randomly select a movie

URL = 'http://www.imdb.com/chart/top'



def get_secret_path():
    tree = "run/secrets"
    default = f"/{tree}"

    if os.path.exists(default):
        return default
    elif os.path.exists(f"./{tree}"):
        return f"./{tree}"
    else:
        return "."
    

def load_secrets():
    path = get_secret_path()

    tenant = None
    with open(Path(path) / "cxone_tenant", "rt") as f:
        tenant = f.readline()

    oauth_id = None
    with open(Path(path) / "cxone_oauth_client_id", "rt") as f:
        oauth_id = f.readline()

    oauth_secret = None
    with open(Path(path) / "cxone_oauth_client_secret", "rt") as f:
        oauth_secret = f.readline()

    return (tenant, oauth_id, oauth_secret)

def main():
    print(f'Inside main..BEGIN..!')

    # Check if arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python script.py arg1 arg2 ...")

    # Print each argument
    print("Arguments provided:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Argument {i}: {arg}")
        
    tenant, oauth_id, oauth_secret = load_secrets()

    print(f'tenant :' + tenant)
    print(f'oauth_id : ' + oauth_id)
    print(f' : ' + oauth_secret)

    print(f'Inside main..END..!')

if __name__ == '__main__':
    main()
