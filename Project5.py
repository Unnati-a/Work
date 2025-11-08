class Employee:
    def __init__(self,id,name,age,salary):
        self.__id=id
        self.n=name
        self.a=age
        self.__s=salary

    def Setdata(self,id):
       self.__id=id

    def Setdat(self,salary):
        self.__s=salary 

    def Getdata(self):
        return self.__id

    def Getdat(self):
        return self.__s
        
    def Display(self):
        print(f"\nEmployee with Name = {self.n}, Age = {self.a}, ID = {self.__id}, Salary = {self.__s}")

    def __del__(self):
        pass

class Manager(Employee):
    def __init__(self, id, name, age, salary,dep):
        self.dep=dep
        super().__init__(id, name, age, salary)
        
    def Checkclass(self):
        self.scl=issubclass(Manager,Employee)

    def Display(self):
        print(f"\nManager with Name = {self.n}, Age = {self.a}, ID = {self.Getdata()}, Salary = {self.Getdat()}, Department = {self.dep}")
        print(f"Manager is sub-class of Employee = {self.scl}")

class Developer(Employee):
    def __init__(self, id, name, age, salary,lan):
        self.language=lan
        super().__init__(id, name, age, salary)

    def Checkclass(self):
        self.sclass=issubclass(Developer,Employee)

    def Display(self):
        print(f"\nDeveloper with Name = {self.n}, Age = {self.a},ID = {self.Getdata()}, Salary = {self.Getdat()}, Language = {self.language}")
        print(f"Developer is sub-class of Employee = {self.sclass}")

EmployeeL=[]
ManagerL=[]
DeveloperL=[]

while 1<2:
    print("""
--- Python OOP Project: Employee Management System ---

Choose an operation:
1. Create a Employee
2. Create an Manager
3. Create an Developer
4. Show Details
5. Exit
""")
    a=int(input("Enter your choice: "))

    if a==5:
        print("Exiting the system. All resources have been Freed")
        print("\nGoodbye!")
        break
    elif a==1:
        e=input("Enter name: ")
        ee=int(input("Enter age: "))
        eee=input("Enter ID: ")
        ae=int(input("Enter salary: "))

        eobj=Employee(eee,e,ee,ae)
        EmployeeL.append(eobj)
        eobj.Display()
    elif a==2:
        m=input("Enter name: ")
        mm=int(input("Enter age: "))
        mmm=input("Enter ID: ")
        me=int(input("Enter salary: "))
        mme=input("Enter Department: ")

        mobj=Manager(mmm,m,mm,me,mme)
        ManagerL.append(mobj)
        mobj.Checkclass()
        mobj.Display()
    elif a==3:
        d=input("Enter name: ")
        dd=int(input("Enter age: "))
        ddd=input("Enter ID: ")
        de=int(input("Enter salary: "))
        dde=input("Enter Language: ")

        dobj=Developer(ddd,d,dd,de,dde)
        DeveloperL.append(dobj)
        dobj.Checkclass()
        dobj.Display()
    elif a==4:
        print("1. Display Employee")
        print("2. Display Manager")
        print("3. Display Developer")
        aa=int(input("Enter your choice: "))
        if aa==1:
            for e in EmployeeL:
                eobj.Display()
        elif aa==2:
            for m in ManagerL:
                mobj.Display()
        elif aa==3:
            for d in DeveloperL:
                dobj.Display()
        else:
            print("Enter Valid Choice !")
    else:
        print("Enter Valid Choice")




