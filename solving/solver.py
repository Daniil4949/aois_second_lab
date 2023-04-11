def changing(n):
    truth_table = []
    first_changing = [False] * n
    truth_table.append(first_changing)
    while True:
        iteration = len(first_changing) - 1
        current_changing = truth_table[-1].copy()
        while iteration >= 0 and current_changing[iteration]:
            iteration -= 1
        if iteration < 0:
            break
        current_changing[iteration] = True
        iteration += 1
        while iteration < n:
            current_changing[iteration] = False
            iteration += 1
        truth_table.append(current_changing)
    return truth_table


def print_table(truth_table, variables, expression_result):
    for var in variables:
        print(f"{var}\t", end="")
    print("expr\tFi")
    for i in range(len(truth_table)):
        for j in range(len(truth_table[i])):
            print("1\t" if truth_table[i][j] else "0\t", end="")
        print("1\t" if expression_result[i] else "0\t", end="")
        print(i)
        print()
    print()


def solving_pdnf(truth_table, variables, result):
    suitable_options = []
    function_parts = []
    for i in range(len(result)):
        if result[i]:
            suitable_options.append(truth_table[i])
    for i in range(len(suitable_options)):
        function_part = "("
        for j in range(len(variables)):
            if suitable_options[i][j]:
                function_part += variables[j] + "*"
            else:
                function_part += "(!" + variables[j] + ")*"
        function_part = function_part[:-1] + ")"
        function_parts.append(function_part)
    return function_parts


def show_dpnf(truth_table, variables, expression_result):
    disjunction_result = ""
    parts = solving_pdnf(truth_table, variables, expression_result)
    if len(parts) != 0:
        disjunction_result += parts[0]
        for i in range(1, len(parts)):
            disjunction_result += "+" + parts[i]
        print("Principal disjunction normal function:\n" + disjunction_result + "\n")
    else:
        print("Principal disjunction normal function doesn't exist\n")


def calculating_parts_of_pcnf(truth_table, variables, expression_result):
    suitable_options = []
    function_parts = []
    for i in range(len(expression_result)):
        if not expression_result[i]:
            suitable_options.append(truth_table[i])
    for i in range(len(suitable_options)):
        function_part = "("
        for j in range(len(variables)):
            if not suitable_options[i][j]:
                function_part += variables[j] + "+"
            else:
                function_part += "(!" + variables[j] + ")+"
        function_part = function_part[:-1] + ")"
        function_parts.append(function_part)
    return function_parts


def print_pcnf(truth_table, variables, expression_result):
    disjunction = ""
    function_parts = calculating_parts_of_pcnf(truth_table, variables, expression_result)
    if len(function_parts) != 0:
        disjunction += function_parts[0]
        for i in range(1, len(function_parts)):
            disjunction += "*" + function_parts[i]
        print("Principal conjuction normal function:\n" + disjunction + "\n")
    else:
        print("Principal conjuction normal function doesn't exist\n")


def result_of_pdnf(truthTable, expressionResult):
    suitable_options = []
    results = []
    for i in range(len(expressionResult)):
        if expressionResult[i]:
            suitable_options.append(truthTable[i])
    for i in range(len(suitable_options)):
        binary_result = ""
        for j in range(len(suitable_options[i])):
            if suitable_options[i][j]:
                binary_result += "1"
            else:
                binary_result += "0"
        results.append(int(binary_result, 2))
    if len(results) != 0:
        print("PDNF numeric form:")
        result = "+(" + str(results[0])
        for i in range(1, len(results)):
            result += ", " + str(results[i])
        print(result + ")\n")


def result_of_pcnf(truth_table, result):
    suitable_options = []
    results = []
    for i in range(len(result)):
        if not result[i]:
            suitable_options.append(truth_table[i])
    for option in suitable_options:
        binary_result = ''.join(['0' if val else '1' for val in option])
        results.append(int(binary_result, 2))
    if results:
        print("PCNF numeric form:")
        result = "*(" + str(results[0])
        for i in range(1, len(results)):
            result += ", " + str(results[i])
        print(result + ")\n")


def to_int(binary_value):
    result = 0
    for i in range(len(binary_value)):
        if binary_value[len(binary_value) - i - 1] == '1':
            result += 2 ** i
    return result


def index(result):
    index = 0
    for i in range(len(result)):
        if result[i]:
            index += pow(2, len(result) - 1 - i)
    print("\nIndex Form:\ni = " + str(index))


def show_pdnf(truth_table, variables, result):
    show_dpnf(truth_table, variables, result)
    result_of_pdnf(truth_table, result)


def show_pcnf(truth_table, variables, result):
    print_pcnf(truth_table, variables, result)
    result_of_pcnf(truth_table, result)


def final_result(truth_table, variables, result):
    show_pdnf(truth_table, variables, result)
    print()
    show_pcnf(truth_table, variables, result)
    index(result)
