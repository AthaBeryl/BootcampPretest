 # Kriteria Kabisat
 # 1. habis dibagi 4, tapi tidak habis dibagi 100
 # 2. habis dibagi 100 dan juga 400

# Created by : Muhammad athaberyl ramadhyli adl

class Kabisat:
    def validate(self,year,endyear):
        self.year = year
        self.endyear = endyear
        kabisat = [] # container tahun kabisat
        notKabisat = [] # container tahun non kabisat
        for i in range(year,endyear):
            if(year%4 == 0 and year%100 != 0 or year%100 == 0 and year%400 == 0): # realisasi rumus diatas
                kabisat.append(year) # menambahkan index ke kontainer
            else:
                notKabisat.append(year)
            year+=1 # increment

        print("List Tahun Kabisat {}".format(kabisat))
        print("List Tahun Non Kabisat {}".format(notKabisat))

kabisat = Kabisat()
kabisat.validate(int(input("Input Start Year : ")),int(input("Input End Year   : ")))


