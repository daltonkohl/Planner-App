import pickle
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *  #QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from Person import *

class GUI(QMainWindow):

    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self._user_dict = {} #{username : password, id, which is the numnber of user it was added as}
        self.user_objs = [] #{username : obj}
        self.user_count = 0
        self.screen = self.app.primaryScreen()
        self.screen_width = self.screen.size().width()
        self.screen_height = self.screen.size().height()
        self.setGeometry(self.screen_width//4, self.screen_height//4, self.screen_width // 2, self.screen_height // 2)
        self.setWindowTitle("Planner App")
        self.showMinimized()
        

    def validate_user(self, username, password):
        """
        Function validates the input username and password with the existing database
        Returns -1 if the username does not exist within the database
        Returns 0 if the password does not match the username
        Returns the Person object if the username and password match 
        """
        if(username not in self._user_dict.keys()):
            #print("Username not in database, please sign up")
            return -1
        elif(self._user_dict[username][0] != password):
            #print("Password does not match username")
            return 0
        else:
            print(f"Succesfully logged in {username}")
            return self.user_objs[self._user_dict[username][1]] #future return value to be 1 , the Person object

    def add_user(self, username, password, name):
        """
        Function adds a username and password to the database if it does not already exist
        Returns user object upon successful addition
        Returns 0 upon unsuccessful addition
        """

        if(username not in self._user_dict.keys()):
            f = open("username_database.txt", 'a')
            temp = self.user_count
            self._user_dict[username] = (password, temp)
            f.write(f"{username},{password},\n")
            f.close()
            user_obj = Student(name, username, password)
            self.user_objs.append(user_obj)
            print(f"{username} successfully added")
            self.user_count += 1
            return user_obj
        else:
            print("Username already exists")
            return 0

    def delete_user(self, username):
        if(username not in self._user_dict.keys()):
            print("user does not exist")
        else:
            user_nmbr = self._user_dict[username][1]

            with open("username_database.txt", "r") as f:
                lines = f.readlines()
            f.close()
            with open("username_database.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != f"{username},{self._user_dict[username][0]},":
                        f.write(line)
            f.close()

            del self._user_dict[username]
            self.user_objs.pop(user_nmbr)
            self.user_count -= 1

            print("user succesfully removed")
        
        
    def log_out(self):
        """
        Future function that will update the database file
        GUI will keep track of 
        """
        with open("user_database.txt", 'wb') as outp:
            for user in self.user_objs:
                pickle.dump(user, outp)
        self._user_dict.clear()
        self.user_objs.clear()
        self.user_count = 0

        outp.close()


    def load(self):
        f = open("username_database.txt", 'r')

        for line in f:
            user_pass = line.split(",")
            self._user_dict[user_pass[0]] = (user_pass[1], self.user_count)
            self.user_count += 1
            

        with open("user_database.txt", 'rb') as inp:
            for i in range(self.user_count):
                self.user_objs.append(pickle.load(inp))

        inp.close()
        f.close()

    def show_login(self):
        self.welcome_label = QLabel(self)
        self.welcome_label.setText("GUI has not yet been implemented, please see Terminal")
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.welcome_label.move(self.screen_width // 2 - self.welcome_label.fontMetrics().boundingRect(self.welcome_label.text()).width() ,self.screen_height // 4 - self.welcome_label.fontMetrics().boundingRect(self.welcome_label.text()).height())
        self.welcome_label.setFont(QFont("Arial", 20))
        self.welcome_label.adjustSize()
        self.welcome_label.show()

        


    def __str__(self):
        return f"number of users: {self.user_count}\nusername log: {self._user_dict}"