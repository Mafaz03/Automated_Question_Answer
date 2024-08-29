from openai_conv import chat_with_gpt
from ptable import *
import requests


def print_bar_graph(data, bar_char='█', width=50):
    print("\n\n")
    max_value = max(data.values())
    
    for key, value in data.items():
        bar_length = int((value / max_value) * width)
        bar = bar_char * bar_length
        print(f'{key}: {bar} {value}', end='\n')
    print("\n\n")
def subjects(*_):
    """Gets the subjects list (stil dev..)"""
    rows = [["Physics", "Chemistry", "Math", "Biology"], ["Computer Science", "Soft Skills", "Aptitude", "English"], ["French", "Machine Learning", "Data Mining", "Statistics"]]
    pt = Ptable(rows)
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
    print(f"\n{len(correct)} out of {ques_number}")
    if len(correct) + len(failed) == ques_number: print("\nCongrats, quizz completed\n")
    else: print(f"\n{ques_number-(len(correct) + len(failed))} questions yet to attend\n")
    
def help(*_):
    """View possible commands"""
    pass

def report(_, ques_number, __, correct, failed, not_attended):
    """Generates report"""
    keys = ["Total Questions|", "Correct|", "failed|", "not_attended|"]
    max_len = len(max(keys, key=len))
    data = {
        " "*(max_len-len(keys[0])) + keys[0]: ques_number,
        " "*(max_len-len(keys[1])) + keys[1]: len(correct),
        " "*(max_len-len(keys[2])) + keys[2]: len(failed),
        " "*(max_len-len(keys[3])) + keys[3]: ques_number - (len(correct)+len(failed))
    }
    print_bar_graph(data=data)


comm = {"description": "Explore the menu for this tool", "subjects": subjects, "score": score, "help": help, "report": report}

def mcq(topic, difficulty, asked, *_):
    """Generates mcq"""
    return chat_with_gpt(f"""generate an MCQ on the topic: {topic}; Difficulty - {difficulty}; where 0-20 is easy, 20-40 is medium, 40-60 is hard, 60-80 is difficult, 80-100 is extremly difficult; give 4 options, label options a,b,c,d; the last line must contain the correct option only [eg: a]
                    example:
                    
What is the unit of force in the International System of Units?
a) Newton
b) Joule
c) Watt
d) Amps
                         
a Newton
                   
dont ask:
{asked}
                    """)

def learn_more(keyword):
    # Add logic here HAMDAN
    search_url = "https://www.wikidata.org/w/api.php"
    search_params = {
        "action": "wbsearchentities",
        "search": keyword,
        "language": "en",
        "format": "json"
    }
    response = requests.get(search_url, params=search_params)
    search_results = response.json()
    if not search_results['search']:
        return f"Sorry, no results found for '{keyword}'."

    # Get the first entity ID (usually the most relevant one)
    entity_id = search_results['search'][0]['id']
    

    # Get detailed information about the entity
    details_url = "https://www.wikidata.org/w/api.php"
    details_params = {
        "action": "wbgetentities",
        "ids": entity_id,
        "format": "json",
        "languages": "en"
    }
    details_response = requests.get(details_url, params=details_params)
    entity_data = details_response.json()

    # Extract the relevant structured information
    entity_info = entity_data['entities'][entity_id]
    entity_label = entity_info.get('labels', {}).get('en', {}).get('value', 'N/A')
    entity_description = entity_info.get('descriptions', {}).get('en', {}).get('value', 'N/A')

    # Generate the Wikipedia link based on the entity label
    wikipedia_link = f"https://en.wikipedia.org/wiki/{entity_label.replace(' ', '_')}"

    # Format the information into a paragraph
    paragraph = f"""
The {entity_label} is best described as {entity_description}. 

For more detailed information, you can visit the Wikipedia page: {wikipedia_link}.

"""

    return paragraph
    
    
#Helps user gain more knowledge on the topic
   # return f"Wikipedia article on {keyword}"...Call the function(learn_more(keyword)).. 
   
    
question_comm = {"description": "Jump into questions", "mcq": mcq, "learn_more": learn_more}

registered = {'trainer': ["mafaz", "doremon"], 'user': ["Mafaz", "Doremon"]}

def trainer():
    """Trainer Access"""
    user = str(input("\nEnter username: "))
    password = str(input("Enter password: "))
    if registered['trainer'][0] == user and registered['trainer'][1] == password: return True
    else: False

def user():
    """User Access"""
    user = str(input("\nEnter username: "))
    password = str(input("Enter password: "))
    if registered['user'][0] == user and registered['user'][1] == password: return True
    else: False
    

roles_auth = {"description": "Roles", "trainer": trainer, "user": user}

class ASCII:
    # font: Soft
    @classmethod
    def menu(*_):
        print(f"""{bcolors.BRIGHT_GREEN}
    ,--,--,--. ,---. ,--,--, ,--.,--. 
    |        || .-. :|      \|  ||  | 
    |  |  |  |\   --.|  ||  |'  ''  ' 
    `--`--`--' `----'`--''--' `----'  
              {bcolors.RESET}""")
        
    def CirGen(*_):
        print(f"""{bcolors.BRIGHT_GREEN}                                                                                                                                                   
    ,-----.                      ,--.              ,--.                       ,----.                                          ,--.  ,--.                
    '  .--./,--.,--.,--.--.,--.--.`--' ,---.,--.,--.|  |,--.,--.,--,--,--.    '  .-./    ,---. ,--,--,  ,---. ,--.--. ,--,--.,-'  '-.`--' ,---. ,--,--,  
    |  |    |  ||  ||  .--'|  .--',--.| .--'|  ||  ||  ||  ||  ||        |    |  | .---.| .-. :|      \| .-. :|  .--'' ,-.  |'-.  .-',--.| .-. ||      \ 
    '  '--'\'  ''  '|  |   |  |   |  |\ `--.'  ''  '|  |'  ''  '|  |  |  |    '  '--'  |\   --.|  ||  |\   --.|  |   \ '-'  |  |  |  |  |' '-' '|  ||  | 
    `-----' `----' `--'   `--'   `--' `---' `----' `--' `----' `--`--`--'     `------'  `----'`--''--' `----'`--'    `--`--'  `--'  `--' `---' `--''--' 
              {bcolors.RESET}""")
