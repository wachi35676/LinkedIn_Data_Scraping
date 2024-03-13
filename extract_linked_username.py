import csv


def get_linkedin_usernames(filename='sample.csv'):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        usernames = []
        for row in reader:
            link = row['LinkedIn link']
            username = link.split('/')[-1]
            usernames.append(username)
        return usernames


if __name__ == "__main__":
    usernames = get_linkedin_usernames()
    print(usernames)
