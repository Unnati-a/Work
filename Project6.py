class JournalManager:

    def __init__(self):
        self.file="journal.txt"

    def append(self):
        files=open(f"{self.file}","a")
        files.write(aap+"\n")
        files.close()

    def view(self):
        try:
            files=open(f"{self.file}","r")
            read=files.readlines()
            for r in read:
                print(r)
            files.close()
        except Exception:
            print("\nError:","The journal file does not exists, please add a new entry first")
    
    def search(self):

        try:
            files=open(f"{self.file}","r")
            read=files.readlines()
            found=False
            for r in read:
                if ss in r:
                    print(r)
                    found=True
            if not found:
                print("\nNo entries found with the keyword =",ss)
            files.close()

        except Exception:
            print("\nError:","The journal file does not exists, please add a new entry first")

    def dell(self):
        try:
            if aa.lower()=="yes":
                self.file=open("journal.txt","w")
                self.file.close()
                print("\nAll entries deleted")
            else:
                print("\nNot deleted")
        except Exception:
            print("\nNo journal entries to delete")

        
while 1<2:
    print("""
Personal Journal Manager!
Please select an option:

1. Add a new entry
2. View all entries
3. Search for an entry
4. Delete all entries
5. Exit
""")
    a=int(input("Enter your choice: "))
    if a==5:
        print("Thank you for using Personal Journal Manager. GoodBye!")
        break
    if a==1:
        obj=JournalManager()
        aap=input("Enter Journal entry to append: ")
        obj.append()
        print("\nJournal Entry Added Successfull !")
    elif a==2:
        obj=JournalManager()
        print("Your journal entries are ")
        print("------------------------------")
        obj.view()
    elif a==3:
        obj=JournalManager()
        ss=input("Enter keyword to search: ")
        obj.search()
    elif a==4:
        aa=input("Are you sure you want to delete all enteries (yes/no): ")
        obj=JournalManager()
        obj.dell()