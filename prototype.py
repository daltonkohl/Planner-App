from os import removedirs, truncate
from Assignment import Assignment
from Backend import *
from Person import *
from Semester import *
import re
from time import sleep


"""
Prototype runner which is a terminal based application in which users 
can add and view classes and basic assignments
"""


def main():
    back = Backend()
    back.load()
    print("Hello, welcome to Planner App. ")
    valid = False
    while(not valid):
        print("Would you like to \n(0)Exit \n(1)Sign in \n(2)Sign up")
        selection = input("Enter Selection: ")
        if(selection == "0"):
            quit()
        elif(selection == "1"):
            #sign in
            valid_user = False
            while(not valid_user):
                username = input("Please enter username: ")
                password = input("Please enter passowrd: ")
                user = back.validate_user(username, password)
                if(user == -1):
                    print("Username not in database, please sign up")
                    break
                elif(user == 0):
                    print("Password does not match username")
                else:
                    valid_user , valid = True, True

        elif(selection == "2"):
            #sign up
            valid_input = False
            while(not valid_input):
                valid_type = False
                print("Please input user type 1 for student 2 for teacher")
                while(not valid_type):
                    user_type = input("Enter selection: ")
                    if(user_type == "1" or user_type == "2"):
                        valid_type = True
                    else:
                        print("Invalid input, please try again")                 
                valid_username = False
                while(not valid_username):
                    username = input("Please input username: ")
                    if(back.validate_user(username, "") == -1):
                        password = input("Please input password: ")
                        name = input("please input your name: ")
                        user = back.add_user(username, password, name, user_type)
                        valid_username, valid_input, valid = True , True, True
                    else:
                        print("username already exists, please choose another")

        #hidden selection for admin to delete users
        elif(selection == "admin123"):
            rmuser_sel = input("remove user(y/n)? ").lower()
            if(rmuser_sel == "y"):
                removing = True
                while(removing):       
                    rmvuser_name = input("input user to be deleted: ")
                    rmvuser = back.get_user(rmvuser_name)
                    if(type(rmvuser) == Student):
                        teachers = back.get_teachers()
                        for teacher in teachers:
                            teacher.remove_student_from_classes(rmvuser)
                    else:
                        students = back.get_students()
                        for student in students:
                            for existing_class in student.get_class_list():
                                if(existing_class.get_teacher().get_name() == rmvuser.get_name()):
                                    existing_class.remove_teacher()
                    back.delete_user(rmvuser_name)
                    back.log_out()
                    back.load()
                    rmmore_sel = input("would you like to remove another(y/n)? ").lower()
                    if(rmmore_sel != "y"):
                        removing = False
                        print("bye felicia")           
            else:
                print("bye felicia")
        
        #hidden selection to see all users
        elif(selection == "letstakealook"):
            print("\nUsers:")
            for user in back.user_objs:
                print(user.get_name())
            print("")

        elif(selection == "wipeit"):
            if(input("Are you sure you want to wipe? (y/n): ").lower() == "y"):
                f = open("user_database.txt", "w")
                f.close()
                f = open("username_database.txt", "w")
                f.close()
                print("its all gone")
            else:
                print("it lives to see another day")




        else:
            print("Selection was not valid, please try again")

    print(f"\nWelcome, {user.get_name()}")
    doin_stuff = True
    while(doin_stuff):
        if(type(user) == Student):
            print("Choose one of the following options: \n(-1) Delete account \n(0) Log out \n(1) Add class \n(2) Show classes \n(3) Remove Class \n(4) Add Assignment \n(5) Show Assignments \n(6) Remove Assignment \n(7) Complete Assignment")
        else:
            print("Choose one of the following options: \n(-1) Delete account \n(0) Log out \n(1) Add class \n(2) Show classes \n(3) Remove Class \n(4) Add Assignment \n(5) Show Assignments \n(6) Remove Assignment")
        selection = input("Enter Selection: ")

        #log out
        if(selection == "0"):
            break

        #delete account
        elif(selection == "-1"):
            if(input("Are you sure you would like to delete your account (y/n)? ").lower() == "y"):
                if(type(user) == Student):
                    teachers = back.get_teachers()
                    for teacher in teachers:
                        teacher.remove_student_from_classes(user)
                else:
                    students = back.get_students()
                    for student in students:
                        for existing_class in student.get_class_list():
                            if(existing_class.get_teacher().get_name() == user.get_name()):
                                existing_class.remove_teacher()
                back.delete_user(user.get_username())
                break
            else:
                print("good choice :)")

        #add class
        elif(selection == "1"):
            valid_name = False
            while(not valid_name):
                class_name = input("Enter name of class in the correct format (ex. COMP 305): ").upper()
                if(re.search("[A-Z]{4} [0-9]{3}", class_name)):
                   valid_name = True 
                else:
                    print("Incorrect format, please try again")
            valid_date = False
            while(not valid_date):
                start_date = input("Enter start date in the format mm/dd/yyyy: ")
                if(re.search("(0[1-9]|1[012])[- \/.](0[1-9]|[12][0-9]|3[01])[- \/.](19|20)\d\d", start_date)):
                    valid_date = True
                else:
                    print("date not valid, try again")
            valid_date = False
            while(not valid_date):
                end_date = input("Enter end date in the format mm/dd/yyyy: ")
                if(re.search("(0[1-9]|1[012])[- \/.](0[1-9]|[12][0-9]|3[01])[- \/.](19|20)\d\d", end_date)):
                    valid_date = True
                else:
                    print("date not valid, try again")
            if(type(user) == Student):
                teachers = back.get_teachers()
                user.add_class(Class(class_name, start_date, end_date), teachers)
            else:
                students = back.get_students()
                user.add_class(Class(class_name, start_date, end_date), students)

        elif(selection == "2"):
            print("\n*** Classes ***")
            user.show_classes()
            print("")
            input("Press enter to continue")

        #remove class
        elif(selection == "3"):
            valid_name = False
            while(not valid_name):
                class_name = input("Enter name of class in the correct format (ex. COMP 305): ").upper()
                if(re.search("[A-Z]{4} [0-9]{3}", class_name)):
                   valid_name = True 
                else:
                    print("Incorrect format, please try again")
            if(user.get_class(class_name) != -1):
                if(type(user) == Student):
                    user.remove_class(user.get_class(class_name))
                else:
                    students = back.get_students()
                    user.remove_class(user.get_class(class_name), students)
                input(f"Class: {class_name} was deleted, press enter to continue")
            else:
                input("That class does not exist, press enter to continue")

        #add assignment
        elif(selection == "4"):
            valid_name = False
            while(not valid_name):
                class_name = input("Enter name of class in the correct format (ex. COMP 305) or 0 to go back: ").upper()
                if(re.search("[A-Z]{4} [0-9]{3}", class_name)):
                    if(user.get_class(class_name) != -1):
                        valid_name = True 
                    else:
                        print("Class does not exist, please create the class first")
                elif(class_name == "0"):
                        break
                else:
                    print("Incorrect format, please try again")
            valid_name = False
            while(not valid_name):
                assignment_name = input("Enter name of assignment or 0 to go back: ")
                if(user.get_assignment(class_name, assignment_name) == -1):
                    if(assignment_name == "0"):
                        break
                    valid_name = True
                    valid_date = False
                    while(not valid_date):
                        start_date = input("Enter date issued in the format mm/dd/yyyy: ")
                        if(re.search("(0[1-9]|1[012])[- \/.](0[1-9]|[12][0-9]|3[01])[- \/.](19|20)\d\d", start_date)):
                            valid_date = True
                        else:
                            print("date not valid, try again")
                    valid_date = False
                    while(not valid_date):
                        end_date = input("Enter due date in the format mm/dd/yyyy: ")
                        if(re.search("(0[1-9]|1[012])[- \/.](0[1-9]|[12][0-9]|3[01])[- \/.](19|20)\d\d", end_date)):
                            valid_date = True
                        else:
                            print("date not valid, try again")
                    description = input("Enter a description of the assignment(press enter for no description): ")
                    if(type(user) == Student):
                        user.add_assignment(user.get_class(class_name), Assignment(assignment_name, start_date, end_date, "", description))
                    else:
                        students = back.get_students()
                        user.add_assignment(user.get_class(class_name), Assignment(assignment_name, start_date, end_date, "", description), students)
                else:
                    print("Assignment already exists")

        #Show assignments
        elif(selection == "5"):
            print("\n*** Assignments ***\n")
            user.show_assignments()
            print("")
            input("Press enter to continue")

        #Remove assignment
        elif(selection == "6"):
            valid_name = False
            while(not valid_name):
                class_name = input("Enter name of class in the correct format (ex. COMP 305) or 0 to go back: ").upper()
                if(re.search("[A-Z]{4} [0-9]{3}", class_name)):
                    if(user.get_class(class_name) != -1):
                        valid_name = True 
                    else:
                        print("Class does not exist, please create the class first")
                elif(class_name == "0"):
                        break
                else:
                    print("Incorrect format, please try again")
            valid_name = False
            while(not valid_name):
                assignment_name = input("Enter name of assignment or 0 to go back: ")
                if(user.get_assignment(class_name, assignment_name) != -1):
                    valid_name = True
                    if(type(user) == Student):
                        user.remove_assignment(user.get_class(class_name), user.get_assignment(class_name, assignment_name))
                    else:
                        students = back.get_students()
                        user.remove_assignment(user.get_class(class_name), user.get_assignment(class_name, assignment_name), students)
                    print(f"Assignment: {assignment_name} from Class: {class_name} was succesfully deleted")
                elif(assignment_name == "0"):
                    break
                else:
                    print("Assignment does not exist")

        #complete assginment implement later




    back.log_out()


main()
"""def fixdis():
    back = Backend()
    back.add_user("dalt", "123", "Dalton", "1")
    back.log_out()

fixdis()"""


