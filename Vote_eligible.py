age=int(input("enter your age "))
if age<=0:
    print("Invalid inputs")
elif age>0 and age<18 :
    print(f"not eligible to vote for Now \n but you can vote after {18-age} years")
else:
    print("you are eligible to vote !!")