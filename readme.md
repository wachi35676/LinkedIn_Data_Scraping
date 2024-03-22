# LinkedIn Data Scraper and CSV Generator

This project is designed to scrape LinkedIn profile data using the LinkedIn API and store the data in a CSV file. The script extracts information such as name, job title, company name, experience, education, and other relevant details from LinkedIn profiles.

## Prerequisites

Before running the code, make sure you have the following:

1. **Python 3.x** installed on your system.
2. **RapidAPI Key**: You need to obtain an API key from [RapidAPI](https://rapidapi.com/rockapis-rockapis-default/api/linkedin-api8/). This key is required to access the LinkedIn API.
3. **OpenAI Key**: You need to obtain an API key from [OpenAI](https://platform.openai.com/api-keys). This key is required for data cleaning and formatting using OpenAI's GPT-3.5-turbo-0125 language model.

## Setup

1. Clone or download the project repository to your local machine.
2. Create a new virtual environment for the project using `venv` or `conda`. This step is optional but recommended to keep the project dependencies isolated.
3. Install the required Python packages by running the following command:

   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root directory and add the following lines, replacing `YOUR_RAPID_API_KEY` with your actual RapidAPI key, and `YOUR_OPENAI_KEY` with your actual OpenAI key:

   ```
   RAPID_API_KEY=YOUR_RAPID_API_KEY
   OPENAI_API_KEY=YOUR_OPENAI_KEY
   ```

   The `.env` file is used to store environment variables securely.

5. Create a `sample.csv` file in the project root directory. This file should contain a column named `LinkedIn link` with the LinkedIn profile URLs of the users whose data you want to scrape. The header row should be `LinkedIn link`.

## Usage

To run the script, navigate to the project root directory and execute the following command:

```
python main.py
```

This command will perform the following steps:

1. Extract LinkedIn usernames from the `sample.csv` file.
2. Scrape LinkedIn data for each username using the RapidAPI LinkedIn API.
3. Clean and format the scraped data using OpenAI's GPT-3.5-turbo-0125 language model.
4. Write the cleaned data to a CSV file named `output.csv` in the project root directory.

The `output.csv` file will contain the following columns:

- `FirstName`
- `LastName`
- `CompanyName`
- `Email`
- `LocationCity`
- `JobTitle`
- `LinkedInLink`
- `Experience`
- `UniversityAttendedForBachelorsDegree`
- `BachelorsDegreeFieldOfStudy`
- `UniversityAttendedForMastersDegree`
- `MastersDegreeFieldOfStudy`

## Notes

- Make sure to keep the `.env` file secure and never share your API keys publicly.
- The script uses the OpenAI GPT-3.5-turbo-0125 language model for data cleaning and formatting. This may incur costs based on your OpenAI API usage.
- The script is designed to handle a specific input data format from the LinkedIn API. If the API response format changes, the `gpt_data_cleaning.py` file may need to be updated accordingly.
