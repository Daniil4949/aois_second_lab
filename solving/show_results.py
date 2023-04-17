from solving.solver import show_cpnf, result_cdnf, result_ccnf, show_ccnf, index


def cdnf(table, elements, exp):
    show_cpnf(table, elements, exp)
    result_cdnf(table, exp)


def ccnf(table, elements, exp):
    show_ccnf(table, elements, exp)
    result_ccnf(table, exp)


def expression(table, elements, exp):
    cdnf(table, elements, exp)
    print()
    ccnf(table, elements, exp)
    index(exp)
