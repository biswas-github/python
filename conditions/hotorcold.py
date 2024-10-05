temp=float(input("Enter the temprature"))
if temp<=0:
    print(f"it is freezing cold at {temp}")
elif temp>0 and temp<=15:
    print(f"it is cold at {temp}")
else:
    print(f"it is hot at {temp}")