import json

from extract_linked_username import get_linkedin_usernames
from linkedIn_data_scrapper import scrape_linkedin_data
from gpt_data_cleaning import clean_data
from dictionary_to_csv import add_entry_to_csv


def scrape_and_clean_data(usernames):
    """
    Scrape and clean data for each username
    :param usernames:
    :return:
    """
    for username in usernames:
        raw_data = scrape_linkedin_data(username)
        cleaned_data = clean_data(json.loads(raw_data))
        cleaned_data = json.loads(cleaned_data)
        cleaned_data['LinkedInLink'] = f"https://www.linkedin.com/in/{username}"
        yield cleaned_data


def main(file_path='sample.csv'):
    """
    Main function to scrape and clean data for LinkedIn usernames in a CSV file
    :param file_path:
    :return:
    """
    usernames = get_linkedin_usernames(file_path)

    # Scrape and clean data for each username, and add it to a CSV file
    for data in scrape_and_clean_data(usernames):
        add_entry_to_csv(data)

    print("Data added to CSV file")


if __name__ == "__main__":
    main()
