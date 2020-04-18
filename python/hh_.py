import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
}
base_url = 'https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&search_period=7&text=Python&page=0'


def hh_pars(base_url, headers):
    session = requests.Session()
    req = session.get(base_url, headers=headers)
    if req.status_code == 200:
        soup = bs(req.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})

        for div in divs:
            title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            print(title + ' - ' + ' ' + href)

    else:
        print('Error')

hh_pars(base_url,headers)


# session = requests.Session()
# req = session.get(base_url, headers=headers)
# if req.status_code == 200:
#     soup = bs(req.content, 'html.parser')
#     divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
#     for div in divs:
#         title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
#         href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
#         sql = "INSERT INTO `artist_song` (`artist`, `song`) VALUES (%s, %s)"
# print(soup.prettify())

