# define three functions that doing code check availability


def basic_code_check(string_input, length_string):  # check for basic code
    n = 0
    sum_check = 0
    while n < length_string - 1:  # ensuring the code is excluding last digit
        digit = int(string_input[n])
        sum_check += digit
        n += 1
    last_digit_check = int(string_input[n])
    modulo_check = sum_check % 10  # modulo 10
    if last_digit_check == modulo_check:  # true if last digit match modulo result
        print("-- code: %s valid Basic code." % string_input)
        return True, string_input
    else:
        return False, string_input


def positional_code_check(string_input, length_string):  # check for positional code
    n = 0
    sum_check = 0
    while n < length_string - 1:
        digit = int(string_input[n])
        sum_check += digit * (n + 1)  # sum of position number times digit at position
        n += 1
    last_digit_check = int(string_input[n])
    modulo_check = sum_check % 10  # modulo 10
    if last_digit_check == modulo_check:  # true if last digit match modulo result
        print("-- code: %s valid Position code." % string_input)
        return True, string_input
    else:
        return False, string_input


def upc_code_check(string_input, length_string):  # check for UPC code
    n = 0
    sum_check = 0
    while n < length_string - 1:
        digit = int(string_input[n])
        odd_even_check = n % 2  # check for odd or even number
        if odd_even_check == 0:
            sum_check += (digit * 3)  # multiplying by 3 for each odd
        else:
            sum_check += (digit * 1)  # multiplying by 1 for each even
        n += 1
    last_digit_check = int(string_input[n])
    modulo_check = sum_check % 10  # modulo 10
    if modulo_check == 0:  # if modulo is 0, last digit is 0
        modulo_check = 0
    else:  # if modulo is 1 - 9, last digit is 10 - modulo
        modulo_check = 10 - modulo_check
    if last_digit_check == modulo_check:
        print("-- code: %s valid UPC code." % string_input)
        return True, string_input
    else:
        return False, string_input
