import requests
import time
import random
import numpy as np
from scrapper import *

def pinger(urls_to_ping):
    with open('user-agents.txt', "r") as f:
        user_agent = f.read().splitlines()

    with open('proxies', "r") as f:
        proxies = f.read().splitlines()
        proxies_sorted = sorted(set(proxies))

    try:
        with open('output.txt', "r") as f:
            lastcycle = int(f.read().splitlines()[-1])
    except:
        lastcycle = 1

    daytime = 86400
    rest_of_time = 86400
    randomised = daytime / len(proxies_sorted)
    print (randomised)
    for ip in proxies_sorted:
        for url_counter in urls_to_ping:
            header = {'User-Agent': user_agent[random.randint(0, len(user_agent))]}
            try:
                response = requests.get(url_counter, proxies={'https': f"http://{ip}"}, headers=header, timeout=20)
            except:
                response = "Errors requests"
                pass
            lastcycle += 1

            with open("output.txt", "a") as file:
                result = f"Cycle n°{lastcycle}: {response}\n"
                file.write(str(result))

            print(f"Cycle n°{lastcycle}: {response}")

            random_number = random.randint(1, round(randomised))
            print(random_number)
            time.sleep(random.randint(1, int(random_number)))
            rest_of_time = rest_of_time - int(random_number)
            print(rest_of_time)
    time.sleep(rest_of_time)
    return 42
