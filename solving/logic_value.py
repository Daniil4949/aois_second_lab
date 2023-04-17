ELEMENTS = ["!", "+", "*", "->", "==", ")", "("]


def tokens_function(expression, tokens_list, all_elements):
    variable = 0
    i = 0
    while i < len(expression):
        if expression[i].isalpha():
            tokens_list.append(all_elements[variable])
            i += (len(all_elements[variable]) - 1)
            variable += 1
        elif expression[i] != ' ':
            if (expression[i] == '-' and expression[i + 1] == '>') or (
                    expression[i] == '=' and expression[i + 1] == '='):
                tokens_list.append(expression[i:i + 2])
                i += 1
            else:
                tokens_list.append(expression[i])
        i += 1


def correct_vars(element):
    try:
        if len(element) > 1 and element[1] == '0':
            raise Exception(f"Incorrect - \"{element}\"")
        for i in range(1, len(element)):
            if not element[i].isdigit():
                raise Exception(f"Incorrect - \"{element}\"")
        return True
    except Exception as ex:
        print(ex)
        return False


def check(element, elements):
    try:
        if element in elements:
            return correct_vars(element)
        elif element in ELEMENTS:
            return True
        else:
            raise Exception(f"Unknown symbol \"{element}\"")
    except Exception as ex:
        print(ex)
        return False


def tokens_check(elements, values):
    try:
        for i in range(len(elements) - 1):
            if elements[i] in values and elements[i + 1] in values:
                raise Exception("Incorrect value")
    except Exception as ex:
        print(ex)
        return False
    return True


def valid_logic_value(values, tokens, only_values):
    if len(only_values) == 0:
        print("I do not see any variables here...")
        return False
    for token in tokens:
        if not check(token, only_values):
            return False
    return hooks(values) and tokens_check(tokens,
                                          only_values)


def elements_in_logic_val(expression, variables, all_values):
    for i in range(len(expression)):
        if expression[i].isalpha():
            var = 1
            while i + var < len(expression) and expression[i + var].isdigit():
                var += 1
            if expression[i:i + var] not in variables:
                variables.append(expression[i:i + var])
            all_values.append(expression[i:i + var])


def hooks(expression):
    try:
        opening_brackets = expression.count("(")
        closing_brackets = expression.count(")")
        if opening_brackets == closing_brackets:
            return True
        elif opening_brackets > closing_brackets:
            raise Exception("Incorrect. Symbol ')' is necessary here")
        else:
            raise Exception("Incorrect. Symbol ')' is not necessary here")
    except Exception as ex:
        print(ex)
        return False
