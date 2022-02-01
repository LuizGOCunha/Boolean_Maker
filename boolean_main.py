from functions import boolean_creator, list_creator_prompt
from boolean_values import technology_values, work_values, location_values, platform_values, spoken_language_values

if __name__ == '__main__':
    pass

# In which languages our search should be in
# (I dont know how i will incorporate that yet, but we'll get there)
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

#       *********Remember that values and options should have respective orders!*********

#list of possible values of our different segments:
list_of_values = [technology_values,work_values,location_values,platform_values,spoken_language_values]

# Here we will ask the user for what they want, so we can create the string later
demanded_technologies = list_creator_prompt('technologies', technology_options)
demanded_works = list_creator_prompt('jobs', work_options)
demanded_locations = list_creator_prompt('locations', location_options)
demanded_platforms = list_creator_prompt('platforms', platform_options)
demanded_spoken_language = list_creator_prompt('language', spoken_language_options)

#list of all demands that our user made
list_of_demands = [demanded_technologies,demanded_works,demanded_locations,demanded_platforms,demanded_spoken_language]

# Here we process all those demands into a boolean string
boolean_string = boolean_creator(list_of_demands, list_of_values)

#Then we give it back to the user! :^)
print('Your boolean string is:')
print(boolean_string)