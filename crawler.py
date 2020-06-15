try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found, please run 'pip install google'")


# https://www.geeksforgeeks.org/performing-google-search-using-python-code/
# Searh keyword
def search_google(keyword):
    for j in search(keyword, tld="co.in", num=10, stop=10, pause=2):
        print(j)


if __name__ == '__main__':
    query = 'BLM'
    search_google(query)
