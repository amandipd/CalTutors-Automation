import re
import requests
import pandas as pd
import os


def run(sheets_url):
    convert_url_to_sheets(sheets_url)
    read_csv_file()


def read_csv_file():
    df = pd.read_csv("downloaded_data.csv")
    print(df.to_string())
    os.remove("downloaded_data.csv")


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


run('https://docs.google.com/spreadsheets/d/1jsTdN1fkj_3brJ1H6P_AShoDnsqDdG_iJi6811fL9Jc/edit?gid=0#gid=0')
