
from os import name
from Assignment import Assignment


class Person(object):

    def __init__(self, name, username = "", password = ""):
        self.name = name
        self._username = username
        self._password = password

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_username(self):
        return self._username

    def __str__(self):
        return f"Person: {self.name}"

    def save_to_file():
        """
        Future function that saves the object using pyhton pickle module

        """

class Student(Person):
    def __init__(self, name, username, password):
        super().__init__(name, username, password)
        self.classes = []
        self.assignments = [] #(class, assignment)


    #Class related methods
    def add_class(self, new_class, teachers):
        """
        new_class to be a class object
        """
        if(any(i.get_name() == new_class.get_name() for i in self.classes)):
            print("Class already exists")
        else:
            self.classes.append(new_class)
            for teacher in teachers:
                if(teacher.get_class(new_class.get_name()) != -1):
                    for existing_assignment in teacher.get_class(new_class.get_name()).get_assignments():
                        self.add_assignment(new_class, existing_assignment)
                    new_class.add_teacher(teacher)
                    teacher.add_student_to_class(new_class, self)

            print(f"Succesfully added {new_class.get_name()}")

    def get_class(self, class_name):
        """
        If class exist in classes list, returns the class object
        If class does not exist in classes list, returns -1
        """
        for item in self.classes:
            if(item.get_name() == class_name):
                return item
        return -1


    def remove_class(self, existing_class):
        """
        If class exists in classes list, removes class from the classes list
        If class does not exist in classes list, returns -1
        """
        if(any(i.get_name() == existing_class.get_name() for i in self.classes)):
            for assignment_name in existing_class.get_assignment_names():
                self.remove_assignment(existing_class, self.get_assignment(existing_class.get_name(), assignment_name))
            self.classes.remove(existing_class)
        else:
            print("Class does not exist")
            return -1

    def show_classes(self):
        """
        Prints all classes in classes list
        """
        for _class in self.classes:
            print(f"{_class}\n")


    #assignment related methods
    def add_assignment(self, existing_class, new_assignment):
        """
        Function adds assignment to assignment list if the assignment does not already exist
        and the class does exist in the classes list
        Returns 1 upon successful addition
        Returns 0 upon unsuccessful addition
        """

        if((all(i[1].get_name() != new_assignment.get_name() or new_assignment.get_name() not in existing_class.get_assignment_names() for i in self.assignments)) and any(k.get_name() == existing_class.get_name() for k in self.classes)):
            existing_class = self.get_class(existing_class.get_name())
            self.assignments.append((existing_class, new_assignment))
            existing_class.add_assignment(new_assignment)
            print(f"Succesfully added assignment: {new_assignment.get_name()}")
            return 1
        else:
            return 0


    def get_assignment(self, existing_class, existing_assignment):
        for i in self.assignments:
            if(i[0].get_name() == existing_class and i[1].get_name() == existing_assignment):
                return i[1]
        return -1

    def remove_assignment(self, existing_class, existing_assignment):
        if(any(i[0].get_name() == existing_class.get_name() and i[1].get_name() == existing_assignment.get_name() for i in self.assignments)):
            existing_class = self.get_class(existing_class.get_name())
            existing_assignment = self.get_assignment(existing_class.get_name(), existing_assignment.get_name())
            self.assignments.remove((existing_class, existing_assignment))
            existing_assignment = existing_class.get_assignment(existing_assignment.get_name())
            existing_class.remove_assignment(existing_assignment)
            
    def show_assignments(self):
        """"
        Prints all assignments in the class list
        """
        for (existing_class, existing_assignment) in self.assignments:
            print(f"Class: {existing_class.get_name()}\n{existing_assignment}\n")
    
    def get_assignment_names(self):
        name_list = []
        for (existing_class, existing_assignment) in self.assignments:
            name_list.append(existing_assignment.get_name())
        return name_list

    def get_class_list(self):
        return self.classes


    def __str__(self):
        return f"Student: {self.name}\nClasses: {self.classes}\nAssignments: {self.get_assignment_names()}"

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        return (self.name == other.name)


class Teacher(Person):

    def __init__(self, name, username, password):
        super().__init__(name, username, password)
        self.classes = {} #key = class --- value = list of students
        self.assignments = []


    def add_class(self, new_class, students):
        if(any(i.get_name() == new_class.get_name() for i in self.classes.keys())):
            print("Class already exists")
        else:
            self.classes[new_class] = students
            new_class.add_teacher(self)
            for student in students:
                if(student.get_class(new_class.get_name()) != -1):
                    student.get_class(new_class.get_name()).add_teacher(self)
            print(f"Succesfully added {new_class.get_name()}")

    def show_classes(self):
        """
        Prints all classes in classes list
        """
        for _class in self.classes.keys():
            print(f"{_class}\n")

    def remove_class(self, existing_class, students):
        """
        If class exists in classes list, removes class from the classes list
        If class does not exist in classes list, returns -1
        """
        if(any(i.get_name() == existing_class.get_name() for i in self.classes.keys())):
            for assignment_name in existing_class.get_assignment_names():
                self.remove_assignment(existing_class, self.get_assignment(existing_class.get_name(), assignment_name),  students)
            self.classes.pop(existing_class)
            for student in students:
               if(student.get_class(existing_class.get_name()) != -1):
                    student.get_class(existing_class.get_name()).remove_teacher()                
        else:
            print("Class does not exist")
            return -1

    def get_class(self, class_name):
        """
        If class exist in classes list, returns the class object
        If class does not exist in classes list, returns -1
        """
        for item in self.classes.keys():
            if(item.get_name() == class_name):
                return item
        return -1


    def add_assignment(self, existing_class, new_assignment, students):
        """
        Function adds assignment to assignment list if the assignment does not already exist
        and the class does exist in the classes list
        Returns 1 upon successful addition
        Returns 0 upon unsuccessful addition
        """

        if((all(i[1].get_name() != new_assignment.get_name() or new_assignment.get_name() not in existing_class.get_assignment_names() for i in self.assignments)) and any(k.get_name() == existing_class.get_name() for k in self.classes.keys())):
            self.assignments.append((existing_class, new_assignment))
            existing_class.add_assignment(new_assignment)
            for student in students:
                if(student.get_class(existing_class.get_name()) != -1):
                    student.get_class(existing_class.get_name())
                    student.add_assignment(existing_class, new_assignment)
            print(f"Succesfully added assignment: {new_assignment.get_name()}")
            return 1
        else:
            return 0

    def get_assignment(self, existing_class, existing_assignment):
        for i in self.assignments:
            if(i[0].get_name() == existing_class and i[1].get_name() == existing_assignment):
                return i[1]
        return -1

    def show_assignments(self):
        """"
        Prints all assignments in the class list
        """
        for (existing_class, existing_assignment) in self.assignments:
            print(f"Class: {existing_class.get_name()}\n{existing_assignment}\n")

    def get_assignment_names(self):
        name_list = []
        for (existing_class, existing_assignment) in self.assignments:
            name_list.append(existing_assignment.get_name())
        return name_list

    def remove_assignment(self, existing_class, existing_assignment, students):
        if(any(i[0].get_name() == existing_class.get_name() and i[1].get_name() == existing_assignment.get_name() for i in self.assignments)):
            existing_class.remove_assignment(existing_assignment)
            self.assignments.remove((existing_class, existing_assignment))
            for student in students:
                if(student.get_class(existing_class.get_name()) != -1):
                    existing_assignment = student.get_assignment(existing_class.get_name(), existing_assignment.get_name())
                    existing_class = student.get_class(existing_class.get_name())
                    student.remove_assignment(existing_class, existing_assignment)

    def add_student_to_class(self, existing_class, new_student):
        existing_class = self.get_class(existing_class.get_name())
        if(all(i.get_name() != new_student.get_name() for i in self.classes[existing_class])):
            self.classes[existing_class].append(new_student)

    def remove_student_from_classes(self, existing_student):
        for existing_class in self.classes.keys():
            self.classes[existing_class].remove(existing_student)


    def __str__(self):
        return f"{self.name}"






