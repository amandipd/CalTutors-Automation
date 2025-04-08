# Cal Tutors Sheet Reader

A Python application to manage and track tutor sessions, hours, and payments from Google Sheets data.

## Overview

This system allows tutors to track their sessions with students, calculate total hours worked, and determine payments due. It extracts data from a Google Sheets spreadsheet and processes it into a structured format.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/tutor-management.git
   cd tutor-management
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure your Google Sheets document is accessible (must be publicly viewable or have sharing permissions set)

2. Run the application:
   ```bash
   python read_data.py
   ```

3. To use your own spreadsheet, modify the `sheets_url` variable in `read_data.py` with your Google Sheets URL

## Data Format

Your Google Sheet should be formatted with:
- Date column as the first column
- Student names as column headers
- Hours worked in each cell
- Last column containing summary information (TOTAL HOURS, TOTAL PAY)

Example:
```
DATE,       Maddy, Shiley, Candy, Guillermo, TOTAL HOURS:, 6
2/3/2025,   1,     ,      1,     ,          TOTAL PAY:,    230
2/5/2025,   ,      2,     ,      ,          ,              
2/12/2025,  1,     1,     ,      ,          ,              
```

## Project Structure

- `read_data.py` - Main script for extracting and processing data
- `tutors.py` - Contains Tutors class to manage tutor information
- `requirements.txt` - Lists all dependencies
