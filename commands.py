from ptable import *


def subjects(*_):
    rows = [["Physics", "Chemistry", "Math", "Biology"], ["Computer Science", "Soft Skills", "Aptitude", "English"], ["French", "Machine Learning", "Data Mining", "Statistics"]]
    pt = ptable(rows)
    pt.make_row()
    print(pt.horizontal_str)

def score(table_state, ques_number, skip_val, correct, failed, not_attended):
    table_state.make_matrix(ques_number, 
                            skip_val, 
                            prefix="Level: ", 
                            correct=correct, 
                            failed=failed, 
                            not_attended=not_attended)

comm = {"subjects": subjects, "score": score}