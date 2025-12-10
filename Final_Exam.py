print("The value of __name__ is:", __name__)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class RetailAnalyzer:

    # 1. Initialization
    # ----------------------------------------------------
    def __init__(self):
        self.data = None

    # 2. Load Dataset
    # ----------------------------------------------------  
    def load_data(self, file_path):

        if not file_path.endswith(".csv"):
            print("\n---File must me CSV---\n")
            return
        try:
            self.data = pd.read_csv(file_path)
            print("\n---File loaded successfully!---\n")
        except:
            print("\n---Cannot read the file---\n")


    # 3. Clean Dataset
    # ----------------------------------------------------
    """
    - ffill = will take data from previous and fill
    """
    def clean_data(self):
        print("\n-------Find and Clean Missing Data-------\n")
        while 1<2:
            print("1. See Missing Rows in Data")
            print("2. Fill the Missing Values")
            print("3. Return to Main Menu\n")
            
            choice = int(input("Enter your Choice: "))
            if choice == 3:
                break
            elif choice == 1:
                missing = self.data[self.data.isnull().any(axis=1)]
                if missing.empty:
                    print("\n---No missing rows!---\n")
                else:
                    print(missing)
            elif choice == 2:
                self.data.fillna(method='ffill', inplace=True)
                print("\n---Missing Values Auto-Filled!---\n")
            else:
                print("\n---Enter Valid Choice---\n")


    # 4. Calculate Metrics
    # ----------------------------------------------------
    """
    - dict is created for all values THAN through looping values exctration is done
    """
    def calculate_metrics(self):
        if self.data is None:
            print("\n---Data-Set not loaded!---\n")
        
        print("\n---Calculated Metrics---\n")

        # Total sales using NumPy
        total_sales = np.sum(self.data["Total Sales"])

        # Average sales using NumPy
        avg_sales = np.mean(self.data["Total Sales"])

        # Most popular product
        most_popular = self.data["Product"].mode()[0]

        metrics = {
            "Total Sales": total_sales,
            "Average Sales": avg_sales,
            "Most Popular Product": most_popular
        }

        return metrics
    
    
    # 5. Filter Data by Category or Date Range
    # ----------------------------------------------------
    """
    - strip = removes extra spaces.
    - unique = provide all unique values from column
    - for filter = Available filters are given (for smooth usage)
    """
    def filter_data(self, condition):
        if self.data is None:
            print("\n---Data-Set not loaded!---\n")

        cond = condition.lower().strip()

        valid_filters = ["category", "date>", "date<"]
        if cond not in valid_filters:
            print("\n---Error with spelling! Choose: category, date>, date< ---\n")
            return
        
        if cond == "category":
            try:
                print("\n----Available Categories----\n")
                print(self.data["Category"].unique())
                print()
                sub_cat = input("Enter category: ").strip()
                result = self.data[self.data["Category"].str.lower() == sub_cat.lower()]
                print(result)
            except Exception as e:
                print(f"---Error in Filtering: {e}---")

        elif cond == "date>":
            try:
                print("\n-----Available Dates----\n")
                print(self.data["Date"].unique())
                print()
                d = input("Enter date (YYYY-MM-DD): ").strip()

                result = self.data[self.data["Date"] > d]
                print(result)
            except Exception as e:
                print(f"---Error in Filtering: {e}---")
        
        elif cond == "date<":
            try:
                print("\n-----Available Dates----\n")
                print(self.data["Date"].unique())
                print()
                d = input("Enter date (YYYY-MM-DD): ").strip()

                result = self.data[self.data["Date"] < d]
                print(result)
            except Exception as e:
                print(f"---Error in Filtering: {e}---")
    

    # 6. Display Summary Report
    # ----------------------------------------------------
    """
    - describe = will display all statistical summary of data
    - info = display overall information of data
    """
    def display_summary(self):
        if self.data is None:
            print("\n---Data-Set not loaded!---\n")
        
        print("\n---Data-Stastical Summary---\n")
        summary = self.data.describe()
        print(summary)

        print("\n---Data-Set Summary---\n")
        inf_sum = self.data.info()
        print(inf_sum)

    
    #  7. Visualizations (Matplotlib + Seaborn)
    # ----------------------------------------------------
    def bar_chart(self):
        if self.data is None:
            print("\n---Data-Set not loaded!---\n")

        plt.figure(figsize=(8, 5))
        sns.barplot(x="Category", y="Total Sales", data=self.data, estimator=sum, color="green", hue="Category")
        plt.title("Total Sales by Category")
        plt.show()

    def line_graph(self):
        if self.data is None:
            print("\n---Data-Set not loaded!---\n")
        
        df = self.data.copy()
        df["Date"] = pd.to_datetime(df["Date"])
        df.sort_values("Date", inplace=True)

        plt.figure(figsize=(8, 5))
        plt.plot(df["Date"], df["Total Sales"])
        plt.title("Sales Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Total Sales")
        plt.show()
    
    def heatmap(self):
    # Correlation only for 2 columns asked
        if self.data is None:
            print("\n---Data-Set not loaded!---\n")

        plt.figure(figsize=(6, 4))
        corr = self.data[["Price", "Quantity Sold"]].corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.show()


# A. MAIN WORKING
# ----------------------------------------------------
analyzer = RetailAnalyzer()

while 1<2:
    print("""
===== Retail Sales Analyzer =====
1. Load File
2. Clean Data
3. Calculate Metrics
4. Filter-Data
5. Display Summary
6. Bar Chart
7. Line Chart
8. Heat Map
9. Exit
""")

    main_choice = int(input("Enter your Choice: "))

    if main_choice == 9:
        print("\n------Exiting the Program------\n")
        break

    elif main_choice == 1:
        path = input("Enter CSV file path eg=(U:/Datasets/train.csv): ")
        analyzer.load_data(path)

    elif main_choice == 2:
        analyzer.clean_data()

    elif main_choice == 3:
        full_dict = analyzer.calculate_metrics()
        for key, values in full_dict.items():
                    print(f"{key} ===> {values}")

    elif main_choice == 4:
        print("\nFilter Options: category / date> / date<\n")
        cond = input("Enter filter type: ").strip()
        analyzer.filter_data(cond)

    elif main_choice == 5:
        analyzer.display_summary()

    elif main_choice == 6:
        analyzer.bar_chart()

    elif main_choice == 7:
        analyzer.line_graph()

    elif main_choice == 8:
        analyzer.heatmap()

    else:
        print("\n---Enter Valid Choice---\n")
