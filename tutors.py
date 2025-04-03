class Tutors:
    def __init__(self, name, total_hours, total_pay):
        self.__name = name
        self.__total_hours = 0
        self.__total_pay = 0
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
        
        key = student_name 
        self.sessions[key] = [date, hours, paid]
