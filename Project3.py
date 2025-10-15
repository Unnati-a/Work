# NEW UPDATED PROJECT 3 = DEL, TUPLE, SET USED !!

print("Welcome to the Student Data Organizer!")
slist=[]
while 1<2:
    print("""
Select an option:
1. Add Student
2. Display All Student
3. Update Student Inofrmation
4. Delete Student
5. Display Subjects Offered
6. Exit
""")
    a=int(input("Enter your Choice: "))
    if a==6:
        print("Thank you for using the program, You Exited!")
        break
    elif a==1:
        b=input("Enter ID: ")
        bb=b.split(",")
        c=input("Enter Name: ")
        d=int(input("Enter Age: "))
        e=input("Enter Grade: ")
        f=input("Enter DOB (YYYY-MM-DD): ")
        ff=f.split("-")
        g=input("Enter Subjects (comma-seperated): ")
        gg=g.split(",")
        dt={
            "ID": tuple(bb),
            "Name": c,
            "Age": d,
            "Grade": e,
            "DOB": tuple(ff),
            "Subjects": set(gg)
        }
        slist.append(dt)
        print("ID ADDED !")
    elif a==2:
        for s in slist:
            print(f"Name: {s["Name"]}, Age: {s["Age"]}, Grade: {s["Grade"]}, DOB: {s["DOB"]}, Subjects: {s["Subjects"]}, ID= {s["ID"]}")
            if slist==[]:
                print("List is Empty !")
    elif a==3:
        id=input("Enter ID to Update: ")
        id2=id.split(",")
        for s in slist:
            if s["ID"]==tuple(id2):
                s["Name"]=input("Enter Updated Name: ")
                s["Age"]=input("Enter Updated Age: ")
                s["Grade"]=input("Enter Updated Grade: ")
                s["Subjects"]=input("Enter Updated Subjects: ")
                s["DOB"]=input("Enter Updated DOB: ")
                print("Updated Successfully !")
    elif a==4:
        id=input("Enter ID to Delete: ")
        id2=id.split(",")
        for s in slist:
            if s["ID"]==tuple(id2):
                index=slist.index(s)
                del slist[index]
                print("ID Deleted !")
    elif a==5:
        id=input("Enter ID to List Subjects Selected: ")
        id2=id.split(",")
        for s in slist:
            if s["ID"]==tuple(id2):
                print(f"The subjects selected by {s["ID"]} are = {s["Subjects"]}")
    else:
        print("Invalid")

"""
slist[-1]["DOB"][0]="1999"
print("not mutable")        should rase error

"""

# OLD PROJECT 3

# print("Welcome to the Student Data Organizer!")
# slist=[]
# while 1<2:
#     print("""
# Select an option:
# 1. Add Student
# 2. Display All Student
# 3. Update Student Inofrmation
# 4. Delete Student
# 5. Display Subjects Offered
# 6. Exit
# """)
#     a=int(input("Enter your Choice: "))
#     if a==6:
#         print("Thank you for using the program, You Exited!")
#         break
#     elif a==1:
#         dt={
#             "ID": int(input("Enter Student ID: ")),
#             "Name": input("Enter Name: "),
#             "Age": int(input("Enter Age: ")),
#             "Grade": input("Enter Grade: "),
#             "DOB": input("Enter Date of Birth(YYYY-MM-DD): "),
#             "Subjects": input("Enter Subjects (comma seperated): ")
#         }
#         slist.append(dt)
#         print("Added Succesfully")
#     elif a==2:
#         for s in slist:
#             print(f"Student ID:{s["ID"]} | Name: {s["Name"]} | Age: {s["Age"]} | Grade: {s["Grade"]} | Subjects: {s["Subjects"]}")
#     elif a==3:
#         id=int(input("Enter ID to Update: "))
#         for s in slist:
#             if s["ID"]==id:
#                 s["Name"]= input("Enter Updated Name: ")
#                 s["Age"]= int(input("Enter Updated Age: "))
#                 s["Grade"]= input("Enter Updated Grade: ")
#                 s["DOB"]= input("Enter Updated Date of Birth: ")
#                 s["Subjects"]= input("Enter Updated Subjects: ")
#         print("Student Added Successfully!")
#     elif a==4:
#         id=int(input("Enter ID to Delete: "))
#         for s in slist:
#             if s["ID"]==id:
#                 slist.remove(s)
#         print("Student Deleted!")
#     elif a==5:
#         id=int(input("Enter ID to see Subjects: "))
#         for s in slist:
#             if s["ID"]==id:
#                 print(f"The subjects are= {s["Subjects"]}")
#     else:
#         print("Invalid")