from functions import search_language_prompt, operation_finished
from validators import option_is_valid


def test_that_tries_values_in_option_validation_function():
    print('test_that_tries_values_in_option_validation_function:')
    assert option_is_valid(0, range(0,10)) == True, '0 in (0,10) doesnt return True'
    assert option_is_valid(11, range(0,10)) == False, '11 in (0,10) doesnt return False'
    assert option_is_valid(5, range(0,10)) == True, '5 in (0,10) doesnt return True'
    assert option_is_valid(-1, range(0,10)) ==  False, '-1 in (0,10) doesnt return False'
    assert option_is_valid(9999, range(0,10)) == False, '9999 in (0,10) doesnt return False'
    assert option_is_valid(9, range(-99,99)) == True, '9 in (-99,99) doesnt return True'
    print('Test successful')
     


if __name__=='__main__':
    test_that_tries_values_in_option_validation_function()