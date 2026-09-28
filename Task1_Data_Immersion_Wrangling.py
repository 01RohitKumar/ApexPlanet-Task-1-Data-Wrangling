import pandas as pd

file_path = "Dataset/sales_dataset.xlsx"

df = pd.read_excel(file_path)

print("Dataset loaded successfully!")
print(df.head())

print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Data Information ---")
print(df.info())

print("\n--- Statistical Summary ---")
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

print("\n--- Duplicate Rows ---")
duplicate_count = df.duplicated().sum()
print("Total duplicate rows:", duplicate_count)

print("\n--- Duplicate Records ---")
print(df[df.duplicated()])

print("\n--- Unique Gender Values ---")
print(df["Gender"].unique())

print("\n--- Unique City Values ---")
print(df["City"].dropna().unique())

print("\n--- Unique Product Values ---")
print(df["Product"].unique())

print("\n--- Unique Category Values ---")
print(df["Category"].unique())


# TASK 1 - DATA IMMERSION & WRANGLING
# ApexPlanet Data Analytics Internship


import pandas as pd
import os


# 1. LOAD DATA


file_path = "Dataset/sales_dataset.xlsx"

df = pd.read_excel(file_path)

print("Dataset loaded successfully!")



# 2. BASIC DATA PROFILING


print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Data Information ---")
df.info()

print("\n--- Statistical Summary ---")
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())



# 3. DUPLICATE CHECK


print("\n--- Duplicate Rows ---")

duplicate_count = df.duplicated().sum()

print("Total duplicate rows:", duplicate_count)

print("\n--- Duplicate Records ---")
print(df[df.duplicated()])



# 4. INCONSISTENT FORMATTING CHECK


print("\n--- Unique Gender Values ---")
print(df["Gender"].unique())

print("\n--- Unique City Values ---")
print(df["City"].dropna().unique())

print("\n--- Unique Product Values ---")
print(df["Product"].unique())

print("\n--- Unique Category Values ---")
print(df["Category"].unique())



# 5. VALUE COUNTS FOR TEXT COLUMNS


print("\n--- Gender Value Counts ---")
print(df["Gender"].value_counts(dropna=False))

print("\n--- City Value Counts ---")
print(df["City"].value_counts(dropna=False))

print("\n--- Product Value Counts ---")
print(df["Product"].value_counts(dropna=False))

print("\n--- Category Value Counts ---")
print(df["Category"].value_counts(dropna=False))



# 6. OUTLIER DETECTION USING IQR


def detect_outliers(dataframe, column):

    Q1 = dataframe[column].quantile(0.25)
    Q3 = dataframe[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = dataframe[
        (dataframe[column] < lower_bound) |
        (dataframe[column] > upper_bound)
    ]

    print(f"\n--- Outlier Check: {column} ---")
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)
    print("Number of Outliers:", len(outliers))

    return outliers


# Check numerical columns

age_outliers = detect_outliers(df, "Age")

quantity_outliers = detect_outliers(df, "Quantity")

price_outliers = detect_outliers(df, "Unit_Price")

sales_outliers = detect_outliers(df, "Total_Sales")



# 7. CREATE COPY FOR CLEANING


cleaned_df = df.copy()



# 8. HANDLE MISSING VALUES


print("\n--- Missing Values Before Cleaning ---")
print(cleaned_df.isnull().sum())


# Age → Median imputation

age_median = cleaned_df["Age"].median()

cleaned_df["Age"] = cleaned_df["Age"].fillna(age_median)


# City → Mode imputation

city_mode = cleaned_df["City"].mode()[0]

cleaned_df["City"] = cleaned_df["City"].fillna(city_mode)


print("\n--- Missing Values After Cleaning ---")
print(cleaned_df.isnull().sum())



# 9. STANDARDIZE DATE FORMAT


print("\n--- Order_Date Data Type Before Conversion ---")
print(cleaned_df["Order_Date"].dtype)


cleaned_df["Order_Date"] = pd.to_datetime(
    cleaned_df["Order_Date"],
    errors="coerce"
)


print("\n--- Order_Date Data Type After Conversion ---")
print(cleaned_df["Order_Date"].dtype)



# 10. STANDARDIZE TEXT COLUMNS


text_columns = [
    "Gender",
    "City",
    "Product",
    "Category"
]

for column in text_columns:

    cleaned_df[column] = (
        cleaned_df[column]
        .astype(str)
        .str.strip()
    )


# Standardize Gender capitalization

cleaned_df["Gender"] = cleaned_df["Gender"].str.title()


# Standardize City capitalization

cleaned_df["City"] = cleaned_df["City"].str.title()


# Standardize Product capitalization

cleaned_df["Product"] = cleaned_df["Product"].str.title()


# Standardize Category capitalization

cleaned_df["Category"] = cleaned_df["Category"].str.title()


print("\n--- Text Standardization Completed ---")



# 11. CHECK ID DUPLICATES


print("\n--- Order ID Check ---")

print("Total Order IDs:", cleaned_df["Order_ID"].count())

print("Unique Order IDs:", cleaned_df["Order_ID"].nunique())


print("\n--- Customer ID Check ---")

print("Total Customer IDs:", cleaned_df["Customer_ID"].count())

print("Unique Customer IDs:", cleaned_df["Customer_ID"].nunique())



# 12. CHECK TOTAL SALES CALCULATION


cleaned_df["Calculated_Total_Sales"] = (
    cleaned_df["Quantity"] * cleaned_df["Unit_Price"]
)


cleaned_df["Sales_Difference"] = (
    cleaned_df["Total_Sales"]
    - cleaned_df["Calculated_Total_Sales"]
)


print("\n--- Total Sales Verification ---")

print(
    "Rows where Total_Sales does not match Quantity × Unit_Price:",
    (cleaned_df["Sales_Difference"].abs() > 0.01).sum()
)



# 13. REMOVE TEMPORARY CALCULATION COLUMNS


cleaned_df.drop(
    columns=[
        "Calculated_Total_Sales",
        "Sales_Difference"
    ],
    inplace=True
)



# 14. CHECK FINAL DATA QUALITY


print("\n--- FINAL DATA QUALITY CHECK ---")

print("\nShape:")
print(cleaned_df.shape)

print("\nMissing Values:")
print(cleaned_df.isnull().sum())

print("\nDuplicate Rows:")
print(cleaned_df.duplicated().sum())

print("\nData Types:")
print(cleaned_df.dtypes)



# 15. CREATE OUTPUT FOLDER


output_folder = "Output"

os.makedirs(output_folder, exist_ok=True)



# 16. SAVE CLEANED DATASET


output_file = os.path.join(
    output_folder,
    "cleaned_sales_dataset.csv"
)

cleaned_df.to_csv(
    output_file,
    index=False
)


print("\n============================================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY!")
print("============================================================")

print("\nCleaned dataset saved at:")
print(output_file)



# 17. SAVE DATA QUALITY SUMMARY


quality_summary = pd.DataFrame({
    "Metric": [
        "Total Rows",
        "Total Columns",
        "Total Missing Values Before Cleaning",
        "Total Missing Values After Cleaning",
        "Duplicate Rows Before Cleaning",
        "Duplicate Rows After Cleaning",
        "Age Outliers",
        "Quantity Outliers",
        "Unit Price Outliers",
        "Total Sales Outliers"
    ],

    "Value": [
        len(df),
        len(df.columns),
        df.isnull().sum().sum(),
        cleaned_df.isnull().sum().sum(),
        df.duplicated().sum(),
        cleaned_df.duplicated().sum(),
        len(age_outliers),
        len(quantity_outliers),
        len(price_outliers),
        len(sales_outliers)
    ]
})


quality_file = os.path.join(
    output_folder,
    "data_quality_summary.csv"
)

quality_summary.to_csv(
    quality_file,
    index=False
)


print("\nData quality summary saved at:")
print(quality_file)



# 18. FINAL PREVIEW


print("\n--- FINAL CLEANED DATA PREVIEW ---")
print(cleaned_df.head())

print("\n--- FINAL CLEANED DATA INFO ---")
cleaned_df.info()

print("\nTask 1 processing completed.")