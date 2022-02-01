def option_is_valid(option, valid_range):
    if option in valid_range:
        return True
    if option not in valid_range:
        return False

def operation_finished(input, cancel_value):
    if input == cancel_value:
        return True
    else: 
        return False 