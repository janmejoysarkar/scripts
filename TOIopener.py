'''
Opens Latest Delhi Edition TOI in browser.
New paper available at 7am everyday
''' 

import requests
from bs4 import BeautifulSoup
import webbrowser as wb

url='https://dailyepaper.in/times-of-india-epaper-pdf-download-2021/'
page= requests.get(url)
status=page.status_code
print(status)
soup = BeautifulSoup(page.content, 'html.parser')
paper= soup.find_all(style ="font-size: 16px;")[0]
link= paper.find(href=True)['href']
wb.open(link)
