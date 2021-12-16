import pickle
from Person import *
import datetime

class Backend():

    def __init__(self):
        self._user_dict = {} #{username : password, id, which is the numnber of user it was added as}
        self.user_objs = [] #{username : obj}
        self.user_count = 0

    def encrypt(self, word):
        c = ''
        for i in word:
            if (i == ' '):
                c += ' '
            else:
                c += (chr(ord(i) + 3))
        return c

    def decrypt(self, word):
        c = ''
        for i in word:
            if (i == ' '):
                c += ' '
            else:
                c += (chr(ord(i) - 3))
        return c
        

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

    def add_user(self, username, password, name, user_type):
        """
        Function adds a username and password to the database if it does not already exist
        Returns user object upon successful addition
        Returns 0 upon unsuccessful addition
        """

        if(username not in self._user_dict.keys()):
            f = open("username_database.txt", 'a')
            temp = self.user_count
            self._user_dict[username] = (password, temp)
            f.write(f"{self.encrypt(username)},{self.encrypt(password)},\n")
            f.close()
            if(user_type == "1"):
                user_obj = Student(name, username, password)
            else:
                user_obj = Teacher(name, username, password)
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
                    if line.strip("\n") != f"{self.encrypt(username)},{self.encrypt(self._user_dict[username][0])},":
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

    def get_students(self):
        temp = []
        for user in self.user_objs:
            if(type(user) == Student):
                temp.append(user)
        return temp
    
    def get_teachers(self):
        temp = []
        for user in self.user_objs:
            if(type(user) == Teacher):
                temp.append(user)
        return temp

    def get_user(self, user_name):
        for user in self.user_objs:
            if(user_name == user.get_username()):
                return user
                 
    def get_current_date(self):
        now = str(datetime.datetime.now())
        now = now.split()[0].split("-")
        month, day, year = now[1], now[2], now[0]
        date = f"{month}/{day}/{year}"
        return date


    def load(self):
        f = open("username_database.txt", 'r')

        for line in f:
            user_pass = line.split(",")
            self._user_dict[self.decrypt(user_pass[0])] = (self.decrypt(user_pass[1]), self.user_count)
            self.user_count += 1
            

        with open("user_database.txt", 'rb') as inp:
            for i in range(self.user_count):
                self.user_objs.append(pickle.load(inp))

        inp.close()
        f.close()



    def __str__(self):
        return f"number of users: {self.user_count}\nusername log: {self._user_dict} user_objs:{self.user_objs}"