# ch15_start_with_A.py
name=["ayus","amir","khan"]
A_start=[]
for data in name:
    data=data.upper()
    if data.startswith("A"):
        A_start.append(data)
print(f"starting with a are :{A_start}")

# program for b
items=["ps5","phone","programn","pp","hehe"]
startswith_p=[]
for data in items:
    data=data.upper()
    if data.startswith("P"):
        startswith_p.append(data)
print(f"starting with P are :{startswith_p}")


