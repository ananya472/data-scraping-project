# data-scraping-project

Project Overview
This Python script is designed to automatically scrape data from a list of specified URLs on the TalentEdge website. The script collects detailed information about various online courses offered by different institutions. The data is then stored in an Excel file for further analysis or processing.

Libraries Used: pandas,requests, BeautifulSoup

#How the Script Works

1.List of URLs: The script begins by defining a list of URLs that point to different course pages on the TalentEdge website.
2.Function: This function accepts a single URL as an argument, makes a GET request to the URL, and then parses the HTML content using BeautifulSoup.
2.Data Extraction: The script extracts the following information from each course page.
4.Data Collection:The script iterates over each URL in the list, calling the scrape_course_data(url) function, and stores the results in a list of dictionaries.
5.Saving Data: After collecting the data, the script converts the list of dictionaries into a pandas DataFrame and saves it as an Excel file (courses_data.xlsx).

#How to Run the Script

#Prerequisites:
1.Ensure that Python is installed on your system.
2.Install the required libraries

#Steps to Run:

1.Copy the Script: Copy the provided script into a Python file, e.g., scrape_courses.py.

2.Run the Script:

-Open a terminal or command prompt.
-Navigate to the directory where your Python file is saved.
-Run the script using the following command:
python scrape_courses.py

3.Output:
Once the script finishes executing, an Excel file named courses_data.xlsx will be created in the same directory. This file contains the scraped data in a tabular format.


#Sample Data Output
The courses_data.xlsx file will have the following columns:

URL
Title
Description
What You Will Learn
Skills
Faculty 1 Name
Faculty 1 Designation
Faculty 1 Description
Institute Name
Content

Each row corresponds to a different course, with all relevant details extracted from the respective course page.
