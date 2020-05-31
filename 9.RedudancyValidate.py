# Created by : Muhammad athaberyl ramadhyli adl

class Normalize():
    def deleteRedudancy(self,data = []):
        self.data = data;
        data = list(dict.fromkeys(data))
        print(data)


normalize = Normalize()
normalize.deleteRedudancy(["Jakarta", "Aceh", "Malang", "Medan", "Bontang", "Jogja", "Jakarta", "Bandung", "Malang", "Solo", "Palembang", "Bandung"]
)