from typing import List, Dict
from collections import deque
from solving.expression import correct_expression, tokenizing, counting_variables_of_expression
from solving.solver import changing

def main():
    while True:
        vars_values: Dict[str, bool] = {}
        result_of_expression: List[bool] = []
        signs_of_stack = deque()
        stack_variables = deque()
        tokens: List[str] = []
        all_variables: List[str] = []
        unique_variables: List[str] = []
        print("\nEnter expression:")
        logic_expression = input()
        counting_variables_of_expression(logic_expression, unique_variables, all_variables)
        tokenizing(logic_expression, tokens, all_variables)
        number_of_variables: int = len(unique_variables)
        number_of_permutations: int = 2 ** number_of_variables
        truth_table = Solver.changing(number_of_variables)
        if Expression.correct_expression(logic_expression, tokens, unique_variables):
            for i in range(number_of_permutations):
                for j in range(number_of_variables):
                    vars_values[unique_variables[j]] = truth_table[i][j]
                result_of_expression.append(
                    LogicCalculator.getting_result(tokens, unique_variables, vars_values, signs_of_stack, stack_variables))
            Solver.print_table(truth_table, unique_variables, result_of_expression)
            Solver.final_result(truth_table, unique_variables, result_of_expression)


if __name__ == "__main__":
    main()
