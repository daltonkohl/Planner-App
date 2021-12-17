from dateutil.parser import parse


class Assignment:
    """
    Class for assignments
    """
    
    def __init__(self, name, date_issued  = "", date_due = "", description = ""):
        """
        Constructor for an assignment object
        @param name: Name of assignment
        @param date_issued: Date that assignment is issued to student
        @param date_due: Date that the assignment is set to be due
        @param description: Description of assignment
        """
        self.name = name
        self.date_issued = date_issued
        self.date_due = date_due
        self.description = description

    def get_name(self):
        """
        Returns name of assignment object
        @return self.name: Name of assignment object
        """
        return self.name

    def set_name(self, name):
        """
        Sets a new name for assignment object
        @param name: Name of assignment
        """
        self.name = name

    def get_date_issued(self):
        """
        Returns the date issued for assignment object
        @return self.date_issued: Date issued of assignment object
        """
        return self.date_issued

    def set_date_issued(self, date_issued):
        """
        Sets a new date issued for assignment object
        @param date_issued: Date that assignment is issued to student
        """
        self.date_issued = date_issued
    
    def get_date_due(self):
        """
        Returns the due date for assignment object
        @return self.date_due: Due date of assignment object
        """
        return self.date_due
    
    def set_date_due(self, date_due):
        """
        Sets a new due date for assignment object
        @param date_due: Date that the assignment is set to be due
        """
        self.date_due = date_due

    def get_description(self):
        """
        Returns the description for assignment object
        @return self.description : Description of assignment object
        """
        return self.description

    def set_description(self, description):
        """
        Sets a new description for assignment
        @param description: Description of assignment
        """    
        self.description = description

    def __str__(self):
        """
        Overloads __str__ function to handle the parameters of an assignment object
        @return string: Returns string containing all parameters of assignment object
        """
        return f"Assignment Name: {self.name}\nDate Issued: {self.date_issued}\nDate Due: {self.date_due}\nDescription: {self.description}"

    def __eq__(self, other):
        """
        Overloads __eq__ function to handle an assignment object
        @param other: Object that self will be compared to
        @return boolean: Returns true if comparison succeeds, false otherwise
        """
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        return (self.name == other.get_name())

    def __lt__(self, other):
        """
        Overloads __lt__ function to handle an assignment object
        @param other: Object that self will be compared to
        @return boolean: Returns true if self's due date is less than other's due date, false otherwise
        """
        return parse(self.date_due) < parse(other.get_date_due())