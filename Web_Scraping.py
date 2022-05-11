import bs4, requests

site = requests.get('https://github.com/PedroIeremis').content
print(site)

soup = bs4.BeautifulSoup(site, 'html.parser')
print(soup)


