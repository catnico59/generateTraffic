import requests
import time
import random
import numpy as np

from pinger import pinger
from scrapper import *

urls_to_ping = [
    'https://codepen.io/',
]
clear_proxies()
if clear_proxies():
    get_array_proxies()
    cleaning_proxies()
    pinger(urls_to_ping)

if pinger(urls_to_ping) == 42:
    print("CLEANING PROXIES REQUIRED")
    clear_proxies()
