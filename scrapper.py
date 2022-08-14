import time

import requests
from bs4 import BeautifulSoup

scraped_urls = [
    'https://proxyhub.me/fr/be-free-proxy-list.html',
    'https://proxyhub.me/fr/fr-free-proxy-list.html',
    'https://proxyhub.me/en/fr-free-proxy-list.html',
    'https://proxyhub.me/fr/be-free-proxy-list.html',
    'https://proxyhub.me/fr/fr-free-proxy-list.html',
    'https://proxyhub.me/en/fr-free-proxy-list.html',
    'https://proxyhub.me/fr/be-free-proxy-list.html',
    'https://proxyhub.me/fr/fr-free-proxy-list.html',
    'https://proxyhub.me/en/fr-free-proxy-list.html',
    'https://proxyhub.me/fr/be-free-proxy-list.html',
    'https://proxyhub.me/fr/fr-free-proxy-list.html',
    'https://proxyhub.me/en/fr-free-proxy-list.html',
    'https://proxyhub.me/fr/be-free-proxy-list.html',
    'https://proxyhub.me/fr/fr-free-proxy-list.html',
    'https://proxyhub.me/en/fr-free-proxy-list.html',
    'https://proxyhub.me/fr/be-free-proxy-list.html',
    'https://proxyhub.me/fr/fr-free-proxy-list.html',
    'https://proxyhub.me/en/fr-free-proxy-list.html',
    'https://proxyhub.me/fr/be-free-proxy-list.html',
    'https://proxyhub.me/fr/fr-free-proxy-list.html',
    'https://proxyhub.me/en/fr-free-proxy-list.html',
    'https://proxyhub.me/fr/be-free-proxy-list.html',
    'https://proxyhub.me/fr/fr-free-proxy-list.html',
    'https://proxyhub.me/en/fr-free-proxy-list.html',
    'https://proxyhub.me/fr/be-free-proxy-list.html',
    'https://proxyhub.me/fr/fr-free-proxy-list.html',
    'https://proxyhub.me/en/fr-free-proxy-list.html',
]


def get_array_proxies():
    counter = 0
    for url in scraped_urls:
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, "lxml")
        data = []
        gdp_table = soup.find("table", attrs={"class": "table"})
        rows = gdp_table.find_all('tr')

        for tr in rows[1:]:
            data.append([td.get_text(strip=True) for td in tr.find_all('td')])

        for row in data:
            ip = row[0]
            port = row[1]

            with open("proxies", "a") as proxies:
                proxies.write(str(ip + ":" + port + "\n"))

        counter += 1
        time.sleep(2)
        print("WAITING SCRAPPING : Procress " + str(counter) + " requests on " + str(len(scraped_urls)))
    return


def cleaning_proxies():
    with open('proxies', "r") as file:
        proxies = file.read().splitlines()
        proxies_sorted = []
        for i in proxies:
            if i not in proxies_sorted:
                proxies_sorted.append(i)
        file.close()

    with open('proxies', "w") as file:
        for proxie in proxies_sorted:
            file.write("%s\n" % proxie)
        file.close()
    return

def clear_proxies():
    with open('proxies', "w") as file:
        file.truncate()
        file.close()
    return True
