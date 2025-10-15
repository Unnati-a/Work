print("Welocme to the Interactive Personal Data Collector!")
print()

a=input("Please enter your name:")
b=int(input("Please enter your age:"))
c=float(input("Please enter your height in meters:"))
d=int(input("Please enter your favourite number:"))
print()

print("Thank You here is the information we collected:")
print()

print("Name:",a,("Type:", type(a), "Memory Address:",id(a)))
print("Age:",b,("Type:",type(b),"Memory Address:",id(b)))
print("Height:",c,("Type:",type(c),"Memory Address:",id(c)))
print("Favourite Number:",d,("Type:",type(d),"Memory Address:",id(d)))
print()

print("Your birth year is approximately:",2025-b,("based on your age of",b))
print()

print("Thank You for using the Personal Data Collector. Goodbye!")