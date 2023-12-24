class QuizBrain:
    def __init__(self, questionList):
        self.questionNumber = 0
        self.questionList = questionList
        self.score = 0

    def stillHasQuestion(self):
        return self.questionNumber < len(self.questionList)

    def nextQuestion(self):
        question = self.questionList[self.questionNumber]
        self.questionNumber += 1

        answer = input(f"Q.{self.questionNumber}: {question.text} (True/False): ")
        self.checkAnswer(answer, question.answer)

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer == correctAnswer:
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correctAnswer}")
        print(f"Your current score is: {self.score} / {self.questionNumber}\n")
