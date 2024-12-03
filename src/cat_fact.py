import requests


def get_cat_fact():
    """Fetches a random cat fact from the MeowFacts API."""
    response = requests.get("https://meowfacts.herokuapp.com/")
    return response.json()


if __name__ == "__main__":
    print(get_cat_fact())
