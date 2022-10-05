def build_basic_formulas():
    primitives = ['c', 'x', 'a*x+b', 'x**2', 'x**n', '1/x', 'sqrt(x)', 'exp(x)']
    derivatives = ['0', '1', 'a', '2*x', 'n*x**(n-1)', '-1/(x**2)', '1/(2*sqrt(x))', 'exp(x)']
    dict_prim_deriv = {}
    for i in range(len(primitives)):
        pi, di = primitives[i], derivatives[i]
        dict_prim_deriv[pi] = di
    return dict_prim_deriv    

    
def watch_basic_formulas(dict_prim_deriv):
    print("Look at the basic formulas")
    for k, v in dict_prim_deriv.items():
        print(f"f(x) = {k} => f'(x) = {v}")


def watch_operation_formulas(dico_op_deriv):
    print("Look at the operations on derivatives")
    for k, v in dico_op_deriv.items():
        print(f"f(x) = {k} => f'(x) = {v}")