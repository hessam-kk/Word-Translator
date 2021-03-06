import requests
from bs4 import BeautifulSoup
import re

def Translate(Word):
    Url = 'https://dic.b-amooz.com/en/dictionary/w?word=' + Word # handle URL to request
    word_list = [] # To store meanings 
    # Load the whole webpage
    page = requests.get(Url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Grab appropriate section using quick access menu
    meanings = soup.find_all('a', attrs={'class' : 'quick-access-items'} )

    for meaning in meanings: 
        meaning = str(meaning)
        meaning = re.sub(r'\s+', ' ', meaning) # remove whitespaces
        meaning = re.sub(r'<.+?>', ' ', meaning) # remove tags and spans
        meaning = re.sub(r'\d+', ' ', meaning) # remove numbers from start
        meaning = re.sub('\.', '', meaning) # remove dot from start
        meaning = re.sub(r'\u200c', ' ', meaning) # remove half space 
        meaning = meaning.strip() # remove any extra left whitespaces
        # print(meaning)
        word_list.append(meaning)

    return word_list
