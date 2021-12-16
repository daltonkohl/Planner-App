from dateutil.parser import parse

"""
Class for general assignments
"""

class Assignment:
    def __init__(self, name, date_issued  = "", date_due = "", date_completed = ""):
        self.name = name
        self.date_issued = date_issued
        self.date_due = date_due
        self.date_completed = date_completed

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_date_issued(self):
        return self.date_issued

    def set_date_issued(self, date_issued):
        self.date_issued = date_issued
    
    def get_date_due(self):
        return self.date_due
    
    def set_date_due(self, date_due):
        self.date_due = date_due
    
    def get_date_completed(self):
        return self.date_completed
    
    def set_date_completed(self, date_completed):
        self.date_completed = date_completed

    def __str__(self):
        return f"Assignment Name: {self.name}\nDate Issued: {self.date_issued}\nDate Due: {self.date_due}\nDate Completed: {self.date_completed}"

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        return (self.name == other.get_name())

    def __lt__(self, other):
        return parse(self.date_due) < parse(other.get_date_due())

"""
Class for reading assignments
"""

class ReadingAssignment(Assignment): 
    def __init__(self, assignmentName, dateIssued, dateDue, dateCompleted, pages, bookTitle):
        super.__init__(assignmentName, dateIssued, dateDue, dateCompleted)
        self.pages = pages
        self.bookTitle = bookTitle

    def getPages(self):
        return self.pages

    def setPages(self, pages):
        self.pages = pages

    def getBookTitle(self):
        return self.bookTitle

    def setBookTitle(self, bookTitle):
        self.bookTitle = bookTitle

    def __str__(self):
        return f"{super.__str__(self)}\nPages: {self.pages}\nBook Title: {self.bookTitle}"

"""
Class for test assignments
"""

class TestAssignment(Assignment): 
    def __init__(self, assignmentName, dateIssued, dateDue, dateCompleted, chaptersCovered):
        super.__init__(assignmentName, dateIssued, dateDue, dateCompleted)
        self.chaptersCovered = chaptersCovered

    def getChaptersCovered(self):
        return self.chaptersCovered

    def setChaptersCovered(self, chaptersCovered):
        self.chaptersCovered = chaptersCovered

    def __str__(self):
        return f"{super.__str__(self)}\nChapters Covered: {self.chaptersCovered}"

"""
Class for homework assignments
"""

class HomeworkAssignment(Assignment): 
    def __init__(self, assignmentName, dateIssued, dateDue, dateCompleted, problems = []):
        super.__init__(assignmentName, dateIssued, dateDue, dateCompleted)
        self.problems = problems

    def getProblems(self):
        return self.problems

    def setProblems(self, problems):
        self.problems = problems

    def __str__(self):
        return f"{super.__str__(self)}\nProblems: {self.problems}"  