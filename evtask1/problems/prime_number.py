from base import AbstractClass


class PrimeNumber(AbstractClass):
    def run(self):
        """program to fn the given number is prime or not"""
        num = int(input("enter the number to check whether it is prime or not..  "))
        if num > 1:
            for i in range(2, int((num/2)+1)):
                if num % i == 0:
                    print(num, "is not a prime number")
                    break
            else:
                print(num, "is a prime number")
        else:
            print(num, "invalid")
        return ''
    
# print(Prime_Number.run(num))
