class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, ans, ques_ans):
        if ans == ques_ans:
            self.score += 1
            print("You got it Right!")
        else:
            print("That's Wrong.")
        print(f"The correct answer was: {ques_ans}.\nYour score is {self.score}/{self.question_number}\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        quiz_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").title()
        self.check_answer(quiz_ans, current_question.answer)
