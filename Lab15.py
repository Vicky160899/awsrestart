import os

def new_user():
    confirm = "N"
    while confirm!="Y":
         username = input("Enter the USERNAME to add")
         print("use the username'" + username + "'?(Y/N)")
         confirm = input().upper()
         if confirm == "Y":
             print("User Added")
         else:
             print("Failed")
             
    
    os.system("sudo adduser" + username)

new_user()    
    