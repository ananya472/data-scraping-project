import pandas as pd
import requests
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [
    "https://talentedge.com/golden-gate-university/doctor-of-business-administration",
    "https://talentedge.com/iim-kozhikode/professional-certificate-programme-in-hr-management-and-analytics",
    "https://talentedge.com/opjindal-global-business-school/masters-of-business-administration-opj-global-university",
    "https://talentedge.com/esgci-school-of-management-paris/doctorate-of-business-administration-esgci",
    "https://talentedge.com/goa-institute-of-management/exectuive-pg-program-in-health-care-management",
    "https://talentedge.com/iim-lucknow/supply-chain-management",
    "https://talentedge.com/iim-lucknow/advanced-program-in-strategic-management-for-business-excellence",
    "https://talentedge.com/iim-raipur/executive-certificate-program-in-digital-finance",
    "https://talentedge.com/xlri-jamshedpur/executive-certificate-program-in-logistics-and-supply-chain-management",
    "https://talentedge.com/iim-raipur/executive-certificate-program-in-general-management",
    "https://talentedge.com/iim-raipur/post-graduate-executive-certification-in-human-resource-management-iimr-hr",
    "https://talentedge.com/iim-raipur/executive-certificate-program-in-digital-marketing-course",
    "https://talentedge.com/iim-kozhikode/applied-financial-risk-management-course",
    "https://talentedge.com/iim-raipur/certificate-course-machine-learning-for-managers",
    "https://talentedge.com/iim-raipur/certificate-course-strategic-management",
    "https://talentedge.com/iiit-allahabad/big-data-analytics-machine-learning-course-iiit-allahabad",
    "https://talentedge.com/iiit-allahabad/machine-learning-and-big-data-analytics-for-professionals-with-prior-python-knowledge",
    "https://talentedge.com/xlri-jamshedpur/postgraduate-certificate-human-capital-leadership-course",
    "https://talentedge.com/iit-delhi/certificate-programme-in-5g-iot-ai",
    "https://talentedge.com/iim-raipur/certificate-course-project-management",
    "https://talentedge.com/iim-raipur/certificate-human-resource-management-course-iim-raipur",
    "https://talentedge.com/iit-delhi/certificate-program-industrial-design-innovation-entrepreneurship",
    "https://talentedge.com/iim-shillong/pg-certification-human-resource-hr-management",
    "https://talentedge.com/iit-delhi/certificate-course-startup-boot-camp-iit-delhi",
    "https://talentedge.com/ucla-extension/executive-program-strategic-leadership",
    "https://talentedge.com/iim-shillong/pg-certification-human-resource-hr-management",
    "https://talentedge.com/iit-delhi/certificate-program-industrial-design-innovation-entrepreneurship",
    "https://talentedge.com/iit-delhi/certificate-course-startup-boot-camp-iit-delhi",
    "https://talentedge.com/iim-raipur/certificate-course-applied-financial-risk-management",
    "https://talentedge.com/xlri-jamshedpur/digital-marketing-course"
]



def scrape_course_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the title
    title = soup.find('h1').text.strip() if soup.find('h1') else 'N/A'
    
    # Extract the description
    description_div = soup.find('div', class_='desc')
    description = description_div.text.strip() if description_div else 'N/A'
    
    # Extract "What you will learn"
    learn_div = soup.find('div', class_='pl-deeper-undstnd')
    what_you_will_learn = 'N/A'
    if learn_div:
        learn_items = learn_div.find_all('li')
        what_you_will_learn = '; '.join(item.text.strip() for item in learn_items)
    
    # Extract skills
    skills_div = soup.find('div', class_='key-skills-sec')
    skills = 'N/A'
    if skills_div:
        skill_items = skills_div.find_all('li')
        skills = '; '.join(item.text.strip() for item in skill_items)
    
    # Extract faculty information
    faculty_name = 'N/A'
    faculty_designation = 'N/A'
    faculty_description = 'N/A'
    faculty_div = soup.find('div', class_='facutly-card')
    if faculty_div:
        faculty_name_tag = faculty_div.find('h4', class_='best-fname')
        faculty_name = faculty_name_tag.text.strip() if faculty_name_tag else 'N/A'
        faculty_designation_tag = faculty_div.find('p', class_='best-fdesingnation')
        faculty_designation = faculty_designation_tag.text.strip() if faculty_designation_tag else 'N/A'
        faculty_description_tag = faculty_div.find('a', class_='showFacultyDescription')
        if faculty_description_tag:
            faculty_description = faculty_description_tag['data-description'].strip()
    
    # Extract institute name
    institute_name = 'N/A'
    institute_div = soup.find('div', class_='plc-institute')
    if institute_div:
        institute_name_tag = institute_div.find('h4', class_='about-ititle')
        institute_name = institute_name_tag.text.strip() if institute_name_tag else 'N/A'
    

    # Extract syllabus content
    content_div = soup.find('div', class_='sylab-tab-ul')
    content = 'N/A'
    if content_div:
        content_items = content_div.find_all('a')
        content = '; '.join(item.text.strip() for item in content_items)
    
    return {
        'URL': url,
        'Title': title,
        'Description': description,
        'What You Will Learn': what_you_will_learn,
        'Skills': skills,
        'Faculty 1 Name': faculty_name,
        'Faculty 1 Designation': faculty_designation,
        'Faculty 1 Description': faculty_description,
        'Institute Name': institute_name,
        'Content': content,
    }

# Scrape data from all URLs
data = []
for url in urls:
    try:
        data.append(scrape_course_data(url))
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# Create a DataFrame and save it to Excel
df = pd.DataFrame(data)
df.to_excel('courses_data.xlsx', index=False)

print("Data has been saved to courses_data.xlsx")
















