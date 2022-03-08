
class library:
    
    def __init__(self):
        self.books={'Concrete Mathematics':'1601B','Discrete Mathematics':'1705A',
                    'Introduction to Psycology':'1222A','Introduction to Python':'2190C',
                    'Basics of C++':'1333B','Ethical Hacking':'4290A'}
        self.qty={'1601B':50,'1705A':50,'1222A':50,'2190C':50,'1222A':50,'2190C':50,
                  '1333B':2,'4290A':50}
        self.lend={'1601B':0,'1705A':0,'1222A':0,'2190C':0,'1222A':0,'2190C':0,
                  '1333B':0,'4290A':0}
        self.lendusr={'1601B':[],'1705A':[],'1222A':[],'2190C':[],'1222A':[],'2190C':[],
                  '1333B':[],'4290A':[]}

    def search(self,name):
        if name in self.books:
            print("This book exists in library with ISBN number:",self.books[name])
        else:
            print("This book does not exist in this library")

    def disp_books(self):
        for i in self.books:
            print('Book name:{:35s},ISBN number:{:10s}'.format(i,self.books[i]))

    def lend_book(self,name,user_name):
        if name not in self.books:
            print("This book does not exist in library!!")
        elif self.qty[self.books[name]]==self.lend[self.books[name]]:
            print("Not available right  now!! Please come back later!!")
        else :
            self.lend[self.books[name]]+=1
            self.lendusr[self.books[name]].append(user_name)

    def ret_book(self,name,user_name):
        self.lend[self.books[name]]-=1
        self.lendusr[self.books[name]].remove(user_name)

    def addbooks(self,book_name,isbn_no,qtty):
        self.books[book_name]=isbn_no
        self.qty[isbn_no]=qtty
        self.lend[isbn_no]=0
        self.lendusr[isbn_no]=[]

    def removebooks(self,book_name):
        del self.qty[self.books[book_name]]
        del self.lend[self.books[book_name]]
        del self.lendusr[self.books[book_name]]
        del self.books[book_name]
            
    def updatebook(self,book_name,qtty):
        self.qty[self.books[book_name]]=qtty

    def user_menu(self):
        print("**********USER MENU***********")
        print("Enter the number from below options:")
        print("1. Search book")
        print("2. Display books")
        print("3. Lend book")
        print("4. Return book")

    def admin_menu(self):
        print("***********ADMIN MENU**************")
        print("Enter the number from below options:")
        print("1. Add book")
        print("2. Remove book")
        print("3. Update book")
        print("4. Display lended books")
        print("5. Display all the dictionaries present in the library management system")

    def disp_lendedbooks(self):
        for i in self.lend:
            if self.lend[i]!=0:
                print('Book isbn:{:10s},Number of people who have lended:{:<10d},\nList of people who have lended:{}'.format(i,self.lend[i],self.lendusr[i]))


def main():
    object=library()
    while 1:
        identity=eval(input("Who are you?\nEnter 1 if you are a user\nEnter 2 if you are an Admin:\n"))
        if identity==1:
            print("Welcome user")
            while 1:
                object.user_menu()
                choice=eval(input("Your choice?"))
                
                if choice==1:
                    inp=input("Enter the book name you want to search: ")
                    object.search(inp)
                    
                elif choice==2:
                    object.disp_books()
                    
                elif choice==3:
                    inp=input("Enter the book you want to lend:")
                    name=input("Enter your name:")
                    object.lend_book(inp,name)
                    
                elif choice==4:
                    inp=input("Enter the book you want to return:")
                    name=input("Enter your name")
                    object.ret_book(inp,name)
                    
                else:
                    print("Invalid choice")

                ex=input("Do you want to exit? Enter 'yes' if you want to:")
                if ex=='yes':
                    break
                
        elif identity==2:
            password=input("Enter password to log in as Admin: ")
            if password=="libAdmin@thislibrary":
                print("Welcome admin")
                while 1:
                    object.admin_menu()
                    choice=eval(input("Your choice?"))
                    
                    if choice==1:
                        book_name=input("Enter the book name:")
                        isbn_no=input("Enter the isbn number:")
                        qtty=input("Enter the quantity of this book:")
                        object.addbooks(book_name,isbn_no,qtty)
                        
                    if choice==2:
                        book_name=input("Enter the book you want to remove:")
                        object.removebooks(book_name)
                        
                    if choice == 3:
                        book_name=input("Enter the book you want to update:")
                        qtty=input("Enter the new quantity of this book:")
                        object.updatebook(book_name,qtty)

                    if choice==4:
                        object.disp_lendedbooks()

                    if choice==5:
                        print("List of books with isbn numbers available in the library")
                        print(object.books)
                        print("List of book isbn numbers with total quantity available in library")
                        print(object.qty)
                        print("List of book isbn numbers with number of books that have been lended from the library")
                        print(object.lend)
                        print("List of book isbn numbers with list of users who lended the books")
                        print(object.lendusr)

                    ex=input("Do you want to exit? Enter 'yes' if you want to:")
                    if ex=='yes':
                        break
                    
            else:
                print("Wrong password")
        else:
            print("Invalid input")
            
        ex_pr=input('Do you want to exit from library system:')
        if ex_pr=='yes':
            break



if __name__=="__main__":
    main()
