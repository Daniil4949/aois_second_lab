def getting_result(tokens, variables, values, stack_elements, stack_variables):
    signs = ["!", "*", "+", "->", "=="]
    for token in tokens:
        if token in variables:
            stack_variables.append(values[token])
        elif token in signs:
            while len(stack_elements) >= 1 and priority(stack_elements[-1]) >= priority(
                    token):
                stack_variables.append(execute_operation(stack_variables, stack_elements.pop()))
            stack_elements.append(token)
        else:
            if token == "(":
                stack_elements.append(token)
            else:
                while stack_elements[-1] != "(":
                    stack_variables.append(execute_operation(stack_variables, stack_elements.pop()))
                stack_elements.pop()
    while len(stack_elements) != 0:
        stack_variables.append(execute_operation(stack_variables, stack_elements.pop()))
    return stack_variables.pop()


def binary(stack_variables, sign):
    second_value = stack_variables.pop()
    first_value = stack_variables.pop()
    if sign == "*":
        return first_value and second_value
    elif sign == "+":
        return first_value or second_value
    elif sign == "->":
        return not (first_value and not second_value)
    else:
        return first_value == second_value


def execute_operation(stack_variables, sign):
    if sign == "!":
        return not stack_variables.pop()
    else:
        return binary(stack_variables, sign)


priorities = {
    "!": 5,
    "*": 4,
    "+": 3,
    "->": 2,
    "==": 1
}


def priority(sign):
    if sign in priorities:
        return priorities[sign]
    else:
        return 0
