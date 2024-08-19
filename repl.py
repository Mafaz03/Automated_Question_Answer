import random
from ptable import *
from commands import *
from prettytable import PrettyTable
from colors import *


def show_table(rows):
    pt = ptable(rows)
    pt.make_row()
    print(pt.horizontal_str)

def show_ptable(rows):
    pt = PrettyTable()
    pt.field_names = rows[0]
    for row in rows[1:]:
        pt.add_row(row)
    print(pt)

def color_text(string, color):
    return color + string + bcolors.RESET


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
        asked = []
        i = 0
        while i <= self.ques_number:
            ASCII.menu()
            show_table([["Command", "Description"], ["Menu (you are here)", comm['description']], ["Questions", question_comm["description"]]])

            user_input = str(input(f"Explore or go to questions: "))
            if user_input.lower() == 'help':
                show_table([["Command", "Description"]] + [[k, comm[k].__doc__] for k in list(comm.keys()) if k != "description"] + [['questions', 'Go towards questions']])

            if user_input in list(comm.keys()):

                while user_input.lower() != 'break':
                    comm[user_input.lower()](*self.arguments)
                    user_input = str(input(f"To go back to question, type 'break': "))
                    if user_input.lower() == 'help':
                        show_table([["Command", "Description"], ['break', 'Go towards questions']])

            if user_input.lower() == 'questions':
                while user_input.lower() != "menu":
                    
                    if i == 0: asked.append('')
                    else: asked.append(mcq_qa[0])
                    mcq_qa = question_comm['mcq'](self.subject, self.difficulty, "\n".join(asked)).splitlines()
                    mcq_q = '\n'.join(mcq_qa[:-1])
                    mcq_a = ''.join(mcq_qa[-1])
                    # import pdb; pdb.set_trace()
                    print('\n'+color_text(mcq_q,bcolors.BRIGHT_MAGENTA))
                    # print(asked)
                    
                    user_input = str(input(f"Question numer {i+1}; Enter option (a-d): "))
                    if user_input.lower() == 'help':
                        show_table([[k, question_comm[k].__doc__] for k in list(question_comm.keys()) if k != "description"])

                    if user_input.lower() == "menu": break

                    ans = str(user_input).lower()
                    option = mcq_a[0]
                    answer = mcq_a[2:]
                    # print(option, ans[0])
                    if option.lower() == ans[0]:                    
                        self.correct.append(i+1)
                        print(color_text("\nCorrect\n", bcolors.YELLOW))
                    else: 
                        self.failed.append(i+1)
                        print(color_text(f"\nIncorrect, correct option was: {mcq_a}\n", bcolors.RED))

                    user_input = str(input("Read for next question? (learn more/Y): "))
                    if user_input.lower() == 'help':
                        show_table([[k, question_comm[k].__doc__] for k in list(question_comm.keys()) if k != "description"])
                    if user_input.lower() == "learn more":
                        wiki_result = question_comm['learn_more'](answer)
                        print(wiki_result)
                        print("\nReturning to questions")
                    i += 1
                    if i >= self.ques_number : break


r = sample_repl()
r.start()