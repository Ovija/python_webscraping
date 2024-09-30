# Smartphone Comparison

## Project Overview

This project was developed as part of a course, focused on web scraping data analysis. The project comprises two main components: web scraping using Selenium and data management in MariaDB.

## Components:
*  Web Scraping: The script scrapes smartphone data from Galaxus using the Selenium framework and saves it into CSV files.
*  Database Integration: The scraped data is then processed and loaded into a MariaDB database, where it can be queried for further analysis.

## Code Structure:

*  *Start the scraper:*
    The scraped data will be saved into a CSV file named Scrape.csv.
*  **Data Cleaning:
    Data is cleaned and transformed for further steps.
*  **Merge:
    The previously cleaned data is merged with clean smartphone data from another website.
*  **Database Upload Script (VETTIM~2.PY)
    This script reads the scraped CSV files and loads the data into a MariaDB database.
    Ensure that MariaDB is running and you have created the necessary database with credentials.

## Data Stages:
*    Stage1: Raw data from scraping.
*    Stage2: The scraped data is intentionally contaminated for learning purposes to allow for later cleaning using Python.
*    Stage3: Clean/Transformed data.
*    Merge: Merged data


