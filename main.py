import requests
from bs4 import BeautifulSoup
from random import choice

user_agents = [
                'Mozilla/5.0 (Linux; U; Android 6.0; en-US; Nomi_i4510 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.2.1.1108 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 5.1; Optima 1200T 3G TT1043PG Build/UNKNOWN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 YaBrowser/18.1.0.527.01 Safari/537.36',                'Opera/9.80 (J2ME/MIDP; Opera Mini/8.0.35158/90.140; U; ru) Presto/2.12.423 Version/12.16',
                'Mozilla/5.0 (Linux; Android 4.3; SM-N9005 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3120.77 Safari/537.36',
                'Mozilla/5.0 (Linux; Android 4.4.2; ASUS_T00I Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.135 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 7.0; BQru-5022 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 YandexSearch/7.15',
                'Mozilla/5.0 (Linux; Android 6.0; BQS-5020 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 YandexSearch/7.20',
                'Mozilla/5.0 (Linux; Android 4.4.2; U27GT-3GH Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36',
                'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) GSA/42.0.183854831 Mobile/15D60 Safari/604.1'
               ]


def headers_random():
    return {'Accept': "*/*", 'User-Agent': choice(user_agents)}


unique_list = []
unique_list_update = []


def news(url_news):
    req = requests.get(url_news, headers=headers_random())
    src = req.text
    soup = BeautifulSoup(src, "lxml")

    all_news = soup.find_all(class_="news__title")
    all_desp = soup.find_all(class_="news__description")
    all_link = soup.find_all(class_='news__more')

    for item_title in all_news[:5]:
        item = item_title.text
        clear_item = item.strip()
        unique_list.append(f'{clear_item}\n')

    for item_desp in all_desp[:5]:
        item2 = item_desp.text
        clear_item2 = item2.strip()
        unique_list.append(f'{clear_item2}\n')

    for item_link in all_link[:5]:
        item3 = item_link.get('href')
        unique_list.append(f'https://intuit.kg{item3}\n\n')

    for topic1 in unique_list[::5]:
        unique_list_update.append(topic1)
    for topic2 in unique_list[1::5]:
        unique_list_update.append(topic2)
    for topic3 in unique_list[2::5]:
        unique_list_update.append(topic3)


news(url_news="https://intuit.kg/news/0")