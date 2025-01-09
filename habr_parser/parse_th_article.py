import requests
from bs4 import BeautifulSoup
import json

print('Write the word "key" if you wanna search articles by the key word\nWrite the word "link" if you have a particular link:')
paste = input()
if paste == 'link':
    print('Paste the link:')
    link = input()
elif paste == 'key':
    print('Write a key word:')
    word = input()
else:
    print('Your input does not match any of the options :(')


habr = https://habr.com/ru/articles/

     
class FirstPaste():
    response = requests.get(link).text
    soup = BeautifulSoup(response, 'lxml')

    def find_by_key(word, soup):
        articles_block = soup.find_all('a', class_ = 'tm-title__link')
        articles = articles_block.find_all('span').text
        key_articles = []
        if word in articles:
            key_articles.append(word)

class ParseTheArticle():
    def find_all_properties(self):
        response = requests.get(link).text
        soup = BeautifulSoup(response, 'lxml')

        title_block = soup.find('h1')
        title_element = title_block.find('span').text
        
        author_block = soup.find('span', class_ = 'tm-user-info__user tm-user-info__user_appearance-default')
        author_element = author_block.find('a', class_ = 'tm-user-info__username').text

        contents_block = soup.find('div', class_ = 'tm-article-body').text

        return title_element, author_element, contents_block


class Article(ParseTheArticle):

    def __init__(self):
        article = self.find_all_properties()
        self.title = article[0]
        self.url = link
        self.author = article[1]
        self.contents = article[2]

    def convert_to_dict(self):
        article = {"title" : self.title,
                   "url" : self.url,
                   "author" : self.author,
                   "contents" : self.contents}
        return article


link = Article()
article = link.convert_to_dict()
with open('result.json', 'w', encoding='utf-8') as json_file:
        json.dump({'data' : article}, json_file, ensure_ascii=False, indent=4)

