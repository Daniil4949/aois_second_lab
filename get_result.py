from typing import List, Dict
from collections import deque
from solving.logic_value import valid_logic_value, tokens_function, elements_in_expression
from solving.solver import changing, show_table, final_value
from solving.getting_result import getting_result


def main():
    print("\nEnter expression:")
    logic_expression = input()
    elements_in_expression(logic_expression, unique_variables, all_variables)
    tokens_function(logic_expression, tokens_function, all_variables)
    elements_count: int = len(unique_variables)
    pems_count: int = 2 ** elements_count
    truth_table = changing(elements_count)
    if valid_logic_value(logic_expression, tokens_function, unique_variables):
        for i in range(pems_count):
            for j in range(elements_count):
                vars_values[unique_variables[j]] = truth_table[i][j]
            result_of_expression.append(
                getting_result(tokens_function, unique_variables, vars_values, signs_of_stack, stack_variables))
        show_table(truth_table, unique_variables, result_of_expression)
        final_value(truth_table, unique_variables, result_of_expression)


vars_values: Dict[str, bool] = {}
result_of_expression: List[bool] = []
signs_of_stack = deque()
stack_variables = deque()
tokens: List[str] = []
all_variables: List[str] = []
unique_variables: List[str] = []
