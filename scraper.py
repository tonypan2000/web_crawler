from bs4 import BeautifulSoup
import codecs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def fetch_webpage(url, browser):
    browser.get(url)
    html = browser.page_source
    return html


# find and returns all links that the donate buttons point to in a webpage
def find_donate_links(webpage):
    # testing with local site
    # content = codecs.open(webpage, 'r').read()
    # soup = BeautifulSoup(requests.get(url).content)
    soup = BeautifulSoup(webpage, 'html.parser')
    titles = soup.find_all('a', title='Donate')
    donate = soup.find_all('a', title='donate')
    if donate:
        titles.append(donate)
    links = [entry.get('href') for entry in titles]
    return links


def scrape(urls):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    for url in urls:
        webpage = fetch_webpage(url, browser)
        links = find_donate_links(webpage)
        print(links)
