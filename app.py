import streamlit as st
import pandas as pd
import subprocess
import os

st.set_page_config(page_title="Job Scraper", layout="centered")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e0ffe0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("LinkedIn Job Scraper")
# page = st.sidebar.selectbox("Go to", ["-- Select Page --", "Home", "Jobs", "About"])
job_role = st.text_input("Enter Job Role:", placeholder="Enter the job role you're interested in")

if st.button("Scrape Jobs"):
    if job_role:
        os.environ["JOBROLE"] = job_role

        # Run the scraping script as a subprocess
        with st.spinner("Scraping jobs... Please wait."):
            result = subprocess.run([os.sys.executable, "scraper.py"], capture_output=True, text=True)

        if result.returncode == 0:
            st.success("Job scraping completed successfully!")
            # Read and show the data
            try:
                df = pd.read_csv("data/applied_jobs.csv")
                st.write("### 💻 Scraped Job Listings")
                st.markdown("----------------------------")
                for idx, row in df.iterrows():
                    col1, col2 = st.columns([4, 1])
                    with col1:
                        st.markdown(f"""
                        **{row['Title']}**  
                        📌 *{row['Location']}*  
                        💼 *{row['Company']}*
                        """)
                    with col2:
                        st.markdown(f"[Apply ⬇️]({row['Link']})", unsafe_allow_html=True)
                    st.markdown("---")


            except FileNotFoundError:
                st.error("CSV file not found. Scraping may have failed.")
        else:
            st.error("Error during scraping:")
            st.code(result.stderr)
    else:
        st.warning("Please enter a job role.")
