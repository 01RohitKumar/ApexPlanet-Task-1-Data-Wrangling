# ApexPlanet Task 1 - Data Immersion & Wrangling

## About the Project

This project is part of the **ApexPlanet Data Analytics Internship Program**.

The objective of Task 1 is to understand, profile, clean, transform, and prepare the given sales dataset for further data analysis.

## Dataset Overview

- **Total Rows:** 1,000
- **Total Columns:** 12
- **Dataset Type:** Sales and Customer Data

### Dataset Columns

The dataset contains the following variables:

- Order_ID
- Order_Date
- Customer_ID
- Customer_Name
- Age
- Gender
- City
- Product
- Category
- Quantity
- Unit_Price
- Total_Sales

## Data Quality Checks

The following data quality checks were performed using Python and Pandas:

- Missing value analysis
- Duplicate row detection
- Inconsistent text formatting check
- Outlier detection using the IQR method
- Data type inspection
- Order ID and Customer ID uniqueness check
- Total Sales calculation verification

## Data Cleaning and Transformation

The following cleaning and transformation operations were performed:

- Missing values in the `Age` column were handled using median imputation.
- Missing values in the `City` column were handled using the mode.
- `Order_Date` was converted into a standardized date format.
- Text columns were cleaned using whitespace removal and standardized capitalization.
- The final cleaned dataset was exported as a CSV file.

## Initial Data Quality Findings

- **Missing values before cleaning:** 33
- **Duplicate rows:** 0
- **Missing Age values:** 20
- **Missing City values:** 13

## Project Files

### Python_Code

- `Task1_Data_Immersion_Wrangling.py` - Main data profiling, cleaning, transformation, and output generation script.
- `Data_Dictionary.py` - Script used to create the data dictionary.

### Output

- `Data_Dictionary.xlsx` - Documents the meaning, data type, and business relevance of each variable.
- `cleaned_sales_dataset.csv` - Final analysis-ready cleaned dataset.
- `data_quality_summary.csv` - Summary of the data quality checks and results.

## Tools and Technologies

- Python
- Pandas
- Microsoft Excel
- GitHub

## Task Objective

The final objective of this task is to produce a clean and analysis-ready dataset while documenting the data quality issues and the cleaning process.

## Internship

**ApexPlanet Software Pvt. Ltd.**

**Data Analytics Internship - Task 1: Data Immersion & Wrangling**
