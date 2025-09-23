# Café Sales Data Cleaning App

A **Python-based data cleaning tool** for café sales datasets. This project reads raw sales data, cleans and formats it, and outputs a **cleaned dataset** ready for analysis. It can also be extended into a **Streamlit web app** for interactive cleaning.

---

## Features

- Convert numeric columns (`Quantity`, `Price Per Unit`, `Total Spent`) safely.  
- Remove invalid entries (`UNKNOWN`, `ERROR`) in key columns.  
- Handle missing values in important columns (`Item`, `Payment Method`, `Location`, `Transaction Date`).  
- Convert transaction dates to proper datetime format.  
- Remove duplicate rows.  
- Save the cleaned dataset as a new CSV file.

---

## How to Use

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/repo-name.git

Install required packages:
pip install -r requirements.txt 

Run the cleaning script
Dynamic data clean.py

FILES:
Dynamic data clean.py → Main script for data cleaning

datamodel.py → Optional: Contains reusable cleaning functions

requirements.txt → List of required Python packages

README.md → Project description