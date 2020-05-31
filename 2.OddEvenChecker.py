# Created by : Muhammad athaberyl ramadhyli adl
class Number:

    def check(self,number):
        self.number = number
        # bilangan genap = habis dibagi 2 / modulus = 0
        if(number%2 != 0):
            return "{} is Odd".format(number)
        else:
            return"{} is Even".format(number)

number = Number()

# validasi input hanya boleh integer
try:
    numberInput = int(input("Enter Number :"))
    print(number.check(numberInput))
except ValueError:
    print("This is not a number input")




