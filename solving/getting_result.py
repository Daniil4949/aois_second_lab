ELEMENTS = ["!", "*", "+", "->", "=="]
ORDER = {
    "!": 5,
    "*": 4,
    "+": 3,
    "->": 2,
    "==": 1
}


def importance(sign):
    return ORDER[sign] if sign in ORDER else 0


def getting_value(logic_values, variables, values, elements, another_stack_elements):
    for value in logic_values:
        if value in variables:
            another_stack_elements.append(values[value])
        elif value in ELEMENTS:
            while len(elements) >= 1 and importance(elements[-1]) >= importance(
                    value):
                another_stack_elements.append(start_action(another_stack_elements, elements.pop()))
            elements.append(value)
        else:
            if value == "(":
                elements.append(value)
            else:
                while elements[-1] != "(":
                    another_stack_elements.append(start_action(another_stack_elements, elements.pop()))
                elements.pop()
    while len(elements) != 0:
        another_stack_elements.append(start_action(another_stack_elements, elements.pop()))
    return another_stack_elements.pop()


def start_action(stack_variables, sign):
    return not stack_variables.pop if sign == "1" else logic(stack_variables, sign)


def logic(stack_variables, flag):
    second_element = stack_variables.pop()
    first_element = stack_variables.pop()
    if flag == "*":
        return first_element and second_element
    elif flag == "+":
        return first_element or second_element
    elif flag == "->":
        return not (first_element and not second_element)
    else:
        return first_element == second_element
