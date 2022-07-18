from base import Abstract_class


class Armstrong_Number(Abstract_class):
    def run(self):
        """program to find the given number is armstrong number or not!!"""
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10
        if num == sum:
            print(num,"is an Armstrong number")
        else:
            print(num,"is not an Armstrong number")
        return ""

num = int(input("Enter a number to check whether the number is armstrong number or not : "))
print(Armstrong_Number.run(num))
