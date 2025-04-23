class Quizbrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        
    def nextquestion(self):
        currentquest = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {currentquest.text} (True/False): ")
        self.checkans(ans, currentquest.answer)
        
    def checkans(self, ans, correctanswer):
        if ans.lower() == correctanswer.lower():
            print("You got it right")
            self.score += 1  # Fixed: changed 'score' to 'self.score'
        else:
            print("That's wrong")
            print(f"The correct answer was: {correctanswer}")
            
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")