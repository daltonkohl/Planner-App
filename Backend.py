import pickle
from Person import *
import datetime

class Backend():
    """
    Class for Backend
    """

    def __init__(self):
        """
        Sets inital values for self._user_dict, self.user_objs, and self.user_count
        """
        self._user_dict = {} #{username : password, id, which is the numnber of user it was added as}
        self.user_objs = [] #{username : obj}
        self.user_count = 0

    def encrypt(self, word):
        """
        Encrypts the designated word
        @param word: the word to be encrypted
        @ return c: the encrypted word
        """
        c = ''
        for i in word:
            if (i == ' '):
                c += ' '
            else:
                c += (chr(ord(i) + 3))
        return c

    def decrypt(self, word):
        """
        Decrypts the designated word
        @param word: the word to be decrypted
        @return c: the decrypted word
        """
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
        @param username: the username of the user
        @param password: the password of the user
        @return -1: returns -1 if the username does not exist within the database
        @return 0: returns 0 if the password does not match the username
        @return self.user_objs[self._user_dict[username][1]]: returns the Person object if the username and password match 
        """
        #if username does not exist
        if(username not in self._user_dict.keys()):
            return -1
        #if password does not match username
        elif(self._user_dict[username][0] != password):
            return 0
        else:
            print(f"Succesfully logged in {username}")
            return self.user_objs[self._user_dict[username][1]]

    def add_user(self, username, password, name, user_type):
        """
        Function adds a username and password to the database if it does not already exist
        @param username: the username of the user
        @param password: the password of the user
        @param name: the name of the user
        @param user_type: the type of user (Student or Teacher)
        @return user_obj: returns user object upon successful addition
        @return 0: returns 0 upon unsuccessful addition
        """

        if(username not in self._user_dict.keys()):
            f = open("username_database.txt", 'a')
            temp = self.user_count
            self._user_dict[username] = (password, temp)
            f.write(f"{self.encrypt(username)},{self.encrypt(password)},\n")
            f.close()
            #if user is a student
            if(user_type == "1"):
                user_obj = Student(name, username, password)
            #if user is a teacher
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
        """
        Deletes the user, removing its object from the objects list; its username, password, 
        and id from the dictionary; the username and password from the data file; and the object from 
        the objects data file
        @param username: the username of the object
        """
        if(username not in self._user_dict.keys()):
            print("user does not exist")
        else:
            user_nmbr = self._user_dict[username][1]

            with open("username_database.txt", "r") as f:
                lines = f.readlines()
            f.close()
            with open("username_database.txt", "w") as f:
                for line in lines:
                    #if username password combination does not equal that of the deleted username password combination
                    if line.strip("\n") != f"{self.encrypt(username)},{self.encrypt(self._user_dict[username][0])},":
                        f.write(line)
            f.close()

            del self._user_dict[username]
            self.user_objs.pop(user_nmbr)
            self.user_count -= 1

            print("user succesfully removed")
          
    def log_out(self):
        """
        Updates the database files with the changes from the session
        """
        with open("user_database.txt", 'wb') as outp:
            for user in self.user_objs:
                #uses pickle to dump objects into the data file
                pickle.dump(user, outp)
        self._user_dict.clear()
        self.user_objs.clear()
        self.user_count = 0

        outp.close()

    def get_students(self):
        """
        Returns a list of all students
        @return temp: a list of student objects
        """
        temp = []
        for user in self.user_objs:
            if(type(user) == Student):
                temp.append(user)
        return temp
    
    def get_teachers(self):
        """
        Returns a list of all teachers
        @return temp: a list of teachers
        """
        temp = []
        for user in self.user_objs:
            if(type(user) == Teacher):
                temp.append(user)
        return temp

    def get_user(self, user_name):
        """
        Returns the user object associated with the username
        @param user_name: the username of the user
        @return user: the user object
        """
        for user in self.user_objs:
            if(user_name == user.get_username()):
                return user
                 
    def load(self):
        """
        Loads the username, password, id dictionary and the user object list from the database files
        """
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
        """
        Overloads the __str__ method
        @return f"number of users: {self.user_count}\nusername log: {self._user_dict} user_objs:{self.user_objs}":
        the string representation of the Backend class
        """
        return f"number of users: {self.user_count}\nusername log: {self._user_dict} user_objs:{self.user_objs}"