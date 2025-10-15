print("Welcome to the Pattern Generator and Number Analyzer!")
print()
while 1<2:
    print()
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    a=int(input("Enter your Choice: "))
    print()
    if a==3:
        print("Exiciting the program. Goodbye!")
        break
    if a==1:
        b=int(input("Enter the number of rows for the pattern: "))
        print()
        print("Pattern:")
        for i in range(1,b+1):
            print("*"*i)
    if a==2:
        c=int(input("Enter the start of the range: "))
        d=int(input("Enter the end of the range: "))
        total=0
        for i in range(c,d+1):
            total+=i
            if i%2==0:
                print("Number",i,"is","Even")
            else:
                
                print("Number",i,"is","Odd")
        print("Sum of all numbers from",c,"to",d,"is:",total)
