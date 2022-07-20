from problems.armstrong_number import ArmstrongNumber
from problems.prime_number import PrimeNumber
from problems.fibonaaci_series import FibonaaciSeries
from time_cal import result_time


@result_time
def mail_run():
    print("Welcome!! ")
    print(" 1) fibonaaci series")
    print(" 2) prime number")
    print(" 3) armstrong number")
    num = 0
    num2 = int(input("choose the problem : "))
    if num2 == 1:
        return FibonaaciSeries.run(num)
    elif num2 == 2:
        return PrimeNumber.run(num)
    elif num2 == 3:
        return ArmstrongNumber.run(num)
    else:
        return("""invalid entry!!!!
    please enter valid number....""")
