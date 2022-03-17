# Genérer du Traffic

Script en  python3 permettant de scraper des proxies situés en France ou à l'étranger ( selon le paramétrage) , et grâce à une liste d'user agent.

#### Permet de pinger de manière indétectable une url ou des urls afin de simuler du traffic, google analyse celui-ci, ainsi plus il sera fort et régulier plus google améliora ainsi le référencement de votre site.

#### Ce script est conçu pour tourner 24/24h, avec un temps aléatoire entre chaque requetes répartis en fonction du nombre de proxies qu'il
récupère. Dés que son cycle est terminé, il récupère de nouveaux proxies.

Ainsi s'il récupére que 100 proxies, il va les répartir sur 24h, tout en générant un temps aléatoire entre chaque requètes

#  Traffic Generator

Script in python3 allowing to scrape proxies located in France or abroad (depending on the configuration), and thanks to a list of user agents.

#### Allows you to ping an url or urls in an undetectable way in order to simulate traffic, google analyzes it, so the stronger and more regular it will be, the more google will improve the referencing of your site.

#### This script is designed to run 24 hours a day, with a random time between each request distributed according to the number of proxies it
recovers. As soon as its cycle is finished, it retrieves new proxies.

So if it retrieves only 100 proxies, it will distribute them over 24 hours, while generating a random time between each request

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the project.

```bash
pip install requests
pip install time
pip install random
pip install numpy
```

## Launch

```python
python3 ./pinger.py
```
