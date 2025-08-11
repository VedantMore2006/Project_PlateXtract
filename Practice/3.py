i = 1
# p = int(input("Enter the principal amount: "))
while i < 2:
    p = int(input("Enter the principal amount: "))
    if p > 999:
        i += 1
    else:
        print("Enter Valid principal")


rate = int(input("Enter the rate of interest: "))
time = int(input("THE time period: "))
print(f"principal = {p}")
si = round((p * rate * time) / 100, 2)
print("The simple interest is: ", si)
