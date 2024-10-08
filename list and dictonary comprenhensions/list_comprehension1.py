# first we will do the list comprehension 
address=["po0khara","putalisadak","ktm","chitwan"]
start_with_P=[data for data in address if data.upper().startswith("P")]
print(f"starting with p : {start_with_P}")