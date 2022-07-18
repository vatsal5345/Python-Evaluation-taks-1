print("Welcome!! ")
print(" 1) fibonaaci series")
print(" 2) prime number")
print(" 3) armstrong number")

num = int(input("choose the problem : "))
if num == 1:
    from problems.fibonaaci_series import Fibonaaci_Series
    Fibonaaci_Series()
elif num == 2:
    from problems.prime_number import Prime_Number
    Prime_Number()
elif num == 3:
    from problems.armstrong_number import Armstrong_Number
    Armstrong_Number()
else:
    print("""invalid entry!!!!
please enter valid number....""")
