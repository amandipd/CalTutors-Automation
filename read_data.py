import re
import requests
import pandas as pd
from tutors import Tutors
import os


def run():

    # When actually implementing this, we will likely store tutor_name and sheet_url in a databse table or dictionary.
    sheets_url = 'https://docs.google.com/spreadsheets/d/1uPpm1K4f9fx97sO6cTrNqyhBorXxNp9zHgC52wcMKIs/edit?gid=0#gid=0'
    tutor_name = "Aidan"

    convert_url_to_sheets(sheets_url)
    # tutor_object = read_csv_file()
    read_csv_file()

    # print("Tutor Name: " + tutor_object.get_name())

    # print("Tutor Students: " + str(tutor_object.get_sessions()))

    # print("Total Hours: " + str(tutor_object.get_total_hours()))

    # print("Total Pay: " + str(tutor_object.get_total_pay()))

# Find the columns for total hours and total pay





def read_csv_file():
    df = pd.read_csv("downloaded_data.csv")
    cols = find_total_columns(df)
    # os.remove("downloaded_data.csv")  # Remove the file after reading it

# Finds the exact row and column of a string in a pandas datagframe.
def find_string_in_dataframe(df, search_string):
    matches = []

    for col in df.columns:
        exact_matches = df[df[col].astype(str) == search_string]
        
        if not exact_matches.empty:
            for row_idx in exact_matches.index:
                matches.append((row_idx, col))
    
    return matches if matches else None

def convert_url_to_sheets(sheets_url):

    # Extract the document ID from the URL using regex
    doc_id_match = re.search(r'/d/([a-zA-Z0-9_-]+)', sheets_url)
    if not doc_id_match:
        return "Invalid Google Sheets URL"
    doc_id = doc_id_match.group(1)

    # Extract the gid parameter if it exists
    gid_match = re.search(r'gid=([0-9]+)', sheets_url)
    gid_param = ""
    if gid_match:
        gid_param = f"&gid={gid_match.group(1)}"

    new_url = f"https://docs.google.com/spreadsheets/d/{doc_id}/export?format=csv{gid_param}"

    try:
        response = requests.get(new_url)
        response.raise_for_status()  # Raise an error for bad responses

        with open("downloaded_data.csv", "wb") as file:
            file.write(response.content)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


run()
