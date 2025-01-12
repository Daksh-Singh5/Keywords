num1=int(input("give me a number: "))

for i in range(1,num1+1):
    if i%20==0:
        print("twist")
        continue
    elif i%15==0:
        pass
    elif i%5==0:
        print("fizz")
        continue
    elif i%3==0:
        print("buzz")
        continue
    print(i)