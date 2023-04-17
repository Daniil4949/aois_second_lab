def changing(n):
    tabl = []
    moving = [False] * n
    tabl.append(moving)
    while True:
        move = len(moving) - 1
        cur_move = tabl[-1].copy()
        while move >= 0 and cur_move[move]:
            move -= 1
        if move < 0:
            break
        cur_move[move] = True
        move += 1
        while move < n:
            cur_move[move] = False
            move += 1
        tabl.append(cur_move)
    return tabl


def show_table(tabl, elements, values):
    for var in elements:
        print(f"{var}\t", end="")
    print("expr\tFi")
    for i in range(len(tabl)):
        for j in range(len(tabl[i])):
            print("1\t" if tabl[i][j] else "0\t", end="")
        print("1\t" if values[i] else "0\t", end="")
        print(i)
        print()
    print()


def getting_result_of_cndf(truth_table, variables, result):
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


def show_cpnf(truth_table, variables, expression_result):
    disjunction_result = ""
    parts = getting_result_of_cndf(truth_table, variables, expression_result)
    if len(parts) != 0:
        disjunction_result += parts[0]
        for i in range(1, len(parts)):
            disjunction_result += "+" + parts[i]
        print("Principal disjunction normal function:\n" + disjunction_result + "\n")
    else:
        print("Principal disjunction normal function doesn't exist\n")


def elements_of_ccnf(tabl, elements, expression_result):
    convinient_elements = []
    value_elements = []
    for i in range(len(expression_result)):
        if not expression_result[i]:
            convinient_elements.append(tabl[i])
    for i in range(len(convinient_elements)):
        function_part = "("
        for j in range(len(elements)):
            if not convinient_elements[i][j]:
                function_part += elements[j] + "+"
            else:
                function_part += "(!" + elements[j] + ")+"
        function_part = function_part[:-1] + ")"
        value_elements.append(function_part)
    return value_elements


def show_ccnf(table, elements, expression_result):
    disjunction = ""
    function_parts = elements_of_ccnf(table, elements, expression_result)
    if len(function_parts) != 0:
        disjunction += function_parts[0]
        for i in range(1, len(function_parts)):
            disjunction += "*" + function_parts[i]
        print("Principal conjuction normal function:\n" + disjunction + "\n")
    else:
        print("Principal conjuction normal function doesn't exist\n")


def result_cdnf(table, value):
    suitable_options = []
    results = []
    for i in range(len(value)):
        if value[i]:
            suitable_options.append(table[i])
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


def result_ccnf(truth_table, result):
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
    value = 0
    for i in range(len(result)):
        if result[i]:
            value += pow(2, len(result) - 1 - i)
    print("\nIndex Form:\ni = " + str(value))


def cdnf(truth_table, variables, result):
    show_cpnf(truth_table, variables, result)
    result_cdnf(truth_table, result)


def ccnf(truth_table, variables, result):
    show_ccnf(truth_table, variables, result)
    result_ccnf(truth_table, result)


def final_value(truth_table, variables, result):
    cdnf(truth_table, variables, result)
    print()
    ccnf(truth_table, variables, result)
    index(result)
