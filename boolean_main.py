from functions import search_language_prompt

if __name__ == '__main__':
    pass
# In which languages our search should be in
language_options = ['English', 'Spanish', 'Portuguese']
# 0 - English
# 1 - Spanish
# 2 - Portuguese

# Which technologies we will be searching
technology_options = []

# What work will be made with this technology
work_options = []

# In what location should we search our candidates
location_options = []

#In what platform we should search our candidates
platform_options = []

# What language should our candidates speak?
spoken_language_options = []



language_list = search_language_prompt()
print(language_list)