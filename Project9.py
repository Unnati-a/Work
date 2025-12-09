import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:

# A. INITIALIZATION

    def __init__(self):
        self.data = None

# 1. LOAD DATA

    def load_data(self):
        print("== Load Data Set ==")
        a = input("Enter the pathe of data set (CSV File): ")

        try:
            self.data = pd.read_csv(a)
            print("\nData Loaded Successfully!\n")
        except FileNotFoundError:
            print("\nFile not Found!\n")

# 2. EXPLORE DATA

    def explore_data(self):

        if self.data is None:
            print("Data-Set not loaded!")
    
        while 1<2:
            print("""
== Explore Data ==
1. Display the First 5 Rows
2. Display the Last 5 Rows
3. Display the Column Names
4. Display Datatypes
5. Display Basic Info.
6. Back to Main Menu
    """)
            schoice = int(input("Enter your choice: "))
            if schoice==6:
                break
            elif schoice==1:
                print(self.data.head(5))
            elif schoice == 2:
                print(self.data.tail(5))
            elif schoice == 3:
                print(self.data.columns)
            elif schoice == 4:
                print(self.data.dtypes)
            elif schoice == 5:
                print(self.data.info())
            else:
                print("----Enter Valid Choice----")

# 3. HANDLE DATAFRAME OPERATIONS

    def data_frame(self):
        if self.data is None:
            print("Data-Set not loaded!")
        while 1<2:
            print("""
== Data-Frame Operations ==
1. Sort by Column
2. Sort by Rows
3. Sum a Column
4. Split Column(Groupby)
5. Main Menu
    """)
            schoice = int(input("Enter your choice: "))

            if schoice == 5:
                break
            elif schoice == 1:
                print("Data sorted column-wise:\n")
                aa = self.data.sort_index(axis=1)
                print(aa.head(7))
            elif schoice == 2:
                print("Data sorted row-wise (index):\n")
                ab = self.data.sort_index()
                print(ab.head(7))
            elif schoice == 3:
                print("Available Columne are:", list(self.data.columns))
                print()

                col = input("Enter column name to sum: ")
                if col in self.data.select_dtypes(include="number").columns:
                    print("The sum is =>",self.data[col].sum())
                else:
                    print("---Column is Not Numeric!---")
            elif schoice == 4:
                print("Available Columne are:", list(self.data.columns))
                print()
                col = input("Enter column name to group by: ")
            
                if col not in self.data.columns:
                    print("Invalid column name!")
                    continue
                grouped = self.data.groupby(col).size()
                print(" Group by Result on Column:", col)
                print(grouped)
            else:
                print("----Enter Valid Choice----")


# 4. CLEAN / HANDLE MISSING DATA

    def clean_data(self):

        if self.data is None:
            print("Data-Set not loaded!")

        self.data.replace(["", " ", "NA", "None", "nan","NAn","NaN","NAN"], pd.NA, inplace=True)

        while 1<2:
            print("""
== Handle Missing Data ==
1. Display rows with missing values
2. Fill missing values with mean
3. Drop rows with missing values
4. Replace missing values with specific value
5. Main Menu
""")
            schoice = int(input("Enter your choice: "))

            if schoice == 5:
                break
            elif schoice == 1:
                missing = self.data[self.data.isnull().any(axis=1)]
                if missing.empty:
                    print("----No missing rows!----")
                else:
                    print(missing)
            elif schoice == 2:
                numeric_cols = self.data.select_dtypes(include=['number']).columns
                self.data[numeric_cols] = self.data[numeric_cols].fillna(self.data[numeric_cols].mean())
                if numeric_cols.empty:
                    print("----No Values to Fill----")
                else:
                    print("----Values filled with Mean!----")
            elif schoice == 3:
                if self.data.dropna(inplace=True):
                    print("----Rows with missing values dropped.----")
                else:
                    print("----No rows to drop.----")
            elif schoice == 4:
                if self.data.isnull().sum().sum() == 0:
                    print("----No Empty Values to Fill!----")
                else:
                    col = input("Enter column name: ")
                    val = input("Enter replacement value: ")
                    self.data[col].fillna(val, inplace=True)
                    print("----Missing values replaced!----")
            else:
                print("----Enter Valid Choice----!")

# 5. GENERATE DESCRIPTIVE STATISTICS

    def statistical_analysis(self):
        if self.data is None:
            print("Data-Set not loaded!")
        else:
            print("\n=====Statistical Data Displayed=====\n")
            dis = self.data.describe()
            print(dis)

# 6. VISUALIZATION

    def data_visual(self):
        if self.data is None:
            print("Data-Set not loaded!")
        
        while 1<2:
            print("""
== Data Visualization ==
1. Bar Plot
2. Line Plot
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Stack Plot
7. Main Menu
""")
            schoice = int(input("Enter your choice: "))

            if schoice == 7:
                break
            elif schoice == 1:
                print("Available Columne are:", list(self.data.columns))
                print()
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                try:
                    plt.bar(self.data[x], self.data[y])
                    plt.title("Bar Chart")
                    plt.show()
                    print("Bar Plot displayed Successfully!")
                except:
                    print("--Cannot Create.--")
            elif schoice == 2:
                print("Available Columne are:", list(self.data.columns))
                print()
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                try:
                    plt.plot(self.data[x], self.data[y])
                    plt.title("Line Chart")
                    plt.show()
                    print("Line Plot displayed Successfully!")
                except:
                    print("--Cannot Create.--")
            elif schoice == 3:
                print("Available Columne are:", list(self.data.columns))
                print()
                x = input("Enter X-axis column: ")
                y = input("Enter Y-axis column: ")

                try:
                    plt.scatter(self.data[x], self.data[y])
                    plt.title("Scatter Plot")
                    plt.show()
                    print("Scatter Plot displayed Successfully!")
                except:
                    print("--Cannot Create.--")
            elif schoice == 4:
                print("Available Columne are:", list(self.data.columns))
                print()
                col = input("Enter column for Pie chart: ")
                pie_data = self.data[col].value_counts()

                try:
                    plt.figure()
                    plt.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%")
                    plt.title("Pie Chart")
                    plt.show()
                    print("Pie chart displayed Successfully!")
                except:
                    print("--Cannot Create.--")
            elif schoice == 5:
                print("Available Columne are:", list(self.data.columns))
                print()
                col = input("Enter column for Histogram: ")

                try:
                    plt.figure()
                    plt.hist(self.data[col], bins=10)
                    plt.title("Histogram")
                    plt.show()
                    print("Histogram displayed Successfully!")
                except:
                    print("--Cannot Create.--")
            elif schoice == 6:
                print("Available Columne are:", list(self.data.columns))
                print()
                print("----Scatter Plot Inputs----")
                x1 = input("Enter X-axis column: ")
                y1 = input("Enter Y-axis column: ")

                print("----Bar Plot Inputs----")
                x2 = input("Enter X-axis column: ")
                y2 = input("Enter Y-axis column: ")

                try:
                    x_1 = self.data[x1]
                    y_1 = self.data[y1]

                    x_2 = self.data[x2]
                    y_2 = self.data[y2]

                    fig, axs = plt.subplots(1, 2, figsize=(10, 4))

                    axs[0].scatter(x_1, y_1)
                    axs[0].set_title("SCATTER CHART")

                    axs[1].bar(x_2, y_2)
                    axs[1].set_title("BAR CHART")
                    
                    plt.tight_layout()
                    plt.show()
                    print("Stack Plot displayed Successfully!")
                except:
                    print("--Cannot Create.--")
            else:
                print("--Enter Valid Choice!--")
    def save_plot(df):
        print("== Save Visualization ==")
        filename = input("Enter file name to save the plot (e.g., plot.png): ")

        try:
            plt.savefig(filename)
            print(f"Visualization saved as {filename} successfully!")
        except Exception as e:
            print("Error saving file:", e)



# FINAL FLOW

# Create ONE object for the entire program
obj1 = SalesDataAnalyzer()

while True:
    print("""
=============== Data Analysis & Visualization Program ===============
Please Select an Option:
1. Load Dataset
2. Explore Data
3. Perform Dataset Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
======================================================================
""")

    mchoice = int(input("Enter your choice: "))

    if mchoice == 8:
        print("Exiting the program. Goodbye!")
        break

    elif mchoice == 1:
        obj1.load_data()

    elif mchoice == 2:
        obj1.explore_data()

    elif mchoice == 3:
        obj1.data_frame()

    elif mchoice == 4:
        obj1.clean_data()

    elif mchoice == 5:
        obj1.statistical_analysis()

    elif mchoice == 6:
        obj1.data_visual()

    elif mchoice == 7:
        obj1.save_plot()

    else:
        print("Enter Valid Choice!")

