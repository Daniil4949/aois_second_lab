from solving.solver import show_cpnf, result_cdnf, result_ccnf, show_ccnf, indexing_form


def cdnf(tabl, elements, exp):
    show_cpnf(tabl, elements, exp)
    result_cdnf(tabl, exp)


def ccnf(tabl, elements, exp):
    show_ccnf(tabl, elements, exp)
    result_ccnf(tabl, exp)


def expression(tabl, elements, exp):
    cdnf(tabl, elements, exp)
    print()
    ccnf(tabl, elements, exp)
    indexing_form(exp)
