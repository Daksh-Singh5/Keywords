bill = int(input("please enter your bill: "))
noOfDays= int(input("please enter the number of days the bill is pending: "))
costadded= 0
for i in range(1,noOfDays+1):
    costadded += bill//3
    bill+=costadded

print("your bill is",bill,"with 3 persent added each day")
