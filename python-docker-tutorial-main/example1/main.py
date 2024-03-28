import random
import requests
import os, re, logging, json
import sys
from bs4 import BeautifulSoup
from pathlib import Path
from kubernetes import client, config


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

def read_secret(namespace, secret_name):
    try:
        # Load in-cluster configuration
        config.load_incluster_config()

        # Initialize the core API client
        core_api = client.CoreV1Api()

        # Retrieve the secret
        secret = core_api.read_namespaced_secret(secret_name, namespace)
        
        # Access the secret data
        secret_data = secret.data
        
        # Decode and print the secret data
        for key, value in secret_data.items():
            decoded_value = value.decode('utf-8')
            print(f"Secret Key: {key}, Value: {decoded_value}")

    except client.rest.ApiException as e:
        print("Exception when calling CoreV1Api->read_namespaced_secret: %s\n" % e)

def main():
    print(f'Inside main..BEGIN..!')

    # Check if arguments are provided
    ''' if len(sys.argv) < 2:
        print("Usage: python script.py arg1 arg2 ...")
    
    # Print each argument
    print("Arguments provided:")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Argument {i}: {arg}")
     '''
    # Usage example:
    namespace = "chand-infosec-dev" # Project name here
    '''
     OR TRY 
     # Load kubeconfig file
    config.load_kube_config()
    # Get the current context
    current_context = config.list_kube_config_contexts()[1]  # 1 corresponds to the index of the current context
    # Get the namespace from the current context
    namespace = current_context['context']['namespace']
    print("Current namespace:", namespace)
    '''
    secret_name = "cxtenantsecretsnew"
    print(f' From OPenShift Secrets: ' +  secret_name + ' === ' + read_secret(namespace, secret_name))


    tenant, oauth_id, oauth_secret = load_secrets()

    print(f'tenant :' + tenant)
    print(f'oauth_id : ' + oauth_id)
    print(f' : ' + oauth_secret)

    print(f'Inside main..END..!')

if __name__ == '__main__':
    main()
