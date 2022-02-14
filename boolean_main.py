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

# To create our boolean string, we separate our phrase into different segments, each with a different function:
# (technologies) AND (work) AND (location) AND (platform) AND (spoken language)
# each of these segments will have many useful words to our search, separated ("just" OR "like" OR "so")
# every item in our search will be associated with these words, like:
# python : "pyt*" OR "Pyt*" OR "pithon" OR "Paithon"
# So, when we choose our technology, we can go ahead and choose the work of our candidate(backend,frontend,etc)
# The process will continue until we have our options selected
# then we will go after the values exemplified in line 18, and append them in our string
# Until we have completed the string
# In the end we will have a Boolean string search created on our terms!

# Which technologies we will be searching
technology_options = ["Python", "Javascript", "Cloud", "PHP", "React","React Native", "Node.js"]

# What work will be made with this technology
work_options = ["Programmer", "DevOps"]

# In what location should we search our candidates
location_options = ["Latin America", "Brazil", "LatAm (No Brazil, no Mexico)"]

#In what platform we should search our candidates
platform_options = ["Linkedin"]

# What language should our candidates speak?
spoken_language_options = ["English"]

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