from validators import operation_finished, option_is_valid


def list_creator_prompt(segment, item_list):
    """Creates a list of the demands that our user has, related to an specific segment"""
    list = []
    valid_range = []
    print(f'Which {segment} should our search include?')
    for index, item in enumerate(item_list):
        print(f'{index} - {item}')
        valid_range.append(index)
    print('(Enter numbers one at a time please)')
    while True:
        item = input('>')
        if operation_finished(item, 'no'):
            return list
        item = int(item)
        if option_is_valid(item, valid_range):
            print('Anything else? (write "no" to stop)')
            list.append((item))
                
        elif not option_is_valid(item, range(1,4)):
            print('Only valid numbers, please.')


def item_parser(item_list, string_value_list):
    """Checks a number in a list of numbers, if it is equal to the index
        of a given list of values, adds these values to the return string"""
    parsed_string = ""
    for index, item in enumerate(item_list):
        for index_V, value in enumerate(string_value_list):
            if item == index_V:
                for word in value:
                    parsed_string += word
                    parsed_string += " OR "
    parsed_string = parsed_string[:-4]
    return parsed_string
        
def list_organizer(list_v):
    """Função que organiza listas criadas ao colocá-las em ordem e remover números repetidos"""
    list_v.sort()
    list_v = set(list_v)
    list_v = list(list_v)
    return list_v
        


# list_of_demands is the list of all the user demands
# list_of_values is the list of all values that we can offer
def boolean_creator(list_of_demands, list_of_values):
    """This function looks into the demands of the user, then looks for it in the list of
    values, then starts creating a boolean search string based on the demands and values given"""
    boolean_string = "("
    for demands, values in zip(list_of_demands,list_of_values):
        item_string = item_parser(demands, values)
        boolean_string += item_string + ') AND ('
    boolean_string = boolean_string[:-6]
    return boolean_string
   

if __name__ == '__main__':
    pass