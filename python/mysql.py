import requests
from bs4 import BeautifulSoup as bs
import mysql
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

bs_url = 'https://www.avito.ru/moskva'

session = requests.session()
req = session.get(bs_url,headers=headers)
try:
    if req.status_code == 200:
        soup = bs(req.content,'html.parser')
        divs = soup.find_all('div', attrs={'class':'l-content clearfix'})

        mysql = """INSERT INTO users (id, company, price) VALUES (%s,%s,%S)"""
    else:
        print('Error')
finally:
    print('Hello World')
print(soup.prettify())