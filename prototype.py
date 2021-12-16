from os import removedirs, truncate
from Assignment import Assignment
from old_gui import *
from Person import *
from Semester import *
import re
from time import sleep


"""
Prototype runner which is a terminal based application in which users 
can add and view classes and basic assignments
"""


def main():
    gui = GUI()
    gui.load()
    print("Hello, welcome to Planner App. ")
    valid = False
    while(not valid):
        print("Would you like to \n(0)Exit \n(1)Sign in \n(2)Sign up")
        selection = input("Enter Selection: ")
        if(selection == "0"):
            quit()
        elif(selection == "1"):
            #sign 
            valid_user = False
            while(not valid_user):
                username = input("Please enter username: ")
                password = input("Please enter passowrd: ")
                user = gui.validate_user(username, password)
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
                valid_username = False
                while(not valid_username):
                    username = input("Please input username: ")
                    if(gui.validate_user(username, "") == -1):
                        password = input("Please input password: ")
                        name = input("please input your name: ")
                        user = gui.add_user(username, password, name)
                        valid_username, valid_input, valid = True , True, True
                    else:
                        print("username already exists, please choose another")

        #hidden selection for admin to delete users
        elif(selection == "admin123"):
            rmuser_sel = input("remove user(y/n)? ").lower()
            if(rmuser_sel == "y"):
                removing = True
                while(removing):       
                    rmvuser = input("input user to be deleted: ")
                    gui.delete_user(rmvuser)
                    gui.log_out()
                    gui.load()
                    rmmore_sel = input("would you like to remove another(y/n)? ").lower()
                    if(rmmore_sel != "y"):
                        removing = False
                        print("bye felicia")           
            else:
                print("bye felicia")
        
        #hidden selection to see all users
        elif(selection == "letstakealook"):
            print("\nUsers:")
            for user in gui.user_objs:
                print(user.get_name())
            print("")


        else:
            print("Selection was not valid, please try again")

    print(f"\nWelcome, {user.get_name()}")
    doin_stuff = True
    while(doin_stuff):
        print("Choose one of the following options: \n(-1) Delete account \n(0) Log out \n(1) Add class \n(2) Show classes \n(3) Remove Class \n(4) Add Assignment \n(5) Show Assignments \n(6) Remove Assignment")
        selection = input("Enter Selection: ")
        if(selection == "0"):
            break
        elif(selection == "-1"):
            if(input("Are you sure you would like to delete your account (y/n)? ").lower() == "y"):
                gui.delete_user(user.get_username())
                break
            else:
                print("good choice :)")

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
            user.add_class(Class(class_name, start_date, end_date))

        elif(selection == "2"):
            print("\n*** Classes ***")
            user.show_classes()
            print("")
            input("Press enter to continue")

        elif(selection == "3"):
            valid_name = False
            while(not valid_name):
                class_name = input("Enter name of class in the correct format (ex. COMP 305): ").upper()
                if(re.search("[A-Z]{4} [0-9]{3}", class_name)):
                   valid_name = True 
                else:
                    print("Incorrect format, please try again")
            if(user.get_class(class_name) != -1):
                user.remove_class(user.get_class(class_name))
                input(f"Class: {class_name} was deleted, press enter to continue")
            else:
                input("That class does not exist, press enter to continue")

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
                    user.add_assignment(user.get_class(class_name), Assignment(assignment_name, start_date, end_date))
                    print("it gets here")
                elif(assignment_name == "0"):
                    break
                else:
                    print("Assignment already exists")

        elif(selection == "5"):
            print("\n*** Assignments ***\n")
            user.show_assignments()
            print("")
            input("Press enter to continue")

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
                    user.remove_assignment(user.get_class(class_name), user.get_assignment(class_name, assignment_name))
                    print(f"Assignment: {assignment_name} from Class: {class_name} was succesfully deleted")
                elif(assignment_name == "0"):
                    break
                else:
                    print("Assignment does not exist")



    gui.log_out()


main()
"""def fixdis():
    gui = GUI()
    gui.add_user("dalt", "123", "Dalton")
    gui.log_out()

fixdis()"""

