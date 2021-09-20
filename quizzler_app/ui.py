from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # You can make sure you call in a QuizBrain class by doing this.
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = "Quizzler"
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.quiz_question = self.canvas.create_text(150, 125, text=f"Question",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR,
                                                     width=280)  # Text now wraps without going out of bounds.
        self.canvas.grid(columnspan=2, row=1, column=0, pady=50)

        false = PhotoImage(file="./images/false.png")
        true = PhotoImage(file="./images/true.png")
        self.false_button = Button(image=false, highlightthickness=0, bg=THEME_COLOR, command=self.answer_is_false)
        self.false_button.grid(row=2, column=1)
        self.true_button = Button(image=true, highlightthickness=0, bg=THEME_COLOR, command=self.answer_is_true)
        self.true_button.grid(row=2, column=0)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1, sticky='n')

        self.get_next_question()

        self.window.mainloop()  # This is like a never-ending while loop.

    def get_next_question(self):
        try:
            q_text = self.quiz.next_question()
        except IndexError:
            messagebox.showinfo(title="You have finished the quiz!",
                                message=f"Your final score was {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        else:
            self.canvas.itemconfig(self.quiz_question, text=q_text)
            self.canvas.config(bg='White')

    def answer_is_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answer_is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg='Green')
        else:
            self.canvas.config(bg='Red')
        self.window.after(1000, self.get_next_question)
        self.score_label.config(text=f"Score: {self.quiz.score}")





