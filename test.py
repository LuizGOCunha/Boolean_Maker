from functions import boolean_creator, list_organizer, operation_finished, item_parser
from validators import option_is_valid


def test_that_tries_values_in_option_validation_function():
    print('test_that_tries_values_in_option_validation_function:')
    assert option_is_valid(0, range(0,10)) == True, '0 in (0,10) doesnt return True'
    assert option_is_valid(11, range(0,10)) == False, '11 in (0,10) doesnt return False'
    assert option_is_valid(5, range(0,10)) == True, '5 in (0,10) doesnt return True'
    assert option_is_valid(-1, range(0,10)) ==  False, '-1 in (0,10) doesnt return False'
    assert option_is_valid(9999, range(0,10)) == False, '9999 in (0,10) doesnt return False'
    assert option_is_valid(9, range(-99,99)) == True, '9 in (-99,99) doesnt return True'
    print('    ***Test successful***')

def test_that_verifies_operation_finished_validator():
    print('test_that_verifies_operation_finished_validator')
    input1 = 10
    input2 = "string"
    input3 = True
    input4 = 3.8
    for index, input in enumerate(['',input1,input2,input3,input4]):
        if index > 0:
            print(f'    input{index}: {input}')
    assert operation_finished(input1, 10) == True, 'input1 with finish flag 10 doesnt return True'
    assert operation_finished(input1, 9) == False, 'input1 with finish flag 9 doesnt return False'
    assert operation_finished(input1, '10') == False, 'input1 with finish flag 10 (string) doesnt return False'
    print('    input1: Test successful')
    assert operation_finished(input2, 'string') == True, 'input2 with finish flag "string" doesnt return True'
    assert operation_finished(input2, '10') == False, 'input2 with finish flag "10" doesnt return False'
    assert operation_finished(input2, False) == False, 'input2 with finish flag False doesnt return False'
    print('    input2: Test successful')
    assert operation_finished(input3, True) == True, 'input3 with finish flag True doesnt return True'
    assert operation_finished(input3, False) == False, 'input3 with finish flag False doesnt return False'
    assert operation_finished(input3, 3.9) == False, 'input3 with finish flag 3.9 doesnt return False'
    print('    input3: Test successful')
    assert operation_finished(input4, 3.8) == True, 'input4 with finish flag 3.8 doesnt return True'
    assert operation_finished(input4, 4.2) == False, 'input4 with finish flag 4.2 doesnt return False'
    assert operation_finished(input4, 3) == False, 'input4 with finish flag 3 doesnt return False'
    print('    input4: Test successful')
    print('    ***Test successful***')

    
    
     
def test_that_verify_parser_function():
    print('test_that_verify_parser_function:')
    string = item_parser([2,1,0],[['"python"', '"paithon"'],['"regex"', '"reg ex"'], ['"git"', '"GIT"']])
    string2 = item_parser([1,0],[['"python"', '"paithon"'],['"regex"', '"reg ex"'], ['"git"', '"GIT"']])
    string3 = item_parser([1,2,9],[['"python"', '"paithon"'],['"regex"', '"reg ex"'], ['"git"', '"GIT"']])
    assert string == '"git" OR "GIT" OR "regex" OR "reg ex" OR "python" OR "paithon"', f'{string} doesnt match'
    print("    " + string)
    assert string2 == '"regex" OR "reg ex" OR "python" OR "paithon"', f'{string2} doesnt match'
    print("    " + string2)
    assert string3 == '"regex" OR "reg ex" OR "git" OR "GIT"', f'{string3} doesnt match'
    print("    " + string3)
    print('    ***Test successful***')

def test_that_verify_the_result_of_boolean_creator():
    print('test_that_verify_the_result_of_boolean_creator:')
    list_of_demands = [[0,1], [2,3,1], [4,2,3]]
    list_of_values =[[['"fabia"', '"gunther"'], ['"Mathias"','"Hunter"'], ['"Gabriel"','"Francesca"']],
                    [['"134"','"564"'], ['"675"','"990"'], ['"009"','"921"'], ['"000"','"126"'], ['"112"','"674"']],
                    [['"a"','"b"'], ['"c"','"d"'], ['"e"','"f"'], ['"g"','"h"'], ['"i"','"j"']]]   
    boolean_string = boolean_creator(list_of_demands, list_of_values)
    print("    Boolean string = " + boolean_string)
    assert boolean_string == '''("fabia" OR "gunther" OR "Mathias" OR "Hunter") AND ("009" OR "921" OR "000" OR "126" OR "675" OR "990") AND ("i" OR "j" OR "e" OR "f" OR "g" OR "h")'''

    print("    Boolean string = " + boolean_string)
    print("    ***Test successful***")

def test_that_verifies_list_organizer_function():
    print('test_that_verifies_list_organizer_function')
    list = [7,5,5,3,2,1,0,4,6,7]
    print(f'    deorganized list:{list}')
    new_list = list_organizer(list)
    assert new_list == [0,1,2,3,4,5,6,7], f'{new_list} doesnt match'
    print('    organized list:' + f'{new_list}')
    print('    ***Test Successful***')





if __name__=='__main__':
    test_that_tries_values_in_option_validation_function()
    test_that_verifies_operation_finished_validator()
    test_that_verify_parser_function()
    test_that_verify_the_result_of_boolean_creator()
    test_that_verifies_list_organizer_function()