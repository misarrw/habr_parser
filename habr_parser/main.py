import requests
from bs4 import BeautifulSoup
import json

habr = 'https://habr.com/ru/search/'

def find_by_key(word):
    global habr, page
    if page > 1:
        habr += f'page{page}&'
    search_url = habr + f'?q={word}&target_type=posts&order=relevance'
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'lxml')
    articles = soup.find_all('article', class_='tm-articles-list__item')
    key_articles_dict = {}
    key_articles_list = []
    
    for article in articles:
        title_block = article.find('h2', class_='tm-title tm-title_h2')
        if title_block and title_block.find('span'):
            link_tag = title_block.find('a', class_='tm-title__link')
            link = link = 'https://habr.com' + link_tag['href']
            title = title_block.find('span').text
            key_articles_dict[title] = link
            key_articles_list.append(title)
    habr = 'https://habr.com/ru/search/'
    return key_articles_dict, key_articles_list

class ParseTheArticle():
    def find_all_properties(self):
        response = requests.get(self.url).text
        soup = BeautifulSoup(response, 'lxml')

        title_block = soup.find('h1')
        title_element = title_block.find('span').text
        
        author_block = soup.find('span', class_ = 'tm-user-info__user tm-user-info__user_appearance-default')
        author_element = author_block.find('a', class_ = 'tm-user-info__username').text

        contents_block = soup.find('div', class_ = 'tm-article-body').text

        return title_element, author_element, contents_block


class Article(ParseTheArticle):
    def __init__(self, url):
        self.url = url
        article = self.find_all_properties()
        self.title = article[0]
        self.author = article[1]
        self.contents = article[2]

    def convert_to_dict(self):
        article = {"title" : self.title,
                   "url" : self.url,
                   "author" : self.author,
                   "contents" : self.contents}
        return article
    

'''def next_page():
    global page, habr, word
    page += 1
    habr += f'?page{page}&'
    result = find_by_key(word)
    for number, article in enumerate(result):
        print(f'{number + 1}. {article}')'''


def show_page():
    global page
    key_articles = find_by_key(word)
    key_articles_list = key_articles[1]
    key_articles_dict = key_articles[0]
    for index, article in enumerate(key_articles_list):
        print(f'{index + 1}. {article}')
    print('If you wanna see other articles, write "next"\nOr write the number of the article you wanna see:')
    next_or_number = input()
    if next_or_number == 'next':
        page += 1
        show_page()
    elif next_or_number.isdigit() == True and int(next_or_number) in range(21):
        element = key_articles_list[int(next_or_number) - 1]
        url = key_articles_dict[element]
        article_url = Article(url)
        article = article_url.convert_to_dict()
        with open('result.json', 'w', encoding='utf-8') as json_file:
            json.dump({'data' : article}, json_file, ensure_ascii=False, indent=4)


page = 1
print('Write the word "key" if you wanna search articles by the key word\nWrite the word "link" if you have a particular link:')
paste = input()
if paste == 'link':
    print('Paste the link:')
    article_url = input()
    article_url = Article(article_url)
    article = article_url.convert_to_dict()
    with open('result.json', 'w', encoding='utf-8') as json_file:
            json.dump({'data' : article}, json_file, ensure_ascii=False, indent=4)
elif paste == 'key':
    print('Write a key word:')
    word = input()
    show_page()
else:
    print('Your input does not match any of the options :(')