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
    for element in elements:
        print(f"{element}\t", end="")
    print("expr\tFi")
    for i in range(len(tabl)):
        for j in range(len(tabl[i])):
            print("1\t" if tabl[i][j] else "0\t", end="")
        print("1\t" if values[i] else "0\t", end="")
        print(i)
        print()
    print()


def getting_result_of_cndf(tabl, elements, value):
    convinient_elements = []
    value_elements = []
    for i in range(len(value)):
        if value[i]:
            convinient_elements.append(tabl[i])
    for i in range(len(convinient_elements)):
        function_part = "("
        for j in range(len(elements)):
            if convinient_elements[i][j]:
                function_part += elements[j] + "*"
            else:
                function_part += "(!" + elements[j] + ")*"
        function_part = function_part[:-1] + ")"
        value_elements.append(function_part)
    return value_elements


def show_cpnf(tabl, elements, value):
    result = ""
    parts = getting_result_of_cndf(tabl, elements, value)
    if len(parts) != 0:
        result += parts[0]
        for i in range(1, len(parts)):
            result += "+" + parts[i]
        print("Principal disjunction normal function:\n" + result + "\n")
    else:
        print("Principal disjunction normal function doesn't exist\n")


def elements_of_ccnf(tabl, elements, value):
    convinient_elements = []
    value_elements = []
    for i in range(len(value)):
        if not value[i]:
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


def show_ccnf(tabl, elements, value):
    disjunction = ""
    function_parts = elements_of_ccnf(tabl, elements, value)
    if len(function_parts) != 0:
        disjunction += function_parts[0]
        for i in range(1, len(function_parts)):
            disjunction += "*" + function_parts[i]
        print("Principal conjuction normal function:\n" + disjunction + "\n")
    else:
        print("Principal conjuction normal function doesn't exist\n")


def result_cdnf(tabl, value):
    convinient_elements = []
    results = []
    for i in range(len(value)):
        if value[i]:
            convinient_elements.append(tabl[i])
    for i in range(len(convinient_elements)):
        binary_result = ""
        for j in range(len(convinient_elements[i])):
            if convinient_elements[i][j]:
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


def result_ccnf(tabl, value):
    convinient_elements = []
    results = []
    for i in range(len(value)):
        if not value[i]:
            convinient_elements.append(tabl[i])
    for element in convinient_elements:
        binary_result = ''.join(['0' if val else '1' for val in element])
        results.append(int(binary_result, 2))
    if results:
        print("PCNF numeric form:")
        value = "*(" + str(results[0])
        for i in range(1, len(results)):
            value += ", " + str(results[i])
        print(value + ")\n")


def to_int(element):
    value = 0
    for i in range(len(element)):
        if element[len(element) - i - 1] == '1':
            value += 2 ** i
    return value


def indexing_form(result_value):
    value = 0
    for i in range(len(result_value)):
        if result_value[i]:
            value += pow(2, len(result_value) - 1 - i)
    print("\nIndex Form:\ni = " + str(value))



