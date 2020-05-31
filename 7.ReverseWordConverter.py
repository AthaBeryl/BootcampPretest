# Created by : Muhammad athaberyl ramadhyli adl

# Contoh Output : Saya Tamvan dan Pemberani
# Hasil Convert yang diharapkan : ayaS navmaT nad inarebmeP
# Hasil Convert yang tidak diharapkan : inarebmeP nad navmaT ayaS

class ReverseWord:
    def reverse(self,sentence):
        self.sentence = sentence
        reversed = sentence[::-1] #reverse jadi :  inarebmeP nad navmaT ayaS
        reversedToArray = reversed.split(' ') #hasil reverse dijadiin array : [inarebmeP,nad,navmaT,ayaS]
        reversedArray = reversedToArray[::-1] #setelah dijadikan array, index array nya di reverse
        reversedSentence = ' '.join(reversedArray) #setelah itu disatukan lagi menjadi kalimat
        print("Original Word : {}".format(self.sentence))
        print("Reversed (per word) : {}".format(reversedSentence))

print("Example :")
sentence = ReverseWord()
sentence.reverse("Saya Tamvan dan Pemberani")
print("=====================================")
sentence.reverse(input("Try it Yourself , Input a Sentence : "))



