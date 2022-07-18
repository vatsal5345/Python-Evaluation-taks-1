from problems.armstrong_number import Armstrong_Number
from problems.prime_number import Prime_Number
from problems.fibonaaci_series import Fibonaaci_Series

print("Welcome!! ")
print(" 1) fibonaaci series")
print(" 2) prime number")
print(" 3) armstrong number")
num = 0
num2 = int(input("choose the problem : "))
if num2 == 1:
    print(Fibonaaci_Series.run(num))
elif num2 == 2:
    print(Prime_Number.run(num))
elif num2 == 3:
    print(Armstrong_Number.run(num))
else:
    print("""invalid entry!!!!
please enter valid number....""")
