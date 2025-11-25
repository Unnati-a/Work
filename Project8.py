import numpy as np

class DataAnalysis:
    
    def oneD(self):
        """
        - Asks for comma seperated value.
        - converts to int and list than creates array
        """
        data=input("Enter elements to create array (seperated with comma): ")
        aa=list(map(int,data.split(",")))
        self.one_D_array=np.array(aa)
        print("\nArray created successfully:")
        print(self.one_D_array)
    
    def twoD(self):
        """
        - ask for rows and columns, multiply and ask elements
        - Asks for comma seperated value.
        - converts to int and list than creates array
        """
        self.row=int(input("Enter number of rows: "))
        self.columns=int(input("Enter number of columns: "))
        data=input(f"Enter {self.row*self.columns} elements for the array seperated by comma: ")
        aa=list(map(int,data.split(",")))
        self.two_D_array=np.array(aa).reshape((self.row,self.columns))
        print("\nArray created successfully:")
        print(self.two_D_array)
    
    def threeD(self):
        """
        - ask for rows and columns, multiply and ask elements
        - multiply by 2 as it is 3 D matrix
        - Asks for comma seperated value.
        - converts to int and list than creates array
        """
        r=int(input("Enter number of rows: "))
        c=int(input("Enter number of columns: "))
        data=input(f"Enter {r*c*2} elements for the 3D array seperated by comma: ")
        aa=list(map(int,data.split(",")))
        print("\nArray created successfully:")
        self.three_D_array=np.array(aa).reshape((2,r,c))
        print(self.three_D_array)

    def indexone(self):
        """
        - ask index number and prints that value from array
        """
        i=int(input("Enter index number to show value (2): "))
        print("\nIndexed Array is =",self.one_D_array[i])

    def sliceone(self):
        """
        ask for slice range convert to int and extracts with 2 variable
        """
        s=input("Enter range for slicing (start:end): ")
        start,end=map(int,s.split(":"))
        print("\nSliced Array:")
        print(self.one_D_array[start:end])
    
    def indextwo(self):
        """ 
        - ask index number(2 D = row and column) and prints that value from array
        """
        i=int(input("Enter Row number: "))
        ii=int(input("Enter Column number: "))
        print("\nIndexed Array is =",self.two_D_array[i,ii])
    
    def slicetwo(self):
        """
        ask for slice range (2 D = row and column) convert to int and extracts with 2 variable
        """
        r=input("Enter row range for slicing (start:end): ")
        c=input("Enter column range for slicing (start:end): ")
        st,en=map(int,r.split(":"))
        start,end=map(int,c.split(":"))
        print("\nSliced Array:")
        print(self.two_D_array[st:en,start:end])

    def math(self):
        """
        ask for same 2 D matrix for maths operations as created earlier
        """
        second=input(f"Enter same size array elements ({self.row*self.columns} elements seperated by comma): ")
        aa=list(map(int,second.split(",")))
        self.second_array=np.array(aa).reshape((self.row,self.columns))
        print("Second Array Created Successfully !")
        # print(second_array)

    def mathadd(self):
        """
        Adds original and 2nd matrix entered by user
        """
        print("Original Array:")
        print(self.two_D_array)
        print("Second Array:")
        print(self.second_array)
        print("Result of Addition:")
        self.add=self.two_D_array+self.second_array
        print(self.add)
    
    def mathsub(self):
        """
        Substracts original and 2nd matrix entered by user
        """
        print("Original Array:")
        print(self.two_D_array)
        print("Second Array:")
        print(self.second_array)
        print("Result of Substraction:")
        self.sub=self.two_D_array-self.second_array
        print(self.sub)
    
    def mathmul(self):
        """
        Multiply original and 2nd matrix entered by user
        """
        print("Original Array:")
        print(self.two_D_array)
        print("Second Array:")
        print(self.second_array)
        print("Result of Multiplication:")
        self.mul=self.two_D_array*self.second_array
        print(self.mul)
    
    def mathdiv(self):
        """
        Division original and 2nd matrix entered by user
        """
        print("Original Array:")
        print(self.two_D_array)
        print("Second Array:")
        print(self.second_array)
        print("Result of Division:")
        self.div=self.two_D_array/self.second_array
        print(self.div)

    def statssum(self):
        """
        Sums all elements of matrix
        """
        print("Original Array:")
        print(self.two_D_array)
        sum=self.two_D_array.sum()
        print(f"The sum of all elements is = {sum}")
    
    def statsmean(self):
        """
        finds mean(average) of all elements of matrix
        """
        print("Original Array:")
        print(self.two_D_array)
        means=self.two_D_array.mean()
        print(f"The mean of array is = {means}")
    
    def statsmed(self):
        """
        finds median (center point) of all elements of matrix
        """
        print("Original Array:")
        print(self.two_D_array)
        med=np.median(self.two_D_array)
        print(f"The median of array is = {med}")
    
    def statssd(self):
        """
        finds standard devation of all elements of matrix
        """
        print("Original Array:")
        print(self.two_D_array)
        sd=self.two_D_array.std()
        print(f"The Standard Deviation of array is = {sd}")
    
    def statvar(self):
        """
        finds variance(square of SD) of all elements of matrix
        """
        print("Original Array:")
        print(self.two_D_array)
        vr=self.two_D_array.var()
        print(f"The Variance of array is = {vr}")

    def statsmin(self):
        """
        finds minimum value from all elements of matrix
        """
        print("Original Array:")
        print(self.two_D_array)
        min=np.min(self.two_D_array)
        print(f"The minimum value in array is = {min}")
    
    def statsmax(self):
        """
        finds maximum value from all elements of matrix
        """
        print("Original Array:")
        print(self.two_D_array)
        max=np.max(self.two_D_array)
        print(f"The maximum value in array is = {max}")

    
    def search(self):
        """
        ask user which element want to search and gives its (position) index from matrix """
        print("This is Original Array:")
        print(self.two_D_array)
        sr=int(input("Enter Value to search: "))
        row,column=np.where(self.two_D_array==sr)
        print(f"The Searche value lies at row {row} and column {column}")
    
    def sort(self):
        """
        sorts the array in ascending order (row wise sorted)
        """
        print("This is Original Array:")
        print(self.two_D_array)
        print("This is Sorted Array:")
        srr=np.sort(self.two_D_array)
        print(srr)
        print("(Sorting Applied Row=Wise.)")
    
    def decend_sort(self):
        """
        sorts the array in descending order (row wise sorted)
        """
        print("This is Original Array:")
        print(self.two_D_array)
        print("This is Sorted Array ( Descending ):")
        des=np.sort(self.two_D_array)[:,::-1]
        print(des)
        print("(Sorting Applied Row=Wise.)")

    def filter(self):
        """
        - filter the array in with conditions entered by user
        - eval converts string into code (expression)
        """
        print("This is Original Array:")
        print(self.two_D_array)
        aa=input("Enter condition to filter (>5,<4): ")
        filtered=self.two_D_array[eval("self.two_D_array"+aa)]
        print(filtered)
    
    def combine(self):
        """
        ask for same 2 D matrix for maths operations as created earlier
        """
        data=input(f"Enter the elements of another array to combine ({self.row*self.columns} elements seperated by comma): ")
        aa=list(map(int,data.split(",")))
        self.second=np.array(aa).reshape((self.row,self.columns))
    
    def v_combine(self):
        """
        joins vertically (not add) original and second matrix
        """
        print("Original Array:")
        print(self.two_D_array)
        print("Second Array:")
        print(self.second)
        print("Combined Array (Vertical Stack):")
        print(print(np.vstack((self.two_D_array,self.second))))

    def h_combine(self):
        """
        joins horizontally (not add) original and second matrix
        """
        print("Original Array:")
        print(self.two_D_array)
        print("Second Array:")
        print(self.second)
        print("Combined Array (Horizontal Stack):")
        print(print(np.hstack((self.two_D_array,self.second))))
    
    def split(self):
        """
        - ask users for vertical or horizontal choice and split parts
        - splits as per choice entered
        """
        print("Original Array:")
        print(self.two_D_array)
        ax=int(input("Enter 1 for (Vertical) and 0 for (horizontal): "))
        sp=int(input("Enter how many parts (1,2 etc.): "))
        print(np.split(self.two_D_array,sp,axis=ax))


while 1<2:
    print("""
Welcome to Numpy Analyzer!
================================
Choose an option:
1. Create a Numpy Array
2. Perform Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort, or Filter Arrays
5. Compute Aggregates and Statistics
6. Exit
""")
    mchoice=int(input("Enter your choice: "))
    print()
    if mchoice==6:
        print("Thank you for using the Numpy Analyzer! Goodbye!")
        break
    elif mchoice==1:
        while 1<2:
            print("""\n
Select the type of array  to create:
1. 1D Array
2. 2D Array
3. 3D Array
4. Main Menu
""")
            schoice=int(input("Enter your choice: "))
            if schoice==1:
                obj1=DataAnalysis()
                obj1.oneD()
                while 1<2:
                    print("Choose an operation:")
                    print("1. Indexing")
                    print("2. Slicing")
                    print("3. Go Back")
                    subc=int(input("Enter your choice: "))
                    if subc==1:
                        obj1.indexone()
                    elif subc==2:
                        obj1.sliceone()
                    elif subc==3:
                        break
                    else:
                        print("Select Valid Choice!")
            elif schoice==2:
                obj1=DataAnalysis()
                obj1.twoD()
                while 1<2:
                    print("\nChoose an operation:")
                    print("1. Indexing")
                    print("2. Slicing")
                    print("3. Go Back")
                    subc=int(input("Enter your choice: "))
                    if subc==1:
                        obj1.indextwo()
                    elif subc==2:
                        obj1.slicetwo()
                    elif subc==3:
                        break
                    else:
                        print("Select Valid Choice!")
            elif schoice==3:
                obj1=DataAnalysis()
                obj1.threeD()
            elif schoice==4:
                break
            else:
                print("Select Valid Choice!")
    elif mchoice==2:
        while 1<2:
            print("""
\nChoose a mathematical operation:
1. Addition
2. Substraction
3. Multiplication
4. Division
5. Go Back
""")
            subchoice=int(input("Enter your choice: "))
            if subchoice==5:
                break
            elif subchoice==1:
                obj1.math()
                obj1.mathadd()
            elif subchoice==2:
                obj1.math()
                obj1.mathsub()
            elif subchoice==3:
                obj1.math()
                obj1.mathmul()
            elif subchoice==4:
                obj1.math()
                obj1.mathdiv()
            else:
                print("Enter Valid Choice!")
    elif mchoice==3:
        while 1<2:
            print("""
\nChoose an Option:
1. Horizontal Combine Arrays
2. Vertical Combine Arrays
3. Split Arrays
4. Main Menu
""")
            subchoice=int(input("Enter your choice: "))
            if subchoice==4:
                break
            elif subchoice==1:
                obj1.combine()
                obj1.h_combine()
            elif subchoice==2:
                obj1.combine()
                obj1.v_combine()
            elif subchoice==3:
                obj1.split()
            else:
                print("Enter Valid Choice!")
    elif mchoice==4:
        while 1<2:
            print("""
\nChoose an Option:
1. Search the value
2. Sort Acsending array
3. Sort Descending array
4. Filter Values
5. Main Menu
""")
            subchoice=int(input("Enter your choice: "))
            if subchoice==5:
                break
            elif subchoice==1:
                obj1.search()
            elif subchoice==2:
                obj1.sort()
            elif subchoice==3:
                obj1.decend_sort()
            elif subchoice==4:
                obj1.filter()
            else:
                print("Enter Valid Choice!")
    elif mchoice==5:
        while 1<2:
            print("""
\nChoose Statistical Operation:
1. Sum
2. Mean
3. Median
4. Standard Deviation
5. Variance
6. Minimum Value
7. Maximum Value
8. Main Menu
""")
            subchoice=int(input("Enter your choice: "))
            if subchoice==8:
                break
            elif subchoice==1:
                obj1.statssum()
            elif subchoice==2:
                obj1.statsmean()
            elif subchoice==3:
                obj1.statsmed()
            elif subchoice==4:
                obj1.statssd()
            elif subchoice==5:
                obj1.statvar()
            elif subchoice==6:
                obj1.statsmin()
            elif subchoice==7:
                obj1.statsmax()
            else:
                print("Select Valid Option!")
    else:
        print("Enter Valid Choice!")
                
        


