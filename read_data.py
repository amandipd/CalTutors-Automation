import re
import requests
import pandas as pd
from tutors import Tutors
import os


def run():
    sheets_url = 'https://docs.google.com/spreadsheets/d/1jsTdN1fkj_3brJ1H6P_AShoDnsqDdG_iJi6811fL9Jc/edit?gid=0#gid=0'
    convert_url_to_sheets(sheets_url)
    tutor_object = read_csv_file()

    print("Tutor Name: " + tutor_object.get_name())

    print("Tutor Students: " + str(tutor_object.get_sessions()))

    print("Total Hours: " + str(tutor_object.get_total_hours()))

    print("Total Pay: " + str(tutor_object.get_total_pay()))


def read_csv_file():
    df = pd.read_csv("downloaded_data.csv")
    os.remove("downloaded_data.csv")  # Remove the file after reading it

    # Get tutor name and convert to title case
    tutor_name = df.columns.tolist()[0].title()
    total_hours = df.at[0, 'TOTAL HOURS']
    print(total_hours)
    total_pay = df.at[0, 'TOTAL PAY']

    # Delete name, TOTAL HOURS, and TOTAL PAY columns as they are no longer needed
    df = df.drop(df.columns[0], axis=1)
    df = df.drop("TOTAL HOURS", axis=1)
    df = df.drop("TOTAL PAY", axis=1)

    # print(tutor_name, total_hours, total_pay) # DEBUG
    tutor_object = Tutors(tutor_name, total_hours, total_pay)

    for __, row in df.iterrows():
        student_name = row['STUDENT']
        date = row['DATE']
        hours = row['HOURS']
        paid = row['PAID']

        tutor_object.add_session(student_name, date, hours, paid)

    return tutor_object


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
