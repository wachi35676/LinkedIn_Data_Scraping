import csv


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


if __name__ == "__main__":
    usernames = get_linkedin_usernames()
    print(usernames)
