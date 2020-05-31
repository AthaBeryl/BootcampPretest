# Maximum , Minimum , and Average Getter from an Array
# Created by : Muhammad athaberyl ramadhyli adl


class Number:
    def __init__(self,numbers = []):
        self.numbers = numbers

    def average(self):
        arrVal = sum(self.numbers) #menjumlahkan seluruh index array
        arrLen = len(self.numbers) #menghitung total index
        averageResult = arrVal/arrLen #penghitungan rata-rata
        return "Average Value : {}".format(averageResult)

    def max(self):
        arrMax = sorted(self.numbers,reverse=True) #sort by desc
        return "Maximum Value : {}".format(arrMax[0]) #get first val

    def min(self):
        arrMax = sorted(self.numbers) #sory by asc
        return "Minimum Value : {}".format(arrMax[0])
#============================ STATIC / SAMPLE ========================
sample = [1,10,2,3,4]
number = Number(sample)
print("Deret Angka :",end=" ")
print(sample)
print(number.max())
print(number.min())
print(number.average())
print("======================================")
# ==================================DINAMIS
angka = input("Masukan Deret Angka (pisahkan dengan koma ) Contoh : 1,2,3,5 : ")
splitter = angka.split(',') #convert string to array (dengan koma sebagai indikatornya)
converter = map(int,splitter) #convert index array string ke integer
deretAngka = list(converter) #mengubah map menjadi array kembali
number = Number(deretAngka)
print("Deret Angka :",end=" ")
print(deretAngka)
print(number.max())
print(number.min())
print(number.average())