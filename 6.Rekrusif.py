# Created by : Muhammad athaberyl ramadhyli adl
def rekursifOddEven(i):
    if i > 0 :
        if(i%2 != 0):
            print("Odd Value  : {}".format(i))
        else:
            print("Even Value : {}".format(i))

        i = i - 1 # increment
        rekursifOddEven(i) #rekrusif loop(memanggil kelas itu sendiri)
    else:
        print(i)

number = int(input("masukkan batas nomer : "))
rekursifOddEven(number)