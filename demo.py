role = str(input("Enter your role :"))
age = int(input("Enter your age :"))
a = bool(role == "Student" and age < 21)
print("Eligible :",a)
