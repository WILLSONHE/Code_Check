# Name: Yuanhe Zhao
# Student Number:
# Assignment 2: Codes and Check Digits

import yuanhezhao_code_check  # importing code_check file


def quit_check(input_check):  # check if user enter 0
    if int(input_check) == 0:
        return False
    else:
        return True


def main():
    # let user input
    digit_input = str(input("Please enter code (digits only) (enter 0 to quit) "))
    result = quit_check(digit_input)
    # create list for each category
    summary_basic = []
    summary_position = []
    summary_upc = []
    summary_none = []
    while result:
        # let length be measured
        length_string = len(digit_input)
        # operate code check to have a result in boolean and digit return
        basic_code_result = yuanhezhao_code_check.basic_code_check(digit_input, length_string)
        positional_code_result = yuanhezhao_code_check.positional_code_check(digit_input, length_string)
        upc_code_result = yuanhezhao_code_check.upc_code_check(digit_input, length_string)
        # starting appending digit input that matches category
        if not basic_code_result[0] and not positional_code_result[0] and not upc_code_result[0]:
            summary_none.append(digit_input)
            print("--code: %s not Basic, Position or UPC code." % basic_code_result[1])
        elif basic_code_result[0] and positional_code_result[0] and upc_code_result[0]:
            summary_basic.append(digit_input)
            summary_position.append(digit_input)
            summary_upc.append(digit_input)
        elif basic_code_result[0] and not positional_code_result[0] and not upc_code_result[0]:
            summary_basic.append(digit_input)
        elif basic_code_result[0] and positional_code_result[0] and not upc_code_result[0]:
            summary_basic.append(digit_input)
            summary_position.append(digit_input)
        elif basic_code_result[0] and not positional_code_result[0] and upc_code_result[0]:
            summary_basic.append(digit_input)
            summary_upc.append(digit_input)
        elif not basic_code_result[0] and positional_code_result and not upc_code_result[0]:
            summary_position.append(digit_input)
        elif not basic_code_result[0] and positional_code_result[0] and upc_code_result[0]:
            summary_position.append(digit_input)
            summary_upc.append(digit_input)
        elif not basic_code_result[0] and not positional_code_result[0] and upc_code_result[0]:
            summary_upc.append(digit_input)
        # prompt user to keep inputting until have a 0 input
        digit_input = str(input("Please enter code (digits only) (enter 0 to quit) "))
        result = quit_check(digit_input)
    # start printing in each category in the same line
    print("\nSummary")
    basic_string_result = ", ".join(summary_basic)
    if basic_string_result == "":
        print("Basic: None")
    else:
        print("Basic:" + basic_string_result)
    position_string_result = ", ".join(summary_position)
    if position_string_result == "":
        print("Position: None")
    else:
        print("Position:" + position_string_result)
    upc_string_result = ", ".join(summary_upc)
    if upc_string_result == "":
        print("UPC: None")
    else:
        print("UPC:" + upc_string_result)
    none_string_result = ", ".join(summary_none)
    if none_string_result == "":
        print("None: None")
    else:
        print("None:" + none_string_result)


if __name__ == '__main__':
    main()
