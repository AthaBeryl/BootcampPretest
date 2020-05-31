# Created by : Muhammad athaberyl ramadhyli adl

#menjumlahkan(+) tanpa batas sampe ditekan key "="
numberContainer = []
isEnd = 0
while(isEnd < 1):
    number = input("Masukan Angka :")
    if(number == "="):
        isEnd = 1
        print("total dari penjumlahan",end="")
        print(numberContainer,end=" Adalah :")
    else:
        numberContainer.append(number)
numberContainer = map(int,numberContainer)
numberContainer = list(numberContainer)
print(sum(numberContainer))

