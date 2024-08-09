import requests
import random
from bs4 import BeautifulSoup


UAS = ("Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1", 
       "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
       "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
       )



def get_soup(url):
       ua = UAS[random.randrange(len(UAS))]
       s = requests.Session()
       headers = {'user-agent': ua}
       r = s.get(url, headers=headers)

       soup = BeautifulSoup(r.text, 'html.parser')

       return soup


def get_price(url):
       soup = get_soup(url)
       soup_price = soup.find_all("span", {"class": "price__value"})
       
       if len(soup_price) == 0:
              print("failed")
              with open("output1.html", "w") as file:
                     file.write(str(soup))
       else:
              price = soup_price[0].text
              raw_price = price.replace("$", "")
              print(raw_price)