import random
from ptable import *

class repl:
    def __init__(self) -> None:
        self.hardness = 0
        self.subject = ""
    def start(self):
        if self.hardness == 0: self.hardness = int(input("Set your hardness (0-10): "))
        if self.subject == "": self.subject = str(input("Select your subject ('help' for assistance): "))
        print(self.subject)
        # import pdb; pdb.set_trace()
        while self.subject.lower() == "help":
            rows = [["Physics", "Chemistry", "Math", "Biology"], ["Computer Science", "Soft Skills", "Aptitude", "English"], ["French", "Machine Learning", "Data Mining", "Statistics"]]
            pt = ptable(rows)
            pt.make_row()
            print(pt.horizontal_str)

            self.subject = str(input("\nSelect your subject ('help' for assistance): "))
        while True:
            str(input("hello: "))


class sample_repl:
    def __init__(self) -> None:
        self.ques_number = int(input("Enter number of questions (make sure it is divisble by 5): "))
        while self.ques_number == 0 or self.ques_number%5 != 0 :
            self.ques_number = int(input("Enter a valid number of questions (make sure it is divisble by 5) (-1 to escape): "))
            if self.ques_number == -1: break

        self.skip_val = 5
        self.pt = ptable()
        self.correct = []
        self.failed=[]
        self.not_attended = list(range(self.ques_number+1))

        self.assistant_keyword = ["score", "subject"]
        self.pt = ptable()
    def start(self):
        i = 0
        while i <= self.ques_number:
            a = random.randint(5,10)
            print(a)
            user_input = str(input(f"Question numer {i} Enter a number between (0-10): "))

            if user_input in self.assistant_keyword:
                if user_input == "score":
                    self.pt.make_matrix(self.ques_number, self.skip_val, prefix="Level: ", correct=self.correct, failed=self.failed, not_attended=self.not_attended)

                if user_input.lower() == "subject":
                    rows = [["Physics", "Chemistry", "Math", "Biology"], ["Computer Science", "Soft Skills", "Aptitude", "English"], ["French", "Machine Learning", "Data Mining", "Statistics"]]
                    pt = ptable(rows)
                    pt.make_row()
                    print(pt.horizontal_str)
            else:
                if a == int(user_input):
                    self.correct.append(i+1)
                else: self.failed.append(i+1)
                i += 1

        # while self.subject.lower() == "score":
        #     rows = [["Physics", "Chemistry", "Math", "Biology"], ["Computer Science", "Soft Skills", "Aptitude", "English"], ["French", "Machine Learning", "Data Mining", "Statistics"]]
        #     pt = ptable(rows)
        #     pt.make_row()
        #     print(pt.horizontal_str)

        #     self.subject = str(input("\nSelect your subject ('help' for assistance): "))
        # while True:
        #     str(input("hello: "))


r = sample_repl()
r.start()