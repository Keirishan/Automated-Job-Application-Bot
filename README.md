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
```
├── app
│   ├── data
│   │   ├── applied_jobs.csv
│   ├── app.py
│   ├── scraper.py
│   ├── requirements.txt
│   ├── .gitignore
│   ├── README.md
│   ├── .env

```

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/Keirishan/Automated-Job-Application-Bot.git
cd linkedin-job-scraper
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Create a .env file
```
LINKEDIN_EMAIL=your_email@example.com
PASSWORD=your_password
DB_USERNAME=your_db_username
DB_PASSWORD=your_db_password
```
4. Run the App
```
streamlit run app.py
```
## 🎯 How to Use
1. Launch the app.
2. Enter your desired job role (e.g., Data Scientist).
3. Select a date filter (defaults to Past 24 hours if not chosen).
4. Click "Scrape Jobs".
5. View results directly in the app or check the data/applied_jobs.csv file.

## 🔒 Note on Usage
This project is intended for educational and research purposes only. Automated scraping of LinkedIn may violate their Terms of Service.

## 📌 Coming Soon
1. Add resume matcher for job relevance score
2. Enhance UI with more filters (location, experience)
3. Schedule scraping with Airflow or Cron

## 👨‍💻 Author
- Keirishan Balachandran - [LinkedIn](https://www.linkedin.com/in/balachandran-keirishan-6a5a66197/)
