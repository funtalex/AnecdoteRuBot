import requests
import random
from bs4 import BeautifulSoup


class Anecdote:
    def __init__(self, url='https://anekdoty.ru/'):
        self.url = url

    def make_buttons(self): # return dict - keys - name of topic, value - link
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'html.parser')
        columns = soup.find_all('ul', class_='col')
        str_columns = '\n'.join([str(item) for item in columns])
        soup2 = BeautifulSoup(str_columns, 'html.parser')
        list_of_links = soup2.find_all('a')
        dict_links = dict()
        for item in list_of_links:
            dict_links[item.text.capitalize()] = item['href']
        return dict_links


    def make_anecdote(self, sub_url='https://anekdoty.ru/detskie/'):
        # sub_url = 'https://anekdoty.ru/detskie/'
        sub_page = requests.get(sub_url)
        soup = BeautifulSoup(sub_page.text, 'html.parser')
        list_anecdotes = [item.text for item in soup.find_all('div', class_='holder-body')]
        return list_anecdotes[random.randrange(len(list_anecdotes))]


    url = 'https://anekdoty.ru/'