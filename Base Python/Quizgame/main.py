from data import question_data
from question_model import Question
from quiz_brain import Quizbrain
question_bank = []
for question in question_data:
    questiontext = question["text"]
    questionans = question["answer"]
    new_question = Question(questiontext,questionans)
    question_bank.append(new_question)
    
quiz = Quizbrain(question_bank)


while quiz.still_has_questions(): 
    quiz.nextquestion()

print(f"You have completed the quiz, Your final score was {quiz.score}/{quiz.question_number}")