import requests
import time
import random
import numpy as np
from scrapper import *

urls_to_ping = [
   'https://codepen.io/',
]

##get_array_proxies()
cleaning_proxies()

with open('user-agents.txt', "r") as f:
    user_agent = f.read().splitlines()

with open('proxies', "r") as f:
    proxies = f.read().splitlines()
    proxies_sorted = sorted(set(proxies))

with open('output.txt', "r") as f:
    lastcycle = int(f.read().splitlines()[-1])

for ip in proxies_sorted:
    for url_counter in urls_to_ping:
        header = {'User-Agent': user_agent[random.randint(0, len(user_agent))]}
        try:
            response = requests.get(url_counter, proxies={'https': f"http://{ip}"}, headers=header, timeout=20)
        except:
            response = "errors requests"
            pass
        lastcycle += 1

        with open("output.txt", "a") as file:
            result = f"\n{lastcycle}"
            file.write(str(result))

        print(f"Cycle n°{lastcycle}: {response}")
        ##time.sleep(random.randint(1, 80))
