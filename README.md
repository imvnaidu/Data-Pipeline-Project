# 📊 Data Pipeline Project

## Description
A complete **data pipeline and interactive dashboard** built with **Python**, **SQLite**, and **Streamlit**.  

This project fetches product data from a public API, transforms it (including USD → INR conversion), stores it in an SQLite database, and provides an interactive dashboard to explore and visualize the data. The pipeline tracks execution status automatically to monitor successful or failed runs.  

---

## Features
- **Data Extraction:** Fetches product data from an external API.  
- **Data Transformation:** Converts prices to INR and adds timestamps.  
- **Data Storage:** Saves product data and pipeline status in **SQLite**.  
- **Pipeline Monitoring:** Tracks last run time and success/failure status.  
- **Interactive Dashboard:**  
  - Displays total products and average price metrics.  
  - Shows pipeline status in real-time.  
  - Browsable product table.  
  - Bar chart of average price by category.  
- **Error Handling:** Logs API errors to `error.log`.  

---

## Technologies Used
- Python  
- SQLite  
- Requests  
- Pandas  
- Streamlit
