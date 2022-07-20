from base import AbstractClass


class FibonaaciSeries(AbstractClass):
    def run(self):
        """to find fibonacci number at position : initial values are 0 and 1 then 
        add this process till given position."""
        num = int(input("enter number to find the fibonaaci term : "))
        p = 1
        q = 0
        if num < 0:
            return 'invalid input'
        elif num == 0:
            return q
        elif num == 1:
            return p
        else:
            for i in range(2, num+2):
                mysum = p + q
                p = q
                q = mysum
            return q

# print(Fibonaaci_Series.run(num))
