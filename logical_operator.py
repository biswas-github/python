# logical operators 
# and or not
atm_userid=30
atm_user_pin=12345
userid=int(input("Enter the user id"))
user_password=int(input("Enter the password"))
if userid== atm_userid and atm_user_pin==user_password:
    print("the login is sucessful !")
elif atm_userid==userid:
    print("id is correct but not the password")
else:
    print("login unsucessful")
    