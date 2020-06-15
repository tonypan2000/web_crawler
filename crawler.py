try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found, please run 'pip install google'")


# https://www.geeksforgeeks.org/performing-google-search-using-python-code/
# Search keyword
def search_google(keyword):
    return [query for query in search(keyword, tld="co.in", num=10, stop=10, pause=2)]
