while 1<2:
    print("""
===========================
Welcome to Multi-Utility Toolkit
===========================
Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Date Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custome Module)
6. Explore Module Attributes (dir())
7. Exit
===========================
          """)
    mainchoice=int(input("Enter your choice: "))

    if mainchoice==7:
        print("""
===========================
Thank you for using the Multi-Utlity Toolkit!
===========================""")
        break

    elif mainchoice==1:
        while 1<2:
            print("""
Datetime and Time Operations:
1. Display current date and time
2. Calculate difference between two dates/times
3. Format date into custom format
4. Countdown Timer
5. Back to Main Menu
                  """)
            
            subchoice=int(input("Enter your choice:"))
            import datetime
            import time

            if subchoice==5:
                break
            elif subchoice==1:

                current=datetime.datetime.now()
                print("Current Date = ",current.date())
                print("Current Time = ",current.time())
                print("=============================")
            elif subchoice==2:

                f=input("Enter First Date (YYYY-MM-DD): ")
                s=input("Enter Second Date (YYYY-MM-DD): ")

                fy,fm,fd=map(int,f.split("-"))
                sy,sm,sd=map(int,s.split("-"))

                fdate=datetime.date(fy,fm,fd)
                sdate=datetime.date(sy,sm,sd)

                dif=sdate-fdate
                print("Difference:",dif)
                print("=============================")

            elif subchoice==3:
                aa=datetime.datetime.now()
                formateddate=aa.strftime("%Y--%m--%d")
                print(f"The Custome Date is: {formateddate}")
                print("=============================")

            elif subchoice==4:

                timer=int(input(("Enter your time for timer: ")))
                print(f"Your Timer is Set for {timer} Seconds")
                time.sleep(timer)
                print("\nTime UP, Time UP !!")
                print("=============================")
            else:
                print("====Enter Valid Choice====")

    elif mainchoice==2:
        while 1<2:
            print("""
Mathematical Operations:
1. Calculate Factorial
2. Solve Compound Interest
3. Back to Main Menu
                  """)
            subchoice=int(input("Enter your choice:"))
            import math
            if subchoice==3:
                break
            elif subchoice==1:
                fac=int(input("Enter number to calculate Factorial: "))
                factorial=math.factorial(fac)
                print(f"The factorial of number {fac} is {factorial}")
                print("=============================")
            elif subchoice==2:
                pamount=int(input("Enter Principal Amount: "))
                rrate=int(input("Enter Rate of Interest (in %): "))
                per=int(input("Enter Time (in years): "))
                r = rrate / 100
                amount=pamount*(1+r/1)**per
                print(f"The Final Amount at End of Year is = {amount}")
                print("=============================")
            else:
                print("====Enter Valid Choice====")
    
    elif mainchoice==3:
        while 1<2:
            print("""
Random Data Generation
1. Generate Random Number
2. Generate Random List
3. Generate Random OTP
4. Back to Main Menu
                  """)
            subchoice=int(input("Enter your choice: "))
            import random
            if subchoice==4:
                break

            elif subchoice==1:
                print(f"The random number generated is = {random.random()*10}")
                print("=============================")

            elif subchoice==2:
                l=[]
                for i in range(1,6):
                    aa=random.randint(1,100)
                    l.append(aa)
                print(f"The list of random numbers is: {l}")
                print("=============================")

            elif subchoice==3:
                aa=str(random.randint(10,100))
                ab=str(random.randint(10,100))
                print(f"The Random OTP is: {aa+ab}")
                print("=============================")

            else:
                print("====Enter Valid Choice====")

    elif mainchoice==4:
        import uuid

        print(f"\nGenerated UUID: {uuid.uuid4()}")
        print("=============================")

    elif mainchoice==5:
        import Project6 as p6

    elif mainchoice==6:
        import importlib
        explore=input("Enter module name to explore: ")
        print(f"Available attributes in {explore} are:")
        print(dir(importlib.import_module(explore)))
        print("=============================")
    else:
        print("====Enter Valid Choice====")