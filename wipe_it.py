"""
Script wipes the user databases
"""
f = open("user_database.txt", "w")
f.close()
f = open("username_database.txt", "w")
f.close()
print("databases have been wiped")