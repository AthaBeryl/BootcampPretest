# Created by : Muhammad athaberyl ramadhyli adl
class Grade:
    def __init__(self,score):
        self.score = score

    def scoreResult(self):
        if self.score >= 90:
            result = "A"
        elif self.score >= 80:
            result = "B"
        elif self.score >= 70:
            result = "C"
        elif self.score >= 60:
            result = "D"
        else:
            result = "E"
        return "Your score is {}, You got '{}' grade , Keep Practice !".format(self.score,result)

#validasi input hanya boleh integer
try:
    score = int(input("Enter Your Score:"))
    grade = Grade(score)
    print(grade.scoreResult())
except ValueError:
    print("This is not a number input")

