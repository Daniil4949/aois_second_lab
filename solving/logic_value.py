ELEMENTS = ["!", "+", "*", "->", "==", ")", "("]


def tokens_function(value, tokens_list, elements):
    variable = 0
    i = 0
    while i < len(value):
        if value[i].isalpha():
            tokens_list.append(elements[variable])
            i += (len(elements[variable]) - 1)
            variable += 1
        elif value[i] != ' ':
            if (value[i] == '-' and value[i + 1] == '>') or (
                    value[i] == '=' and value[i + 1] == '='):
                tokens_list.append(value[i:i + 2])
                i += 1
            else:
                tokens_list.append(value[i])
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


def elements_in_logic_val(element, elements, all_elements):
    for i in range(len(element)):
        if element[i].isalpha():
            var = 1
            while i + var < len(element) and element[i + var].isdigit():
                var += 1
            if element[i:i + var] not in elements:
                elements.append(element[i:i + var])
            all_elements.append(element[i:i + var])


def hooks(expression):
    try:
        first_hooks = expression.count("(")
        second_hooks = expression.count(")")
        if first_hooks == second_hooks:
            return True
        elif first_hooks > second_hooks:
            raise Exception("Incorrect. Symbol ')' is necessary here")
        else:
            raise Exception("Incorrect. Symbol ')' is not necessary here")
    except Exception as ex:
        print(ex)
        return False
