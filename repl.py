import random
from ptable import *
from commands import *

class test_repl:
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
        self.subject = str(input("Enter a subject: "))
        self.difficulty = str(input("Enter difficulty (0-100): "))

        self.skip_val = 5
        self.pt = ptable()
        self.correct = []
        self.failed=[]
        self.not_attended = list(range(self.ques_number+1))


        self.pt = ptable()
        self.arguments = [self.pt, self.ques_number, self.skip_val, self.correct, self.failed, self.not_attended]
    def start(self):
        i = 0
        while i <= self.ques_number:
            user_input = str(input(f"Explore or go to questions: "))

            if user_input in list(comm.keys()):
                while user_input.lower() != 'break':
                    comm[user_input.lower()](*self.arguments)
                    user_input = str(input(f"To go back to question, type 'break': "))
               
            while user_input.lower() != "menu":
                
                mcq_qa = question_comm['mcq'](self.subject, self.difficulty).splitlines()
                mcq_q = '\n'.join(mcq_qa[:-1])
                mcq_a = ''.join(mcq_qa[-1])
                print('\n'+mcq_q)
                
                user_input = str(input(f"Question numer {i+1}; Enter option (a-b): "))
                if user_input.lower() == "menu": break
                if mcq_a.lower() == str(user_input).lower():
                    self.correct.append(i+1)
                    print("Correct")
                else: 
                    self.failed.append(i+1)
                    print("Incorrect, correct option was: ", mcq_a)
                i += 1
                if self.ques_number >= i: break


r = sample_repl()
r.start()