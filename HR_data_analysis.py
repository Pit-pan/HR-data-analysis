import pandas as pd
import re
from sqlalchemy import create_engine

"""The purpose of the script is ETL of some fictitious HR data.
    It performs a basic clean-up of the data before sending it to an SQL server
    for further processing."""

#Importing data from the csv file
data = pd.read_csv("hr_raw_data.csv", index_col = "EmployeeNumber")

#Looking for duplicated rows and deleting them if present

duplicate_count = data.duplicated().sum()
if duplicate_count == 0:
    print("No duplicated rows")
else:
    print(f"There are {duplicate_count} duplicated rows.")
    data = data.drop_duplicates()
    print("Duplicated rows have been deleted")

#Removing spcaes before and after string values

for col in data.select_dtypes("object"):
    data[col] = data[col].str.strip()

print("String values cleaned up.")

#Replacing yes/no or lub y/n values with 1/0
regex_pat_yes = re.compile("^yes$", flags = re.IGNORECASE)
regex_pat_no = re.compile("^no$", flags = re.IGNORECASE)
data = data.replace(regex_pat_yes, 1, regex = True)
data = data.replace(regex_pat_no, 0, regex = True)

print("Replaced yes/no values with 1/0.")

#Counting NULL values (without modifying/deleting them)

empty_values_count = data.isna().sum().sum()
if empty_values_count == 0:
    print(f"There are no empty values.")
else:
    print(f"There are {empty_values_count} empty values")

#Sending data to my SQL database
engine = create_engine(
    "postgresql+psycopg2://LOGIN:PASSWORD@localhost:5432/hr_analysis"
)

data.to_sql("hr_data", engine, if_exists = "replace", index = True, index_label = "EmployeeNumber")
print("Data sent to the SQL Server successfully.")