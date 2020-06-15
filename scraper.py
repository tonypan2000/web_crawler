from bs4 import BeautifulSoup
import requests
import urllib


def find_donate_button(url):
    # Some websites disallow urllib requests
    # urllib2 will require adding a user-agent
    # but is that allowed/ethically ok to do?
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

    # request with urllib
    # request = urllib.request.Request(url, headers=header)
    # response = urllib.request.urlopen(request)
    # html_contents = response.read()

    # request with python requests
    res = requests.get(url, headers=header)

    soup = BeautifulSoup(res, 'html.parser')
    titles = soup.find('title')
    print(titles.text)


def scrape(urls):
    for url in urls:
        find_donate_button(url)
