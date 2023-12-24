from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []

for question in question_data:

    questionObject = Question(question["question"], question["correct_answer"])
    questionBank.append(questionObject)

quiz = QuizBrain(questionBank)

while quiz.stillHasQuestion():
    quiz.nextQuestion()

print("You've completed the quiz")
print(f"Your final score was {quiz.score} / {quiz.questionNumber}")