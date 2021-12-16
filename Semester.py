from datetime import datetime

from Assignment import Assignment

"""
class Semester:
    def __init__(self, name):
        self.name = name
"""
class Class():
    def __init__(self, name, start_date = "", end_date = "", teacher = "STAFF TBA"):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.assignments = []
        self.teacher = teacher

    def get_name(self):
        return self.name

    def add_assignment(self, new_assignment):
            self.assignments.append(new_assignment)

    def get_assignment_names(self):
        name_list = []
        for existing_assignment in self.assignments:
            name_list.append(existing_assignment.get_name())
        return name_list

    def get_assignment(self, existing_assignment):
        for assignment in self.assignments:
            print(f"assignment: {type(assignment)}")
            print(f"ex assignment: {type(existing_assignment)}")
            if existing_assignment.get_name() == assignment.get_name():
                return assignment

    def get_assignments(self):
        return self.assignments

    def remove_assignment(self, existing_assignment):
        self.assignments.remove(existing_assignment)

    def add_teacher(self, teacher):
        self.teacher = teacher

    def remove_teacher(self):
        self.teacher = "STAFF TBA"
        
    def __str__(self):
        return f"Class: {self.name}\nStart Date: {self.start_date}\nEnd Date: {self.end_date}\nAssignments: {self.get_assignment_names()} \nTeacher: {self.teacher}"

    

