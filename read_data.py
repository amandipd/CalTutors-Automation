import re
import requests


def read_sheet(sheets_url):

    # Extract the document ID from the URL using regex
    doc_id_match = re.search(r'/d/([a-zA-Z0-9_-]+)', sheets_url)
    if not doc_id_match:
        return "Invalid Google Sheets URL"
    doc_id = doc_id_match.group(1)

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


read_sheet('https://docs.google.com/spreadsheets/d/1jsTdN1fkj_3brJ1H6P_AShoDnsqDdG_iJi6811fL9Jc/edit?gid=0#gid=0')
