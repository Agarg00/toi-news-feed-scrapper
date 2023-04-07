import requests
from bs4 import BeautifulSoup

res = requests.get('https://timesofindia.indiatimes.com/home/headlines')
soup = BeautifulSoup(res.text, 'html.parser')
a = soup.select('.w_tle')


def toi_news_headlines(links):
    nh = []
    for item, idx in enumerate(links):
        title = links[item].getText()
        href = links[item].select('a')[0].get('href', None)
        nh.append({'title': title, 'link': f'https://timesofindia.indiatimes.com{href}'})
    return nh


result = toi_news_headlines(a)
list_of_values = list(map(lambda d: d['title'], result))
all_keys = list(map(lambda d: d['link'], result))

print("Here is some news feed from TOI with titles and links:\n\n")
for i in range(len(result)):
    print(f'Title: \n\t{list_of_values[i]} \nLink: \n\t{all_keys[i]} \n\n')

print("Total Number of Feeds : ", len(result))
