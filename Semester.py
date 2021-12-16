from datetime import datetime

"""
class Semester:
    def __init__(self, name):
        self.name = name
"""
class Class():
    def __init__(self, name, start_date = "", end_date = ""):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.assignments = []

    def get_name(self):
        return self.name

    def add_assignment(self, new_assignment):
            self.assignments.append(new_assignment)

    def get_assignment_names(self):
        name_list = []
        for existing_assignment in self.assignments:
            name_list.append(existing_assignment.get_name())
        return name_list

    def remove_assignment(self, existing_assignment):
        self.assignments.remove(existing_assignment)

    def __str__(self):
        return f"Class: {self.name}\nStart Date: {self.start_date}\nEnd Date: {self.end_date}\nAssignments: {self.get_assignment_names()}"

