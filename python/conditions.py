n = input("Number: ")

if  "." in n:
    value = float(n)
else:
    value = int(n)

    
if value > 0:
    print("n is positive")
elif value < 0:
    print("n is negative")
else:
    print("n is zero")