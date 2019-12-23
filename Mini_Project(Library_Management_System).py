class Library:
    def __init__(self, bookslist, name):
        self.bookslist = bookslist
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.bookslist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender's details has been updated. You can take the book.")

        else:
            print(f"Book is already being used by {self.lendDict[book]}")
            

    def addBook(self, book):
        self.bookslist.append(book)
        print("Book details has been added succesfully.")

    def returnBook(self, book):
        print(self.bookslist)
        self.lendDict.pop(book)


if __name__ == '__main__':
    library = Library(['Python','Rich dad poor dad','C++','Java'], 'Public Library')

    while(True):
        print(f"Welcome to the {library.name} library. Enter Your choice to continue")
        print("1. Display Books")
        print("2. Lend a Books")
        print("3. Add a Books")
        print("4. Return a Books")

        user_choice = int(input())
        if user_choice == 1:
            library.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("enter your name: ")
            library.lendBook(user,book)
            
        elif user_choice == 3:
            book = input("Enter the name of the book you want to Add.")
            library.addBook(book)
            
        elif user_choice == 4:
            book = input("Enter the name of the book you want to Return.")                
            library.returnBook(book)
            print("You have successfully returned your book.")
            
        else:
            print("Not a valid option")

        print("Press q to quit and c to continue.")
        user_choice2 = ''
        while(user_choice2 != "c" and user_choice2 != "q"):
            
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            if user_choice2 == "c":
                continue 
            
