username=input("Enter username: ")
password=input("Enter password: ")

if(username=="admin" and password=="123"):
    print("Successfully logged in")
else:                               #nesting if else
    if(username!="admin"):
        print("Invalid username")
    else:
        print("Invalid password")
