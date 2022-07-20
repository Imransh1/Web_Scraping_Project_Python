import requests
from bs4 import BeautifulSoup
import pandas as pd


final = pd.DataFrame()


for j in range (1,10):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    response = requests.get(f'https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page={j}',headers=headers).text
    soup = BeautifulSoup(response, 'lxml')
   
    companies = soup.find_all('div', class_='company-content-wrapper')
 
    comp_names = []
    ratings = []
    reviews = []
    c_type = []
    Locations = []
    how_old = []
    workforce = []


    for i in companies:
        try:
            comp_names.append(i.find('h2').text.strip())
        except:
            comp_names.append("None")
        try:
            ratings.append(i.find('p').text.strip())
        except:
            ratings.append("None")
        try:
            reviews.append(i.find('a', class_='review-count').text.strip())
        except:
            reviews.append("None")
        try:
            c_type.append(i.find('p', class_='infoEntity').text.strip())
        except:
            c_type.append("None")
        try:
            Locations.append(i.find_all('p', class_='infoEntity')[1].text.strip())
        except:
            Locations.append("None")
        try:
            how_old.append(i.find_all('p', class_='infoEntity')[2].text.strip())
        except:
            how_old.append("None")
        try:
            workforce.append(i.find_all('p', class_='infoEntity')[3].text.strip())
        except:
            workforce.append("None")
    dict = {'Name':comp_names,  'Ratings':ratings, 'Reviews':reviews, 'Company_Type':c_type, 'Locations':Locations, 'How_Old':how_old, 'Workforce':workforce }
    df = pd.DataFrame(dict)
    final = final.append(df,ignore_index= True)
    pd.set_option('display.colheader_justify', 'center')


csv_data = final.to_csv('scraped1_data.csv',na_rep="None")