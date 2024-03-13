import http.client
import os

from dotenv import load_dotenv

# Load the .env file
load_dotenv()


def scrape_linkedin_data(username):
    """
    This function will scrape the linked in data of the user
    :param username:
    :return:
    """
    conn = http.client.HTTPSConnection("linkedin-api8.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': os.getenv("RAPID_API_KEY"),
        'X-RapidAPI-Host': "linkedin-api8.p.rapidapi.com"
    }

    conn.request("GET", "/?username=" + username, headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")


if __name__ == "__main__":
    print(scrape_linkedin_data("zacharybramwell"))
