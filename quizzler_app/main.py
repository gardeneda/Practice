from question_model import Question
from data_list import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# This tkinter works by having a mainloop, which is essentially like another while loop.
# It's constantly going to check if it needs to update something or if there's a user interaction.
# Therefore, it'll get confused if you have another while loop near it.
# This is why we need to comment the code below out.

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
