import requests
from bs4 import BeautifulSoup

scraped_urls = [
    'https://proxyhub.me/fr/be-free-proxy-list.html',
    'https://proxyhub.me/fr/fr-free-proxy-list.html'
]


def get_array_proxies():
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
    return


def cleaning_proxies():
    with open('proxies', "r") as f:
        proxies = f.read().splitlines()

    with open('proxies', "w") as f:
        f.write(str(set(proxies)))
    return
