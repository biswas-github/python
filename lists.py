# //lists are ordered changeable allow duplicacy list[]
list=['biswas','bast','sreejana']
print(type(list))
#  here the data is printed as the list inside the braces 
print(list) 

# here data is printed separately
for data in list:
    print(data)
# data is changeable
list[0]= "changed"
print('after changing /n')
print(list)