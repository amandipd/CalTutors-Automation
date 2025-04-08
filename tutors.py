import pandas as pd


class Tutors:
    def __init__(self, name, total_hours, total_pay, dataframe):
        self.__name = name
        self.__total_hours = total_hours
        self.__total_pay = total_pay
        self.__sessions = {}  # Initialize as empty dictionary
        self.__dataframe = dataframe
        self.create_student_sessions_map()

    # Getters
    def get_name(self):
        return self.__name

    def get_total_hours(self):
        return self.__total_hours

    def get_total_pay(self):
        return self.__total_pay

    def get_sessions(self):
        return self.__sessions

    def print_tutor_sheet(self):
        print("Total Hours: " + str(self.__total_hours))
        print("Total Pay: " + str(self.__total_pay))
        for student in self.__sessions:
            print("Student: " + student + " Sessions: " + str(self.__sessions[student]))

    def create_student_sessions_map(self):
        '''
        Creates a hashmap (dictionary) where:
        Keys are student names (column headers)
        Values are lists of [date, hours] pairs
        and stores it in self.__sessions
        '''
        # Get the column headers (student names)
        student_names = self.__dataframe.columns
        
        # For each student, create a list of [date, hours] pairs
        for student in student_names:
            # Skip if student name is not a string, is empty, or is purely numeric
            if not isinstance(student, str) or not student.strip() or student.strip().isdigit():
                continue
                
            # Get all non-empty values for this student
            student_data = self.__dataframe[student].dropna()
            
            # Create list of [date, hours] pairs
            sessions = []
            for idx, hours in student_data.items():
                if pd.notna(hours) and hours != '':
                    try:
                        # Convert hours to integer
                        hours_int = int(float(hours))
                        date = self.__dataframe.iloc[idx,0]

                        sessions.append([date, hours_int])
                    except (ValueError, TypeError):
                        # Skip if hours cannot be converted to integer
                        continue
            
            # Only add students who have sessions
            if sessions:
                self.__sessions[student] = sessions

        
        
