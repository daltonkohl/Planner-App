from datetime import datetime

from Assignment import Assignment


class Class():
    """
    Class for classes in a semester
    """

    def __init__(self, name, start_date = "", end_date = "", teacher = "STAFF TBA"):
        """
        Constructor for a class object
        @param name: Name of class
        @param start_date: Start date of class
        @param end_date: End date of class
        @param teacher: Teacher who oversees class
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.assignments = [] #list of assignments pertaining to the class
        self.teacher = teacher

    def get_name(self):
        """
        Returns name of class object
        @return self.name: Name of class object
        """
        return self.name

    def add_assignment(self, new_assignment):
        """
        Appends a new assignment object to the list of assignments
        @param new_assignment: An assignment object to be added to the list of assignments
        """
        self.assignments.append(new_assignment)

    def get_assignment_names(self):
        """
        Returns list of assignment names pertaining to a class
        @return name_list: List of assignments names pertaining to a class
        """
        name_list = []
        for existing_assignment in self.assignments:
            name_list.append(existing_assignment.get_name())
        return name_list

    def get_assignment(self, existing_assignment):
        """
        Returns an assignment object that matched the assignment name
        @param existing_assignment: Name of an assignment
        @return assignment: Returns assignment object that matched the name of existing_assignment
        """
        for assignment in self.assignments:
            if existing_assignment == assignment.get_name():
                return assignment

    def get_assignments(self):
        """
        Returns list of assignments
        @return self.assignments: Returns list of assignment objects pertaining to the class
        """
        return self.assignments

    def remove_assignment(self, existing_assignment):
        """
        Removes any assignment whose name matches with existing_assignment
        @param existing_assignment: Name of assignment to be removed
        """
        self.assignments.remove(existing_assignment)

    def add_teacher(self, teacher):
        """
        Adds a teacher to the class
        @param teacher: Teacher object to be added to the class
        """
        self.teacher = teacher

    def remove_teacher(self):
        """
        Removes teacher object from class and sets new teacher to 'STAFF TBA'
        """
        self.teacher = "STAFF TBA"

    def get_teacher(self):
        """
        Returns the teacher object
        @return self.teacher: Returns teacher object
        """
        return self.teacher
        
    def __str__(self):
        """
        Overloads __str__ function to handle the parameters of a class object
        @return string: Returns string containing all parameters of class object
        """
        return f"Class: {self.name}\nStart Date: {self.start_date}\nEnd Date: {self.end_date}\nAssignments: {self.get_assignment_names()} \nTeacher: {self.teacher}"