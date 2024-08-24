# data-scraping-project

Project Overview
This Python script is designed to automatically scrape data from a list of specified URLs on the TalentEdge website. The script collects detailed information about various online courses offered by different institutions. The data is then stored in an Excel file for further analysis or processing.

Libraries Used: pandas,requests, BeautifulSoup


How the Script Works

List of URLs: The script begins by defining a list of URLs that point to different course pages on the TalentEdge website.
scrape_course_data(url) 

Function: This function accepts a single URL as an argument, makes a GET request to the URL, and then parses the HTML content using BeautifulSoup.

Data Extraction: The script extracts the following information from each course page:
Title: The title of the course.
Description: A brief description of the course.
What You Will Learn: Key learning outcomes listed on the course page.
Skills: Skills that the course will help develop.
Faculty Information: Includes the name, designation, and description of the faculty members.
Institute Name: The name of the institution offering the course.
Content: A list of syllabus content or course modules.
Data Collection:

The script iterates over each URL in the list, calling the scrape_course_data(url) function, and stores the results in a list of dictionaries.
Saving Data:

After collecting the data, the script converts the list of dictionaries into a pandas DataFrame and saves it as an Excel file (courses_data.xlsx).
