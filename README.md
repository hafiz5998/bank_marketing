
BANK MARKETING DATA - SCHEMA DESIGN, TRANSFORMATION & VISUALIZATION
====================================================================

Description:
------------
This project processes the Bank Marketing Dataset (`bank.csv`) using DuckDB to normalize and structure the data into dimension and fact tables following a star schema. It also includes a Streamlit app for interactive visualization and exploration of the transformed data.



Setup & Execution
=================

Step 1: Install Dependencies
----------------------------
Ensure you have Python installed, then run:

python main_script.py



STREAMLIT APP USAGE
====================

Overview:
---------
The Streamlit app provides an interactive dashboard to explore the transformed bank marketing dataset.

Follow these steps to run the app locally:

1. Install Required Libraries
-----------------------------
Open a terminal and run:

go into myApp folder directory


2. Launch the Streamlit App
---------------------------
Start the app using:

    streamlit run app.py

This will:
- Open a new browser tab with the dashboard
- Load data from the DuckDB database and display key statistics and filters

5. Use the Dashboard
--------------------
- View customer demographics
- Filter by job, education, marital status, etc.
- Explore deposit outcomes and campaign effectiveness

Enjoy exploring the bank marketing data interactively!
