from typing import List, Dict
from collections import deque
from solving.logic_value import valid_logic_value, tokens_function, elements_in_logic_val
from solving.solver import changing, show_table
from solving.getting_result import getting_value
from solving.show_results import expression


def main():
    print("\nEnter expression:")
    val = input()
    elements_in_logic_val(val, unique_elements, elements_list)
    tokens_function(val, tokens, elements_list)
    elements_count: int = len(unique_elements)
    pems_count: int = 2 ** elements_count
    tabl = changing(elements_count)
    if valid_logic_value(val, tokens, unique_elements):
        for i in range(pems_count):
            for j in range(elements_count):
                vars_values[unique_elements[j]] = tabl[i][j]
            result_of_expression.append(
                getting_value(tokens, unique_elements, vars_values, signs_of_stack, stack_variables))
        show_table(tabl, unique_elements, result_of_expression)
        expression(tabl, unique_elements, result_of_expression)


vars_values: Dict[str, bool] = {}
result_of_expression: List[bool] = []
signs_of_stack = deque()
stack_variables = deque()
tokens: List[str] = []
elements_list: List[str] = []
unique_elements: List[str] = []
