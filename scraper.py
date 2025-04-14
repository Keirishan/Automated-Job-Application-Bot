from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import os
from dotenv import load_dotenv
import random
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from app import job_role

load_dotenv()
# JOBROLE = input("Enter the Job Role: ")
# JOBROLE = "Data Engineer"
JOBROLE = os.getenv("JOBROLE")
USERNAME = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("PASSWORD")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
LOGIN_URL = "https://www.linkedin.com/login"
JOB_SEARCH_URL = f"https://www.linkedin.com/jobs/search/?keywords={JOBROLE}"

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def random_delay():
    time.sleep(random.uniform(2, 5))

def login(driver):
    driver.get(LOGIN_URL)
    time.sleep(2)

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    login_button.click()
    random_delay()
    print("Logged in successfully!")

def scrape_jobs(driver):
    driver.get(JOB_SEARCH_URL)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "job-card-container"))
        )
    except Exception as e:
        print(f"Timeout or error loading job listings: {e}")
        return []

    jobs = []
    job_cards = driver.find_elements(By.CLASS_NAME, "job-card-container")

    for job in job_cards[:10]:
        try:
            title_element = job.find_element(By.CLASS_NAME, "job-card-list__title--link")
            title = title_element.text
            link = title_element.get_attribute("href")
            try:
                company_element = WebDriverWait(job, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "OCTJiTfuvRoNbAplEIjfcyoefuRMlttDng "))
                )
                location_element = WebDriverWait(job, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "sQKlTTmhEWyOFMaDazSRfzzwTrInZfjXOyhY "))
                )
                company = company_element.text
                location = location_element.text
            except:
                company = "N/A"
                location = "N/A"
            jobs.append({"Title": title, "Company": company, "Link": link, "Location": location})
        except Exception as e:
            print(f"Error scraping job details: {e}")

    return jobs

def main():
    driver = setup_driver()
    login(driver)
    jobs = scrape_jobs(driver)
    if jobs:
        df = pd.DataFrame(jobs)
        df.to_csv("data/applied_jobs.csv", index=False)
        print("Job data saved to CSV!")
        # print("Connecting to MySQL database...")
        # try:
        #     engine = create_engine('mysql+mysqlconnector://root:1234@127.0.0.1:3306/automated_job_application_bot')
        #     df.to_sql('job_details', con=engine, if_exists='replace', index=False)
        #     print("Job details imported to database successfully!")
        # except SQLAlchemyError as e:
        #     print(f"Error connecting to or inserting into database: {e}")
    driver.quit()

if __name__ == "__main__":
    main()