class Quizbrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def still_has_questions(self):
        if self.question_number <len(self.question_list):
            return True
        else:
            False
        
    def nextquestion(self):
        currentquest= self.question_list[self.question_number]
        self.question_number += 1
        ans= input(f"q.{self.question_number}:{currentquest.text}(True/False)")
        self.checkans(ans,currentquest.answer)
    def checkans(self, ans, correctanswer):
        if ans.lower() == correctanswer.lower():
            print("You got it right")
            score += 1
        else:
            print("Thats wrong")
            print(f"The correct answer was :{correctanswer}")
            print(f"Your score is {self.score}/{self.question_number}")
        print("\n")