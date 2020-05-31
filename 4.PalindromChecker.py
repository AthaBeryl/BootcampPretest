# Created by : Muhammad athaberyl ramadhyli adl

#palindrom -> kalimat yg walau dibalik-balik ttp sama

class PalindromChecker:
    def validate(self,sentence):
        self.sentence = sentence
        convert = sentence.lower() #convert input ke lower case , because case sensitive...
        if(convert == convert[::-1]): # jika kalimat sama dengan hasil reverse nya maka..
            print ("This Sentence is a Palindrom")
        else:
            print("This Sentence is NOT a Palindrom")

        print("sentence          : {}".format(convert))
        print("reversed sentence : {}".format(convert[::-1]))
        print(" ")

validator = PalindromChecker()
validator.validate("kasur ini rusak")
validator.validate("kasur ini baru")

sentence = input("Try It Your Self, Input a Sentence : ")
validator.validate(sentence)
