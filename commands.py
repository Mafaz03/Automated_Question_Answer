from openai_conv import chat_with_gpt
from ptable import *
import requests


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

comm = {"description": "Explore the menu for this tool", "subjects": subjects, "score": score}

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
    
    
    """Helps user gain more knowledge on the topic"""
   # return f"Wikipedia article on {keyword}"...Call the function(learn_more(keyword)).. 
   
    


    
question_comm = {"description": "Jump into questions", "mcq": mcq, "learn_more": learn_more}

class ASCII:
    @classmethod
    def menu(*_):
        print(f"""{bcolors.BRIGHT_GREEN}
    ,--,--,--. ,---. ,--,--, ,--.,--. 
    |        || .-. :|      \|  ||  | 
    |  |  |  |\   --.|  ||  |'  ''  ' 
    `--`--`--' `----'`--''--' `----'  
              {bcolors.RESET}""")
