from openai_conv import chat_with_gpt
from ptable import *


def subjects(*_):
    """Gets the subjects list"""
    rows = [["Physics", "Chemistry", "Math", "Biology"], ["Computer Science", "Soft Skills", "Aptitude", "English"], ["French", "Machine Learning", "Data Mining", "Statistics"]]
    pt = ptable(rows)
    pt.make_row()
    print(pt.horizontal_str)

def score(table_state, ques_number, skip_val, correct, failed, not_attended):
    """Gets Your score"""
    table_state.make_matrix(ques_number, 
                            skip_val, 
                            prefix="Level: ", 
                            correct=correct, 
                            failed=failed, 
                            not_attended=not_attended)

comm = {"subjects": subjects, "score": score}

def mcq(topic, difficulty,  *_):
    """Generates mcq"""
    return chat_with_gpt(f"""generate an MCQ on the topic: {topic}; Difficulty - {difficulty}; where 0-20 is easy, 20-40 is medium, 40-60 is hard, 60-80 is difficult, 80-100 is extremly difficult; give 3 options, label options a,b,c; the last line must contain the correct option only [eg: a]
                    example:
                    --------------
                    What is the unit of force in the International System of Units?
                    a) Newton
                    b) Joule
                    c) Watt

                    a
                    --------------
                    """)
    
question_comm = {"mcq": mcq}