from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os
from dotenv import load_dotenv
import random

load_dotenv()
JOBROLE = input("Enter the Job Role: ")
USERNAME = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("PASSWORD")
LOGIN_URL = "https://www.linkedin.com/login"
JOB_SEARCH_URL = f"https://www.linkedin.com/jobs/search/?keywords={JOBROLE}"

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
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
                    EC.presence_of_element_located((By.CLASS_NAME, "lqQJrmhxpqvSKJwiwrWHrYYjevPYYtO"))
                )
                location_element = WebDriverWait(job, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "kAZRrrWuKGqdPhXjvgNXfpaumZkUtKihsbxw"))
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
        print("Job data saved!")
    driver.quit()

if __name__ == "__main__":
    main()