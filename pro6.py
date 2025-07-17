class library:
    def __init__(self):
        self.books=[]
        self.nobooks=0
    def addbooks(self,book):
        self.books.append(book)
        self.nobooks+=1
    def get_no_of_book(self):
        return self.nobooks
    def show_details(self):
        print(f"The library has {self.nobooks} books in library. The books are ")
        for book in  self.books:
            print (book)

l1=library()
l1.addbooks("harry poter")
print(l1.get_no_of_book())
l1.show_details()