import csv
import os
import json


def add_entry_to_csv(data, filename='output.csv'):
    """
    Add a dictionary entry to a CSV file
    :param data:
    :param filename:
    :return:
    """
    headers = ['FirstName', 'LastName', 'CompanyName', 'Email', 'LocationCity', 'JobTitle', 'LinkedInLink',
               'Experience', 'UniversityAttendedForBachelorsDegree', 'BachelorsDegreeFieldOfStudy',
               'UniversityAttendedForMastersDegree', 'MastersDegreeFieldOfStudy']

    if isinstance(data, str):
        data = json.loads(data)

    experience_str = '; '.join([f'{exp["Role"]}, {exp["Company"]}, {exp["Duration"]}' for exp in data["Experience"]])
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


if __name__ == "__main__":
    data = {
        "FirstName": "Zachary",
        "LastName": "Bramwell",
        "CompanyName": "Sperry, Mitchell & Company",
        "Email": "zbramwell@sperrymitchell.com",
        "LocationCity": "New York",
        "JobTitle": "Analyst",
        "LinkedInLink": "linkedin.com/in/zacharybramwell",
        "Experience": [
            {
                "Role": "Associate",
                "Company": "Sperry, Mitchell & Company",
                "Duration": "2024-Present"
            },
            {
                "Role": "Analyst",
                "Company": "Sperry, Mitchell & Company",
                "Duration": "2022-2024"
            },
            {
                "Role": "Teaching Assistant",
                "Company": "Cornell University",
                "Duration": "2022-2022"
            }
        ],
        "UniversityAttendedForBachelorsDegree": "Cornell University",
        "BachelorsDegreeFieldOfStudy": "Applied Economics and Management",
        "UniversityAttendedForMastersDegree": "",
        "MastersDegreeFieldOfStudy": ""
    }

    add_entry_to_csv(data)
    print("Data added to CSV file")
