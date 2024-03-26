import csv
import http.client
import json
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


desired_format = {
    "FirstName": "David",
    "LastName": "Schmidt",
    "Company": "Goldman Sachs",
    "Email": "david.c.schmidt@gs.com",
    "City": "New York",
    "Title": "Investment Banking Associate",
    "Industry": "Investment Banking",
    "PersonLinkedin": "http://www.linkedin.com/in/1davidschmidt",
    "Experience": [
        {
            "Role": "Investment Banking Associate",
            "Company": "Goldman Sachs",
            "Duration": "2021 - Present"
        },
        {
            "Role": "Credit Associate",
            "Company": "Goldman Sachs",
            "Duration": "2021 - 2021"
        },
        {
            "Role": "Credit Analyst",
            "Company": "Goldman Sachs",
            "Duration": "2017 -2020"
        }
    ],
    "BachelorsUniversity": "Stanford University",
    "BachelorsFieldOfStudy": "Management Science & Engineering",
    "MastersUniversity": "",
    "MastersFieldOfStudy": ""
}


def get_linkedin_usernames(filename='sample.csv'):
    """
    Get LinkedIn usernames from a CSV file
    :param filename:
    :return:
    """
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        usernames = []
        emails = {}
        for row in reader:
            link = row['LinkedIn link']
            username = link.split('/')[-1]
            usernames.append(username)
            emails[username] = row['Email']
        return usernames, emails


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

    if res.status == 429:
        response = json.loads(res.read().decode("utf-8"))
        raise Exception("Response code 429: " + response["message"])

    data = res.read()

    return data.decode("utf-8")


def clean_data(raw_data):
    """
    This function takes a JSON object with a specific format and maps it to a desired format.

    :param raw_data: JSON object with a different format
    :return: JSON object with the desired format
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system",
             "content": "I have a JSON object with a specific format. Here is an example: " + json.dumps(
                 desired_format)},
            {"role": "user",
             "content": "I have a JSON object with a different format. Here it is: "
                        + json.dumps(raw_data)
                        + ". Please map the keys from my JSON object to the keys in the example format. "
                          "Do not add any extra keys that are not present in the example format."
             }
        ]
    )

    return response.choices[0].message.content


def add_entry_to_csv(data, filename='output.csv'):
    """
    Add a dictionary entry to a CSV file
    :param data:
    :param filename:
    :return:
    """
    headers = ['FirstName', 'LastName', 'Company', 'Email', 'Title', 'City', 'Industry', 'PersonLinkedin',
               'Experience', 'BachelorsUniversity', 'BachelorsFieldOfStudy',
               'MastersUniversity', 'MastersFieldOfStudy']

    if isinstance(data, str):
        data = json.loads(data)

    experience_str = '\n'.join([f'{exp["Role"]}, {exp["Company"]}, {exp["Duration"]}' for exp in data["Experience"]])
    data["Experience"] = experience_str

    data = {key: data[key] for key in headers if key in data}

    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

        # Flush the file buffer and force write to disk
        csvfile.flush()
        os.fsync(csvfile.fileno())


def scrape_and_clean_data(usernames, emails, update_username_callback):
    """
    Scrape and clean data for each username
    :param usernames:
    :param update_username_callback: Callback function to update the username
    :return:
    """
    for username in usernames:
        update_username_callback(username)  # Call the callback with the current username
        raw_data = scrape_linkedin_data(username)
        cleaned_data = clean_data(json.loads(raw_data))
        cleaned_data = json.loads(cleaned_data)
        cleaned_data['PersonLinkedin'] = f"https://www.linkedin.com/in/{username}"
        cleaned_data['Email'] = emails[username]
        yield cleaned_data


def main(file_path='sample.csv', update_username_callback=None):
    """
    Main function to scrape and clean data for LinkedIn usernames in a CSV file
    :param file_path:
    :param update_username_callback: Callback function to update the username
    :return:
    """
    usernames, emails = get_linkedin_usernames(file_path)

    # Scrape and clean data for each username, and add it to a CSV file
    for data in scrape_and_clean_data(usernames, emails, update_username_callback):
        add_entry_to_csv(data)

    print("Data added to CSV file")


if __name__ == "__main__":
    main()
