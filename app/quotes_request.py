import requests
from random import randint


def get_quotes():
    """
    This function gets the quotes from the API and returns a list of quotes
    """
    url = 'https://type.fit/api/quotes'
    response = requests.get(url)
    quotes = response.json()
    num = randint(1, 30)
    quote = quotes[num]
    print(quote)
    return quote
