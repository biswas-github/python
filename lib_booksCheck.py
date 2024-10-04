#program for finding if the books is in the library or not
books=["tumbaad","english","maths","nepali","science","social","descrete"]
search=str(input("enter a book that you are searching for "))
if search in books:
    print("book found")
else:
    print("not found any books")
    