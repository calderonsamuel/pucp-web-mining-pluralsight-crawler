import json
import pandas as pd

def create_df(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Create a list of dictionaries to hold the DataFrame data
    df_data = []
    for href, children in data.items():
        for child in children:
            df_data.append({'Href': href, 'Child': child})
    
    # Create a DataFrame
    df = pd.DataFrame(df_data)
    return df

file_path = "href_children.json"
df = create_df(file_path)

new_columns = ["Type", "Name", "Teacher", "Level", "Duration", "Date", "Votes"]
df[new_columns] = df["Child"].str.split("\n", expand=True)

# Parse the 'Date' column to datetime format
df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y")

# Remove the "by " string from the "Teacher" column
df["Teacher"] = df["Teacher"].str.replace("^by ", "", regex=True)

# Sort the DataFrame by 'Date_clean' in descending order
df_sorted = df.sort_values(by="Date", ascending=False)

# Drop the 'Child' column
df_sorted = df_sorted.drop(columns=["Child"])

print(df["Date"])
print(df_sorted["Teacher"])

# Save the sorted DataFrame as a CSV file
df_sorted.to_csv("dataset_cursos.csv", index=False)