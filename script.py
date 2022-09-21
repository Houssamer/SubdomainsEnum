import requests
import sys

with open('/home/rhuser/tryhackme/scripting/wordlist2.txt') as sub_list:
    subdomains = sub_list.read().splitlines()
    for subdomain in subdomains:
        sub = f"http://{subdomain}.{sys.argv[1]}"

        try:
            requests.get(sub)

        except requests.ConnectionError:
            pass
        else:
            print("Valid subdomain: ", sub)
