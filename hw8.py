def register(book_name, book_author):
    global library
    library[book_name]=book_author
def search():
    name=input("Type a book name to search: ")
    if name=='x': return False
    print(library.get(name,"Searched book is not in the library."))
    return True
try:
    library={}
    for counter in range(5):
        print("Book ",counter+1,":",sep="")
        book_name=input("Enter a book name: ")
        book_author=input("Enter author: ")
        register(book_name, book_author)
    token=True
    while token:
        token=search()
except:
    print("An error has been occured.")
    raise
