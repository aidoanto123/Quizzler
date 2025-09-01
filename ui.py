from tkinter import *
from quiz_brain import QuizBrain
import time


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = Label(text=f'Score: {self.score}', fg="white", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280,text=f'idk', fill=THEME_COLOR, font=("Arial",20,"italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        #Buttons
        check_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=check_image, highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(column=0, row=2)

        cross_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=cross_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f'Score: {self.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f'You have reached the end of the quiz!\n\nWith a score of {self.score}/10',  font=("Arial",20,"bold"))
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

