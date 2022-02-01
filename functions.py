from validators import operation_finished, option_is_valid


def list_creator_prompt(segment, item_list):
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

def segment_creator_prompt(segment, item_list):
    # item list is our list of possible items
    segment = ""
    # item is the list of technologies selected by the user
    item = list_creator_prompt(segment, item_list)
    print('?')
    print('0 - No')
    print('1 - Yes')
    extra_item_choice = int(input('>'))
    if option_is_valid(extra_item_choice, range(0,2)):
        if extra_item_choice == 0:
            pass
        elif extra_item_choice == 1:
            pass

def item_parser(item_list, string_value_list):
    """Checks a number in a list of numbers, if it is equal to the index
        of a given list of values, adds these values to the return string"""
    parsed_string = ""
    for index, item in enumerate(item_list):
        for index_V, value in enumerate(string_value_list):
            if item == index_V:
                parsed_string += string_value_list[index_V]
                if index < len(item_list)-1:
                    parsed_string += " OR "
    return parsed_string
        

        


# list_of_demands is the list of all the user demands
# list_of_values is the list of all values that we can offer
def boolean_creator(list_of_demands, list_of_values):
    boolean_string = "("
    for demands, values in zip(list_of_demands,list_of_values):
        item_string = item_parser(demands, values)
        boolean_string += item_string + ') AND ('
    boolean_string = boolean_string[:-6]
    return boolean_string
   

def boolean_segment_creator(client_demand_lists):
    for list in client_demand_lists:
        if len(list) > 0:
            while True:
                print('There is more than one item in this segment.')
                print('Are they alternativez or mandatory?')
                print('0 - Alternative')
                print('1 - Mandatory')
                item_separation = int(input('>'))
                if option_is_valid(item_separation, range(0,2)):
                    print('Please insert a valid option')
                else:
                    break
        for index, item in enumerate(list):
            pass


if __name__ == '__main__':
    item_list = ['item 1', 'item 2', 'item 3', 'item 4']
    lista = list_creator_prompt('language', item_list)
    print(lista)