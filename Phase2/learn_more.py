import requests


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