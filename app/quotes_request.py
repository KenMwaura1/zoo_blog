import requests


def get_quotes():
    """
    This function gets the quotes from the API and returns a list of quotes
    """
    url = 'https://type.fit/api/quotes'
    response = requests.get(url)
    quotes = response.json()
    return quotes