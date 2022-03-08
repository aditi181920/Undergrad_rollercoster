




class student:
    def __init__(self):
        self.std_details=[]
        self.roll={}

    def admit(self,name,clss,date):
        newlist=[]
        newlist.append(name)
        newlist.append(clss)
        newlist.append(date)
        if clss not in self.roll:
            newlist.append(1)
            self.roll[clss]=1
        else:
            newroll=self.roll[clss]
            newroll+=1
            self.roll[clss]+=1
            newlist.append(newroll)
        self.std_details.append(newlist)

    def search(self,name,clss,roll):
        for i in self.std_details:
            if i[0]==name and i[1]==clss and i[3]==roll:
                print("Yes. This student exists and the date of admission is:",i[2])
                break
        else:
            print("Sorry. This student does not exist")

    def terminate(self,name,clss,roll):
        for i in self.std_details:
            if i[0]==name and i[1]==clss and i[3]==roll:
                self.std_details.remove(i)
                self.roll[i[1]]-=1
                for j in self.std_details:
                    if j[1]==clss and j[3]>i[3]:
                        j[3]-=1
                break
        else:
            print("The student you want to remove does not exist")


    def update(self,name,clss,roll,new_name,new_clss,new_date):
        for i in self.std_details:
            if i[0]==name and i[1]==clss and i[3]==roll:
                i[0]=new_name
                i[1]=new_clss
                i[2]=new_date
                self.roll[clss]-=1
                if new_clss in self.roll:
                    self.roll[new_clss]+=1
                    i[3]=self.roll[new_clss]
                else:
                    self.roll[new_clss]=1
                    i[3]=1


def main():
    std=student()
    while True:
        print("**********MENU***********")
        print("1. New admission\n2. Search student\n3. Termination\n4. Update record\n5. View all records")
        c=int(input("What you want to do?"))
        if c==1:
            name=input("Enter name of the student:")
            clss=input("Enter class the student is to be admitted:")
            date=input("May i know today's date:")
            std.admit(name,clss,date)

        elif c==2:
            name=input("Enter name of the student you want to search:")
            clss=input("Enter class of that student:")
            roll=int(input("Enter roll number of that student:"))
            std.search(name,clss,roll)

        elif c==3:
            name=input("Enter name of the student you want to terminate:")
            clss=input("Enter class of that student:")
            roll=int(input("Enter roll number of that student:"))
            std.terminate(name,clss,roll)

        elif c==4:
            name=input("Enter name of the student whose record you want to update:")
            clss=input("Enter class of that student:")
            roll=int(input("Enter roll number of that student:"))
            new_name=input("Enter new name:")
            new_clss=input("Enter new class:")
            new_date=input("Enter new date of admission:")
            std.update(name,clss,roll,new_name,new_clss,new_date)

        elif c==5:
            print("List containing details of each student:")
            print(std.std_details)
            print("Details of class and its respective strength:")
            print(std.roll)
            
        else:
            print("Invalid input")

        s=input("Want to continue? Enter y if you want to:")
        if s!='y':
            break

        


if __name__=="__main__":
    main()
