from os import name
from Assignment import Assignment


class Person(object):
    """
    Class for person -- super class for student and teacher
    """

    def __init__(self, name, username = "", password = ""):
        """
        Constuctor for a person object
        @param name: Name of person
        @param username: Username login credential for person
        @param password: Password login credential for person
        """
        self.name = name
        self._username = username
        self._password = password

    def get_name(self):
        """
        Returns name of person
        @return self.name: Name of person object
        """
        return self.name

    def set_name(self, name):
        """
        Sets a new name for the person object
        @param name: Name for person object
        """
        self.name = name

    def get_username(self):
        """
        Returns username of person object
        @return self.username: Username of person object
        """
        return self._username

    def __str__(self):
        """
        Overloads __str__ function to handle the parameters of a person object
        @return string: Returns string containing name of person object
        """
        return f"Person: {self.name}"

class Student(Person):

    def __init__(self, name, username, password):
        """
        Constuctor for a student object
        @param name: Name of student
        @param username: Username login credential for student
        @param password: Password login credential for student
        """
        super().__init__(name, username, password)
        self.classes = [] #class list pertaining to student
        self.assignments = [] #(class, assignment) tuple pertaining to student

    #Class related methods
    def add_class(self, new_class, teachers):
        """
        Adds a class to the list of classes
        @param new_class: Class object to be added
        @param teachers: List of all teacher objects
        """
        #if the class exists in the list of existing classes
        if(any(i.get_name() == new_class.get_name() for i in self.classes)):
            print("Class already exists")
        else:
            self.classes.append(new_class)
            for teacher in teachers:
                #if class does not already exist for teacher
                if(teacher.get_class(new_class.get_name()) != -1):
                    for existing_assignment in teacher.get_class(new_class.get_name()).get_assignments():
                        self.add_assignment(new_class, existing_assignment)
                    new_class.add_teacher(teacher)
                    teacher.add_student_to_class(new_class, self)

            print(f"Succesfully added {new_class.get_name()}")

    def get_class(self, class_name):
        """
        Return a class object that matches class_name
        @param class_name: Name of class to be looked for
        @return item: Returns class object if found
        @return -1: Return -1 if class object is not found
        """
        for item in self.classes:
            if(item.get_name() == class_name):
                return item
        return -1

    def remove_class(self, existing_class):
        """
        Removes class object from class list
        @param existing_class: Name of class to be removed
        @return -1: Returns -1 if class was not found and removed
        """
        #if class exists in list of classes
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
        Adds assignment to assignment list if the assignment does not already exist 
        and the class does exist in the classes list
        @param existing_class: Name of class where assignment needs to be added
        @param new_assignment: Assignment object to be added
        @return 0: Returns 0 upon unsuccessful addition
        @return 1: Returns 1 upon successful addition
        """
        #if class assignment pair does not already exist in the assignments list and the class exists in the class list
        if((all(i[1].get_name() != new_assignment.get_name() or new_assignment.get_name() not in existing_class.get_assignment_names() for i in self.assignments)) and any(k.get_name() == existing_class.get_name() for k in self.classes)):
            #get correct class object
            existing_class = self.get_class(existing_class.get_name())
            self.assignments.append((existing_class, new_assignment))
            existing_class.add_assignment(new_assignment)
            print(f"Succesfully added assignment: {new_assignment.get_name()}")
            return 1
        else:
            return 0

    def get_assignment(self, existing_class, existing_assignment):
        """
        Returns specific assignment object in a class
        @param existing_class: Name of class where assignment exists
        @param existing_assignment: Name of assignment object that needs to be returned
        @return Assignment: Returns assignment object if found
        @return -1: Returns -1 if assignment object if not found
        """
        for i in self.assignments:
            if(i[0].get_name() == existing_class and i[1].get_name() == existing_assignment):
                return i[1]
        return -1

    def remove_assignment(self, existing_class, existing_assignment):
        """
        Removes an assignment from a class
        @param existing_class: Name of class where assignment exists
        @param existing_assignment: Name of assignment object that needs to be removed
        """
        #if the class assignment pair exist in the assignments list
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
        """
        Returns a list of assignment names
        @return name_list: Returns list of assignment names
        """
        name_list = []
        for (existing_class, existing_assignment) in self.assignments:
            name_list.append(existing_assignment.get_name())
        return name_list

    def get_class_list(self):
        """
        Returns list of classes
        @return self.classes: List of classes pertaining to student
        """
        return self.classes

    def __str__(self):
        """
        Overloads __str__ function to handle the parameters of a student object
        @return string: Returns string containing name, classes, and assignment names of student object
        """
        return f"Student: {self.name}\nClasses: {self.classes}\nAssignments: {self.get_assignment_names()}"

    def __eq__(self, other):
        """
        Overloads __eq__ function to handle a student object
        @param other: Object that self will be compared to
        @return boolean: Returns true if comparison succeeds, false otherwise
        """
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        return (self.name == other.name)

class Teacher(Person):

    def __init__(self, name, username, password):
        """
        Constuctor for a teacher object
        @param name: Name of teacher
        @param username: Username login credential for teacher
        @param password: Password login credential for teacher
        """
        super().__init__(name, username, password)
        self.classes = {} #key = class --- value = list of students
        self.assignments = [] #(class, assignment)

    #class related methods
    def add_class(self, new_class, students):
        """
        Adds a class to the dictionary of classes
        @param new_class: Class object to be added
        @param students: List of all student objects
        """
        #if class exists in the classes list
        if(any(i.get_name() == new_class.get_name() for i in self.classes.keys())):
            print("Class already exists")
        else:
            #adds class and students list to the dictionary
            self.classes[new_class] = students
            new_class.add_teacher(self)
            #adds teacher to all students enrolled in the class
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
        Removes class object from class list, removes from students class lists as well
        @param existing_class: Name of class to be removed
        @param students: List of student objects
        @return -1: Returns -1 if class was not found and removed
        """
        #if class exists in class list
        if(any(i.get_name() == existing_class.get_name() for i in self.classes.keys())):
            for assignment_name in existing_class.get_assignment_names():
                self.remove_assignment(existing_class, self.get_assignment(existing_class.get_name(), assignment_name),  students)
            self.classes.pop(existing_class)
            #removes teacher from all students enrolled in the class
            for student in students:
               if(student.get_class(existing_class.get_name()) != -1):
                    student.get_class(existing_class.get_name()).remove_teacher()                
        else:
            print("Class does not exist")
            return -1

    def get_class(self, class_name):
        """
        Return a class object that matches class_name
        @param class_name: Name of class to be looked for
        @return item: Returns class object if found
        @return -1: Returns -1 if class object is not found
        """
        for item in self.classes.keys():
            if(item.get_name() == class_name):
                return item
        return -1

    #assignment related methods
    def add_assignment(self, existing_class, new_assignment, students):
        """
        Adds assignment to assignment list if the assignment does not already exist and the class 
        does exist in the classes list, adds assignment to students in the class as well
        @param existing_class: Name of class where assignment needs to be added
        @param new_assignment: Assignment object to be added
        @param students: List of student objects
        @return 0: Returns 0 upon unsuccessful addition
        @return 1: Returns 1 upon successful addition
        """
        #if class assignment pair does not already exist in the assignments list and the class exists in the class list
        if((all(i[1].get_name() != new_assignment.get_name() or new_assignment.get_name() not in existing_class.get_assignment_names() for i in self.assignments)) and any(k.get_name() == existing_class.get_name() for k in self.classes.keys())):
            self.assignments.append((existing_class, new_assignment))
            existing_class.add_assignment(new_assignment)
            #adds assignment for each student in the class
            for student in students:
                if(student.get_class(existing_class.get_name()) != -1):
                    student.get_class(existing_class.get_name())
                    student.add_assignment(existing_class, new_assignment)
            print(f"Succesfully added assignment: {new_assignment.get_name()}")
            return 1
        else:
            return 0

    def get_assignment(self, existing_class, existing_assignment):
        """
        Returns specific assignment object in a class
        @param existing_class: Name of class where assignment exists
        @param existing_assignment: Name of assignment object that needs to be returned
        @return Assignment: Returns assignment object if found
        @return -1: Returns -1 if assignment object if not found
        """
        for i in self.assignments:
            #if class assignment pair exists in the assignment list
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
        """
        Returns a list of assignment names
        @return name_list: Returns list of assignment names
        """
        name_list = []
        for (existing_class, existing_assignment) in self.assignments:
            name_list.append(existing_assignment.get_name())
        return name_list

    def remove_assignment(self, existing_class, existing_assignment, students):
        """
        Removes an assignment from a class, removes them from all students who are in the class as well
        @param existing_class: Name of class where assignment exists
        @param existing_assignment: Name of assignment object that needs to be removed
        @param students: List of student objects
        """
        #if class assignment pair exists in the assignments list
        if(any(i[0].get_name() == existing_class.get_name() and i[1].get_name() == existing_assignment.get_name() for i in self.assignments)):
            existing_class.remove_assignment(existing_assignment)
            self.assignments.remove((existing_class, existing_assignment))
            #removes assignment for all students in the class
            for student in students:
                if(student.get_class(existing_class.get_name()) != -1):
                    existing_assignment = student.get_assignment(existing_class.get_name(), existing_assignment.get_name())
                    existing_class = student.get_class(existing_class.get_name())
                    student.remove_assignment(existing_class, existing_assignment)

    def add_student_to_class(self, existing_class, new_student):
        """
        Add a student to a class
        @param existing_class: Name of class that student is added to
        @param new_student: Student object that is added to class
        """
        existing_class = self.get_class(existing_class.get_name())
        #if student is not in student list in the classes dictionary
        if(all(i.get_name() != new_student.get_name() for i in self.classes[existing_class])):
            self.classes[existing_class].append(new_student)

    def remove_student_from_classes(self, existing_student):
        """
        Remove student from classes
        @param existing_student: Student object to be removed from classes
        """
        for existing_class in self.classes.keys():
            self.classes[existing_class].remove(existing_student)

    def __str__(self):
        """
        Overloads __str__ function to handle the parameters of a teacher object
        @return string: Returns string containing name of teacher object
        """
        return f"{self.name}"