import json
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

desired_format = {
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
             "content": "I have a JSON object with a specific format. Here is an example: " + json.dumps(desired_format)},
            {"role": "user",
             "content": "I have a JSON object with a different format. Here it is: "
                        + json.dumps(raw_data)
                        + ". Please map the keys from my JSON object to the keys in the example format. "
                          "Do not add any extra keys that are not present in the example format."
             }
        ]
    )

    return response.choices[0].message.content


if __name__ == '__main__':
    raw_data = {
        "firstName": "Muhammad Wasif Ali",
        "lastName": "Wasif",
        "isOpenToWork": False,
        "isHiring": False,
        "profilePicture": "https://media.licdn.com/dms/image/D5603AQH41T7QmZP5xA/profile-displayphoto-shrink_800_800/0/1665816685398?e=1715817600&v=beta&t=YF8xnHhaqwkDla7KQSFVT5V8DrL2cbDdxwwE0wq5t_A",
        "summary": "",
        "headline": "Software Engineer @ Quest | FAST '24 | Research Focus: Procedural Generation of Biomes in Video Games",
        "geo": {
            "country": "Pakistan",
            "city": "Rawalpindi, Punjab",
            "full": "Rawalpindi, Punjab, Pakistan"
        },
        "languages": None,
        "educations": [
            {
                "start": {
                    "year": 2020,
                    "month": 0,
                    "day": 0
                },
                "end": {
                    "year": 2024,
                    "month": 0,
                    "day": 0
                },
                "fieldOfStudy": "",
                "degree": "",
                "grade": "",
                "schoolName": "National University of Computer and Emerging Sciences",
                "description": "",
                "activities": "",
                "url": "https://www.linkedin.com/school/fastnu/",
                "schoolId": "15096487"
            }
        ],
        "position": [
            {
                "companyName": "Quest",
                "companyUsername": "quest-software-quality-engineering-&-testing-laboratory",
                "companyURL": "https://www.linkedin.com/company/quest-software-quality-engineering-&-testing-laboratory/",
                "companyLogo": "https://media.licdn.com/dms/image/D4D0BAQFpPsIDzq4KRw/company-logo_400_400/0/1665040866568/quest_software_quality_engineering__testing_laboratory_logo?e=1718236800&v=beta&t=vsClpZlIBd9YKI7RjfLKAQYznoycxQlAtR8sUequYWY",
                "companyIndustry": "Information Technology & Services",
                "companyStaffCountRange": "11 - 50",
                "title": "Software Engineer",
                "location": "Islāmābād, Pakistan",
                "description": "",
                "employmentType": "",
                "start": {
                    "year": 2024,
                    "month": 1,
                    "day": 0
                },
                "end": {
                    "year": 0,
                    "month": 0,
                    "day": 0
                }
            },
            {
                "companyName": "FAST Gaming Club",
                "companyUsername": "fast-gaming-club",
                "companyURL": "https://www.linkedin.com/company/fast-gaming-club/",
                "companyLogo": "https://media.licdn.com/dms/image/D4D0BAQFS7chXCo3jow/company-logo_400_400/0/1698605714318?e=1718236800&v=beta&t=YY57Yy3ZFWqrbR4PHAcQn_OBmyRUzSOiMnfnKh-8gyQ",
                "companyIndustry": "Computer Games",
                "companyStaffCountRange": "11 - 50",
                "title": "Creative Lead Game Development",
                "location": "Islāmābād, Pakistan",
                "description": "",
                "employmentType": "",
                "start": {
                    "year": 2023,
                    "month": 8,
                    "day": 0
                },
                "end": {
                    "year": 0,
                    "month": 0,
                    "day": 0
                }
            },
            {
                "companyName": "FAST Software Engineering Society",
                "companyUsername": "",
                "companyURL": "",
                "companyLogo": "",
                "companyIndustry": "",
                "companyStaffCountRange": "",
                "title": "Lead Work & Dev",
                "location": "",
                "description": "",
                "employmentType": "",
                "start": {
                    "year": 2023,
                    "month": 1,
                    "day": 0
                },
                "end": {
                    "year": 0,
                    "month": 0,
                    "day": 0
                }
            },
            {
                "companyName": "National University of Computer and Emerging Sciences",
                "companyUsername": "fastnu",
                "companyURL": "https://www.linkedin.com/school/fastnu/",
                "companyLogo": "https://media.licdn.com/dms/image/C510BAQGdFV3S_Aelww/company-logo_400_400/0/1631304359411?e=1718236800&v=beta&t=XGEFVxtKJ3rQPp_o9IS-EZK0RMZlE3u3qfKkYQ38Oe0",
                "companyIndustry": "Higher Education",
                "companyStaffCountRange": "1001 - 5000",
                "title": "Teacher Assistant HCI",
                "location": "Islāmābād, Pakistan",
                "description": "",
                "employmentType": "Part-time",
                "start": {
                    "year": 2023,
                    "month": 8,
                    "day": 0
                },
                "end": {
                    "year": 2023,
                    "month": 12,
                    "day": 0
                }
            },
            {
                "companyName": "National University of Computer and Emerging Sciences",
                "companyUsername": "fastnu",
                "companyURL": "https://www.linkedin.com/school/fastnu/",
                "companyLogo": "https://media.licdn.com/dms/image/C510BAQGdFV3S_Aelww/company-logo_400_400/0/1631304359411?e=1718236800&v=beta&t=XGEFVxtKJ3rQPp_o9IS-EZK0RMZlE3u3qfKkYQ38Oe0",
                "companyIndustry": "Higher Education",
                "companyStaffCountRange": "1001 - 5000",
                "title": "Teacher Assistant DB",
                "location": "",
                "description": "",
                "employmentType": "Part-time",
                "start": {
                    "year": 2023,
                    "month": 8,
                    "day": 0
                },
                "end": {
                    "year": 2023,
                    "month": 12,
                    "day": 0
                }
            },
            {
                "companyName": "Grayhat",
                "companyUsername": "grayhatpk",
                "companyURL": "https://www.linkedin.com/company/grayhatpk/",
                "companyLogo": "https://media.licdn.com/dms/image/C4D0BAQFgba8LDlERRQ/company-logo_400_400/0/1633279020683?e=1718236800&v=beta&t=ziRuRNHZ0d94cpq5zStHEsP30CpahNeqBsYfJ40p-JY",
                "companyIndustry": "Computer Software",
                "companyStaffCountRange": "11 - 50",
                "title": "Game Developer",
                "location": "Islāmābād, Pakistan",
                "description": "",
                "employmentType": "Internship",
                "start": {
                    "year": 2023,
                    "month": 6,
                    "day": 0
                },
                "end": {
                    "year": 2023,
                    "month": 9,
                    "day": 0
                }
            },
            {
                "companyName": "USquare Solutions",
                "companyUsername": "usquaresolutions",
                "companyURL": "https://www.linkedin.com/company/usquaresolutions/",
                "companyLogo": "https://media.licdn.com/dms/image/C4D0BAQH6YkJbYXJARQ/company-logo_400_400/0/1630511547372/usquaresolutions_logo?e=1718236800&v=beta&t=Xed8C5i8BlZ2GqNL5swlQJn8iaxEmqfRIkx2v1g_8lY",
                "companyIndustry": "Information Technology & Services",
                "companyStaffCountRange": "11 - 50",
                "title": "Game Developer",
                "location": "Islāmābād, Pakistan",
                "description": "",
                "employmentType": "Contract",
                "start": {
                    "year": 2023,
                    "month": 2,
                    "day": 0
                },
                "end": {
                    "year": 2023,
                    "month": 8,
                    "day": 0
                }
            },
            {
                "companyName": "USquare Solutions",
                "companyUsername": "usquaresolutions",
                "companyURL": "https://www.linkedin.com/company/usquaresolutions/",
                "companyLogo": "https://media.licdn.com/dms/image/C4D0BAQH6YkJbYXJARQ/company-logo_400_400/0/1630511547372/usquaresolutions_logo?e=1718236800&v=beta&t=Xed8C5i8BlZ2GqNL5swlQJn8iaxEmqfRIkx2v1g_8lY",
                "companyIndustry": "Information Technology & Services",
                "companyStaffCountRange": "11 - 50",
                "title": "Game Developer",
                "location": "Islāmābād, Pakistan",
                "description": "",
                "employmentType": "Internship",
                "start": {
                    "year": 2023,
                    "month": 1,
                    "day": 0
                },
                "end": {
                    "year": 2023,
                    "month": 2,
                    "day": 0
                }
            },
            {
                "companyName": "National University of Computer and Emerging Sciences",
                "companyUsername": "fastnu",
                "companyURL": "https://www.linkedin.com/school/fastnu/",
                "companyLogo": "https://media.licdn.com/dms/image/C510BAQGdFV3S_Aelww/company-logo_400_400/0/1631304359411?e=1718236800&v=beta&t=XGEFVxtKJ3rQPp_o9IS-EZK0RMZlE3u3qfKkYQ38Oe0",
                "companyIndustry": "Higher Education",
                "companyStaffCountRange": "1001 - 5000",
                "title": "Lab Demonstrator OOP",
                "location": "Islāmābād, Pakistan",
                "description": "",
                "employmentType": "Part-time",
                "start": {
                    "year": 2023,
                    "month": 1,
                    "day": 0
                },
                "end": {
                    "year": 2023,
                    "month": 6,
                    "day": 0
                }
            },
            {
                "companyName": "National University of Computer and Emerging Sciences",
                "companyUsername": "fastnu",
                "companyURL": "https://www.linkedin.com/school/fastnu/",
                "companyLogo": "https://media.licdn.com/dms/image/C510BAQGdFV3S_Aelww/company-logo_400_400/0/1631304359411?e=1718236800&v=beta&t=XGEFVxtKJ3rQPp_o9IS-EZK0RMZlE3u3qfKkYQ38Oe0",
                "companyIndustry": "Higher Education",
                "companyStaffCountRange": "1001 - 5000",
                "title": "Lab Demonstrator Database",
                "location": "Islāmābād, Pakistan",
                "description": "",
                "employmentType": "Part-time",
                "start": {
                    "year": 2023,
                    "month": 1,
                    "day": 0
                },
                "end": {
                    "year": 2023,
                    "month": 6,
                    "day": 0
                }
            },
            {
                "companyName": "National University of Computer and Emerging Sciences",
                "companyUsername": "fastnu",
                "companyURL": "https://www.linkedin.com/school/fastnu/",
                "companyLogo": "https://media.licdn.com/dms/image/C510BAQGdFV3S_Aelww/company-logo_400_400/0/1631304359411?e=1718236800&v=beta&t=XGEFVxtKJ3rQPp_o9IS-EZK0RMZlE3u3qfKkYQ38Oe0",
                "companyIndustry": "Higher Education",
                "companyStaffCountRange": "1001 - 5000",
                "title": "Teacher Assistant Data Structures",
                "location": "",
                "description": "",
                "employmentType": "Part-time",
                "start": {
                    "year": 2022,
                    "month": 9,
                    "day": 0
                },
                "end": {
                    "year": 2022,
                    "month": 12,
                    "day": 0
                }
            },
            {
                "companyName": "National University of Computer and Emerging Sciences",
                "companyUsername": "fastnu",
                "companyURL": "https://www.linkedin.com/school/fastnu/",
                "companyLogo": "https://media.licdn.com/dms/image/C510BAQGdFV3S_Aelww/company-logo_400_400/0/1631304359411?e=1718236800&v=beta&t=XGEFVxtKJ3rQPp_o9IS-EZK0RMZlE3u3qfKkYQ38Oe0",
                "companyIndustry": "Higher Education",
                "companyStaffCountRange": "1001 - 5000",
                "title": "Front Desk Officer - Admissions",
                "location": "",
                "description": "",
                "employmentType": "Internship",
                "start": {
                    "year": 2022,
                    "month": 7,
                    "day": 0
                },
                "end": {
                    "year": 2022,
                    "month": 8,
                    "day": 0
                }
            },
            {
                "companyName": "FAST Gaming Club",
                "companyUsername": "fast-gaming-club",
                "companyURL": "https://www.linkedin.com/company/fast-gaming-club/",
                "companyLogo": "https://media.licdn.com/dms/image/D4D0BAQFS7chXCo3jow/company-logo_400_400/0/1698605714318?e=1718236800&v=beta&t=YY57Yy3ZFWqrbR4PHAcQn_OBmyRUzSOiMnfnKh-8gyQ",
                "companyIndustry": "Computer Games",
                "companyStaffCountRange": "11 - 50",
                "title": "Lead Game Development",
                "location": "Islāmābād, Pakistan",
                "description": "",
                "employmentType": "",
                "start": {
                    "year": 2023,
                    "month": 1,
                    "day": 0
                },
                "end": {
                    "year": 2023,
                    "month": 6,
                    "day": 0
                }
            },
            {
                "companyName": "National University of Computer and Emerging Sciences",
                "companyUsername": "fastnu",
                "companyURL": "https://www.linkedin.com/school/fastnu/",
                "companyLogo": "https://media.licdn.com/dms/image/C510BAQGdFV3S_Aelww/company-logo_400_400/0/1631304359411?e=1718236800&v=beta&t=XGEFVxtKJ3rQPp_o9IS-EZK0RMZlE3u3qfKkYQ38Oe0",
                "companyIndustry": "Higher Education",
                "companyStaffCountRange": "1001 - 5000",
                "title": "Teacher Assistant Programming Fundamentals",
                "location": "",
                "description": "",
                "employmentType": "Part-time",
                "start": {
                    "year": 2022,
                    "month": 2,
                    "day": 0
                },
                "end": {
                    "year": 2022,
                    "month": 5,
                    "day": 0
                }
            }
        ],
        "skills": [
            {
                "name": "MERN Stack"
            },
            {
                "name": "Unity"
            },
            {
                "name": "Graphic Design"
            },
            {
                "name": "GitHub"
            },
            {
                "name": "Presentation Skills"
            },
            {
                "name": "JavaScript"
            },
            {
                "name": "C++"
            },
            {
                "name": "C (Programming Language)"
            },
            {
                "name": "Microsoft SQL Server"
            },
            {
                "name": "C#"
            },
            {
                "name": "Java"
            },
            {
                "name": "ASP.NET MVC"
            }
        ],
        "givenRecommendation": None,
        "receivedRecommendation": None,
        "courses": None,
        "certifications": [
            {
                "name": "AWS Certified Cloud Practitioner",
                "start": {
                    "year": 2024,
                    "month": 1,
                    "day": 0
                },
                "end": {
                    "year": 2027,
                    "month": 1,
                    "day": 0
                },
                "authority": "Amazon Web Services (AWS)",
                "company": {
                    "name": "Amazon Web Services (AWS)",
                    "universalName": "amazon-web-services",
                    "logo": "https://media.licdn.com/dms/image/C560BAQER_QnUTXrPJw/company-logo_200_200/0/1670264051233/amazon_web_services_logo?e=1718236800&v=beta&t=M0eqPADj4M2QlDLtpSk58spkCaB0GKC_6F680CvYRW8",
                    "staffCountRange": {},
                    "headquarter": {}
                },
                "timePeriod": {
                    "start": {
                        "year": 0,
                        "month": 0,
                        "day": 0
                    },
                    "end": {
                        "year": 0,
                        "month": 0,
                        "day": 0
                    }
                }
            },
            {
                "name": "AWS Academy Graduate - AWS Academy Cloud Foundations",
                "start": {
                    "year": 2023,
                    "month": 12,
                    "day": 0
                },
                "end": {
                    "year": 0,
                    "month": 0,
                    "day": 0
                },
                "authority": "Amazon Web Services (AWS)",
                "company": {
                    "name": "Amazon Web Services (AWS)",
                    "universalName": "amazon-web-services",
                    "logo": "https://media.licdn.com/dms/image/C560BAQER_QnUTXrPJw/company-logo_200_200/0/1670264051233/amazon_web_services_logo?e=1718236800&v=beta&t=M0eqPADj4M2QlDLtpSk58spkCaB0GKC_6F680CvYRW8",
                    "staffCountRange": {},
                    "headquarter": {}
                },
                "timePeriod": {
                    "start": {
                        "year": 0,
                        "month": 0,
                        "day": 0
                    },
                    "end": {
                        "year": 0,
                        "month": 0,
                        "day": 0
                    }
                }
            }
        ],
        "honors": [
            {
                "title": "3rd Position - Spring 2023",
                "description": "",
                "issuer": "",
                "issuerLogo": "",
                "issuedOn": {
                    "year": 2023,
                    "month": 0,
                    "day": 0
                }
            },
            {
                "title": "Dean's List of Honors - Spring 2023",
                "description": "",
                "issuer": "",
                "issuerLogo": "",
                "issuedOn": {
                    "year": 2023,
                    "month": 0,
                    "day": 0
                }
            },
            {
                "title": "Dean's List of Honors - Fall 2022",
                "description": "",
                "issuer": "",
                "issuerLogo": "",
                "issuedOn": {
                    "year": 2022,
                    "month": 0,
                    "day": 0
                }
            },
            {
                "title": "Dean's List of Honors - Spring 2022",
                "description": "",
                "issuer": "",
                "issuerLogo": "",
                "issuedOn": {
                    "year": 2022,
                    "month": 0,
                    "day": 0
                }
            },
            {
                "title": "Dean's List of Honors - Fall 2021",
                "description": "",
                "issuer": "",
                "issuerLogo": "",
                "issuedOn": {
                    "year": 2021,
                    "month": 0,
                    "day": 0
                }
            },
            {
                "title": "Dean's List of Honors - Fall 2020",
                "description": "",
                "issuer": "",
                "issuerLogo": "",
                "issuedOn": {
                    "year": 2020,
                    "month": 0,
                    "day": 0
                }
            }
        ],
        "volunteering": None
    }
    print(clean_data(raw_data))
