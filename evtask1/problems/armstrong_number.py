from base import AbstractClass


class ArmstrongNumber(AbstractClass):
    def run(self):
        """program to find the given number is armstrong number or not!!"""
        num = int(input("Enter a number to check whether the number is armstrong number or not : "))
        newsum = 0
        temp = num
        while temp > 0:
            n = len(str(temp))
            for i in range(n):
                digit = temp % 10
                newsum += digit ** n
                temp //= 10
            if num == newsum:
                print(num, "is an Armstrong number")
            else:
                print(num, "is not an Armstrong number")
            return ""

# num = int(input("Enter a number to check whether the number is armstrong number or not : "))
# print(Armstrong_Number.run(num))
