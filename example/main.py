import requests
import fake_useragent
from bs4 import BeautifulSoup

user = fake_useragent.UserAgent().random

header = {'user-agent': user}

link = "https://browser-info.ru/"
response = requests.get(link, headers=header).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id = "tool_padding")

### проверяем статус javascript
check_js = block.find('div', id = "javascript_check")
status_js = check_js.find_all('span')[1].text
result_js = f'javascript: {status_js}'

### проверяем статус flash
check_flash = block.find('div', id = 'flash_version')
status_flash = check_flash.find_all('span')[1].text
result_flash = f'flash: {status_flash}'

### проверяем статус user_agent
check_user = block.find('div', id = 'user_agent').text

print(check_user)
'''with open("l.html", "w", encoding="utf-8") as file:
    file.write(response)'''