import pandas as pd
import os


# DATA DICTIONARY - APEXPLANET TASK 1


# Dataset load
file_path = "Dataset/sales_dataset.xlsx"

df = pd.read_excel(file_path)



# DATA DICTIONARY INFORMATION


data_dictionary = pd.DataFrame({

    "Column Name": [
        "Order_ID",
        "Order_Date",
        "Customer_ID",
        "Customer_Name",
        "Age",
        "Gender",
        "City",
        "Product",
        "Category",
        "Quantity",
        "Unit_Price",
        "Total_Sales"
    ],

    "Meaning": [
        "Unique identifier assigned to each order",
        "Date on which the order was placed",
        "Unique identifier assigned to each customer",
        "Name of the customer",
        "Age of the customer",
        "Gender of the customer",
        "City of the customer",
        "Name of the product purchased",
        "Category of the purchased product",
        "Number of units purchased",
        "Price of one unit of the product",
        "Total sales value generated from the order"
    ],

    "Data Type": [
        "String",
        "Date",
        "String",
        "String",
        "Numeric",
        "String",
        "String",
        "String",
        "String",
        "Integer",
        "Float",
        "Float"
    ],

    "Business Relevance": [
        "Used to uniquely identify and track orders",
        "Used for date-wise sales analysis and trends",
        "Used to identify and analyze individual customers",
        "Useful for customer-level analysis",
        "Useful for customer demographic and age-group analysis",
        "Useful for demographic analysis",
        "Useful for geographic and city-wise sales analysis",
        "Useful for product performance analysis",
        "Useful for category-wise sales analysis",
        "Used to analyze product demand and sales volume",
        "Used to analyze pricing and revenue",
        "Used to measure total revenue generated from orders"
    ]
})



# CREATE OUTPUT FOLDER


output_folder = "Output"

os.makedirs(output_folder, exist_ok=True)



# SAVE DATA DICTIONARY


output_file = os.path.join(
    output_folder,
    "Data_Dictionary.xlsx"
)

data_dictionary.to_excel(
    output_file,
    index=False
)



# DISPLAY RESULT


print("============================================================")
print("DATA DICTIONARY CREATED SUCCESSFULLY!")
print("============================================================")

print("\nFile saved at:")
print(output_file)

