# # SyntaxError
# # {key:value  for element/item in iterable conditions}
# first finding the value of square no up to 10
X=0
square={X:X**2 for X in range(1,11)}
print(square)
for key in square:
    print(f"the square of {key} is :{square[key]}")