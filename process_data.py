import pandas as pd
import os

# Folder containing the CSV files
data_folder = "data"

# List to store processed data
all_data = []

# Read each CSV file
for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(data_folder, file)

        # Read CSV
        df = pd.read_csv(file_path)

        # Keep only Pink Morsel products
        df = df[df["product"].str.lower() == "pink morsel"]

        # Remove dollar sign and convert price to float
        df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

        # Calculate sales
        df["sales"] = df["quantity"] * df["price"]

        # Convert date format
        df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

        # Keep required columns
        df = df[["sales", "date", "region"]]

        all_data.append(df)

# Combine all files
final_df = pd.concat(all_data, ignore_index=True)

# Save output
final_df.to_csv("output.csv", index=False)

print("Task 2 completed successfully!")
print(final_df.head())