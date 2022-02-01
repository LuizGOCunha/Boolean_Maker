from validators import operation_finished, option_is_valid

def search_language_prompt():
    language_list =[]
    print('In which languages should our search be?')
    print('1 - English')
    print('2 - Portuguese')
    print('3 - Spanish')
    print('(Enter numbers one at a time please)')
    while True:
        language = input('>')
        if operation_finished(language, 'no'):
            return language_list
        language = int(language)
        if option_is_valid(language, range(1,4)):
            print('Anything else? (write "no" to stop)')
            language_list.append((language))
                
        elif not option_is_valid(language, range(1,4)):
            print('Only valid numbers, please.')

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



if __name__ == '__main__':
  
    item_list = ['item 1', 'item 2', 'item 3', 'item 4']
    lista = list_creator_prompt('language', item_list)
    print(lista)