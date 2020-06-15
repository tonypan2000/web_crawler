from bs4 import BeautifulSoup
import codecs
import requests
import urllib


def fetch_webpage(url):
    # Some websites disallow urllib requests
    # urllib2 will require adding a user-agent
    # but is that allowed/ethically ok to do?
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

    # request with urllib
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    html_contents = response.read()

    # request with python requests
    # res = requests.get(url, headers=header)

    return html_contents


# find and returns all links that the donate buttons point to in a webpage
def find_donate_button(webpage):
    # testing with local site
    # content = codecs.open(webpage, 'r').read()
    # soup = BeautifulSoup(requests.get(url).content)
    soup = BeautifulSoup(webpage, 'html.parser')
    titles = soup.find_all('a', title='donate')
    links = [entry.get('href') for entry in titles]
    return links


def scrape(urls):
    for url in urls:
        webpage = fetch_webpage(url)
        link = find_donate_button(webpage)
