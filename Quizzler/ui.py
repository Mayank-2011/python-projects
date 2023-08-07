from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUi:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250)
        self.canvas_text = self.canvas.create_text(150, 125, width=280, text='Questions', font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.score = Label(text="Score: ", bg=THEME_COLOR, fg="White")
        self.score.grid(column=1, row=0, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file='images/false.png')

        self.true_button = Button(image=true_img, bg=THEME_COLOR, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2, pady=50)

        self.false_button = Button(image=false_img, bg=THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"You have reached the end of the quiz. Your final score is {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

