from functions import boolean_creator, operation_finished, item_parser
from validators import option_is_valid


def test_that_tries_values_in_option_validation_function():
    print('test_that_tries_values_in_option_validation_function:')
    assert option_is_valid(0, range(0,10)) == True, '0 in (0,10) doesnt return True'
    assert option_is_valid(11, range(0,10)) == False, '11 in (0,10) doesnt return False'
    assert option_is_valid(5, range(0,10)) == True, '5 in (0,10) doesnt return True'
    assert option_is_valid(-1, range(0,10)) ==  False, '-1 in (0,10) doesnt return False'
    assert option_is_valid(9999, range(0,10)) == False, '9999 in (0,10) doesnt return False'
    assert option_is_valid(9, range(-99,99)) == True, '9 in (-99,99) doesnt return True'
    print('    Test successful')
     
def test_that_verify_parser_function():
    print('test_that_verify_parser_function:')
    string = item_parser([2,1,0],['"python"','"regex"', '"git"'])
    string2 = item_parser([1,0],['"python"','"regex"', '"git"'])
    assert string == '"git" OR "regex" OR "python"', f'{string} doesnt match'
    print("    " + string)
    assert string2 == '"regex" OR "python"', f'{string2} doesnt match'
    print("    " + string2)
    print('    Test successful')

def test_that_verify_the_result_of_boolean_creator():
    list_of_demands = [[0,1], [2,3,1], [4,2,3]]
    list_of_values =[['"fabia" OR "gunther"', '"Mathias" OR "Hunter"', '"Gabriel" OR "Francesca"'],
                    ['"134" OR "564"', '"675" OR "990"', '"009" OR "921"', '"000" OR "126"', '"112" OR "674"'],
                    ['"a" OR "b"', '"c" OR "d"', '"e" OR "f"', '"g" OR "h"', '"i" OR "j"']]   
    boolean_string = boolean_creator(list_of_demands, list_of_values)
    assert boolean_string == '''("fabia" OR "gunther" OR "Mathias" OR "Hunter") 
                            AND ("009" OR "921" OR "000" OR "126" OR "675" OR "990") 
                            AND ("i" OR "j" OR "e" OR "f" OR "g" OR "h")'''
    print(boolean_string)
    print("    Test successful")


if __name__=='__main__':
    test_that_tries_values_in_option_validation_function()
    test_that_verify_parser_function()
    test_that_verify_the_result_of_boolean_creator()