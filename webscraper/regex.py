import re

def clean_deverence(data):

    # Remove excess spaces and line breaks
    data = re.sub(r'\n', '', data).strip()
    data =  re.sub(r'\s+', ' ', data).strip()
    print(data)

    # # Extract sections using regular expressions
    # name_match = re.search(r'deverence™', data)
    # if name_match:
    #     name = name_match.group()
    # else:
    #     name = ''

    # intro_match = re.search(r'Hello! Odunayo here\.(.*?)© — 2022', data, re.DOTALL)
    # if intro_match:
    #     intro = intro_match.group(1).strip()
    # else:
    #     intro = ''

    # # Extract selected works
    # selected_works = re.findall(r'(\d+\.\s.*?)\n', data)

    # # Structure the extracted data
    # structured_data = {
    #     "name": name,
    #     "intro": intro,
    #     "selected_works": selected_works,
    # }
    structured_data=data
    return structured_data
