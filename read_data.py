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
    read_csv_file(tutor_name)

    # print("Tutor Name: " + tutor_object.get_name())

    # print("Tutor Students: " + str(tutor_object.get_sessions()))

    # print("Total Hours: " + str(tutor_object.get_total_hours()))

    # print("Total Pay: " + str(tutor_object.get_total_pay()))


def read_csv_file(tutor_name):
    # Read CSV without using index_col to preserve the first row
    df = pd.read_csv("downloaded_data.csv")
    os.remove("downloaded_data.csv")  # Remove the file after reading it
    last_col = [df.columns[-1]] + df.iloc[:, -1].tolist()
    total_hours = last_col[0]
    total_pay = last_col[1]

    # Debug
    # print(last_col)
    # print(df)

    curr_tutor = Tutors(tutor_name, total_hours, total_pay, df)
    curr_tutor.print_tutor_sheet()


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
