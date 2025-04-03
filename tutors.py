class Tutors:
    def __init__(self, name, total_hours, total_pay):
        self.__name = name
        self.__total_hours = total_hours
        self.__total_pay = total_pay
        self.__sessions = {}

    # Getters
    def get_name(self):
        return self.__name
    
    def get_total_hours(self):
        return self.__total_hours
    
    def get_total_pay(self):
        return self.__total_pay
    
    def get_sessions(self):
        return self.__sessions
    

    def add_session(self, student_name, date, hours, paid):

        # Session Parameters
        # Key: Tutored Student's Name
        # Value: [Date, Hours, Paid]

        # Ensuring inputs to paid column are valid
        paid = paid.lower()
        if (paid != "yes" and paid != "no" and paid != "true" and paid != "false"):
            paid = "unknown"
        
        key = student_name 

        if key in self.__sessions.keys():
            self.__sessions[key].append([date, hours, paid])
        else:
            self.__sessions[key] = [[date, hours, paid]]
