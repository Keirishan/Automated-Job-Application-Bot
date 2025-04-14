# 🧠 LinkedIn Job Scraper (Streamlit + Selenium)

A Python-based web scraper that allows users to search for LinkedIn job listings based on job role and date posted. It features a Streamlit frontend and a Selenium backend to automate login and scrape job data dynamically.

---

## 🚀 Features

- 🔍 Search for jobs based on **job title** and **date posted**
- 📆 Filter by:
  - Past 24 hours
  - Past Week
  - Past Month
- 💻 Scraped job details include **Job Title**, **Company**, **Location**, and a **direct application link**
- 🧾 Outputs results in a clean **Streamlit interface** and saves to `data/applied_jobs.csv`
- 🔐 Uses `.env` to securely manage credentials

---

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/)
- [Selenium](https://www.selenium.dev/)
- [ChromeDriverManager](https://pypi.org/project/webdriver-manager/)
- [Python dotenv](https://pypi.org/project/python-dotenv/)
- [Pandas](https://pandas.pydata.org/)
- (Optional) SQLAlchemy for DB integration

---

## 📁 Project Structure

