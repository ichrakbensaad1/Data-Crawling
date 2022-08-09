from bs4 import BeautifulSoup
import requests
from csv import writer

from scrap import Locations

import urllib3
urllib3.disable_warnings()

url= "https://www.hhs.gov/ohrp/international/clinical-trial-registries/index.html"

page = requests.get(url, verify=False)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('tbody').find('tr')

with open('dataset.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Trial_ID']
    thewriter.writerow(header)
    info = [Trial_ID,'\n']
    thewriter.writerow(info)   
    #for list in lists:
        #Trial_ID = list.find('tr').text.replace('\n', '')
        #Trial_ID = list.find('tr').text.replace('\n', '')

        
        #info = [Trial_ID,'\n']
        #thewriter.writerow(info)
        

