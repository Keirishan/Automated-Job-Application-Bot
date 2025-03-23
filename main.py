from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
# USERNAME = os.getenv("USERNAME")
# PASSWORD = os.getenv("PASSWORD")
JOBROLE = input("Enter the Job Role: ")
USERNAME = "freakinggeek1315@gmail.com"
PASSWORD = "Keiri@1511"
LOGIN_URL = "https://www.linkedin.com/login"
JOB_SEARCH_URL = f"https://www.linkedin.com/jobs/search/?keywords={JOBROLE}"

print(USERNAME)
print(PASSWORD)

def setup_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    print(f"tttttttttt1{driver.page_source}")
    return driver

def setup_driver():
    options = webdriver.ChromeOptions()
    
    # Run browser visibly to mimic a real user
    # options.add_argument("--headless")  # Comment this line

    # Mimic human behavior
    options.add_argument("start-maximized")
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    return driver

import random

def random_delay():
    time.sleep(random.uniform(2, 5))  # Random delay between 2-5 seconds

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
    
    # Wait for job listings to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results__list-item"))
        )
    except:
        print("Timeout: Job listings did not load.")
        return []

    jobs = []
    job_cards = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

    for job in job_cards[:10]:  # Limit to 10 jobs for demo
        try:
            title = job.find_element(By.CLASS_NAME, "job-details-jobs-unified-top-card__job-title").text
            company = job.find_element(By.CLASS_NAME, "job-details-jobs-unified-top-card__company-name").text
            link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
            jobs.append({"Title": title, "Company": company, "Link": link})
        except Exception as e:
            print(f"Skipping job: {e}")  # If a job element is missing, skip it

    return jobs

def main():
    driver = setup_driver()
    login(driver)
    jobs = scrape_jobs(driver)
    df = pd.DataFrame(jobs)
    df.to_csv("data/applied_jobs.csv", index=False)
    print("Job data saved!")
    driver.quit()

if __name__ == "__main__":
    main()
