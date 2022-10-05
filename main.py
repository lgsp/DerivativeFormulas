import random
from tex_templates import *
from exporting_files import *
from pub import *
from formulas import *
from scores import *


def operations_on_derivatives():
    initial_form = ['k*u', 'u + v', 'u * v', 'u**n', '1/u', 'u/v', 'sqrt(u)', 'exp(u)']
    final_form = [
        "k*u'", "u' + v'", "u'v + uv'", "n*u'*u**(n-1)", 
        "-u'/(u**2)", "(u'v - uv')/(v**2)", "u'/(2*sqrt(u))", "u'*exp(u)"
    ]
    dico_op_deriv = {}
    for i in range(len(initial_form)):
        initial, final = initial_form[i], final_form[i]
        dico_op_deriv[initial] = final
    return dico_op_deriv    
    



def practice_basics(dict_prim_deriv):
    primitives = list(dict_prim_deriv.keys())
    score = 0
    attempts = 0
    cond = True
    while cond:
        attempts += 1
        p = primitives[random.randint(0, len(primitives) - 1)]
        exercice = input(f"f(x) = {p} => f'(x) = ")
        solution = dict_prim_deriv[p]
        score = incr_score(score, exercice == solution, solution)
        continuer = input("Do you want to continue? (Y|N) ")
        if continuer.upper() == "N": 
            cond = False
            final_score(attempts, score)
            review_formulas = input("Do you want to review formulas ? (Y|N) ? ")
            if review_formulas.upper() == 'Y': watch_basic_formulas(dict_prim_deriv)
            
            

def practice_operations(dico_op_deriv):
    initial_form = list(dico_op_deriv.keys())
    score = 0
    attempts = 0
    cond = True
    while cond:
        attempts += 1
        initial = initial_form[random.randint(0, len(initial_form) - 1)]
        exercice = input(f"f(x) = {initial} => f'(x) = ")
        solution = dico_op_deriv[initial]
        score = incr_score(score, exercice == solution, solution)
        continuer = input("Do you want to continue? (Y|N) ")
        if continuer.upper() == "N": 
            cond = False
            final_score(attempts, score)
            review_formulas = input("Do you want to review formulas ? (Y|N) ? ")
            if review_formulas.upper() == 'Y': watch_operation_formulas(dico_op_deriv)
            

def abcdNot0(a, b, c, d):
    while a*b*c*d == 0:
        a, b = random.randint(-10, 10), random.randint(-10, 10)
        c, d = random.randint(-10, 10), random.randint(-10, 10)
    return a, b, c, d


def build_hard_exercises():
    a, b = random.randint(-10, 10), random.randint(-10, 10)
    c, d = random.randint(-10, 10), random.randint(-10, 10)

    a, b, c, d = abcdNot0(a, b, c, d)
    
    n = random.randint(3, 20)
    mu = random.randint(-10, 10) 
    if mu == 0: sigma = 1
    else: sigma = round( abs(mu) / random.randint(5, 20), 2 )
    
    while a*d - b*c == 0:
        a, b = random.randint(-10, 10), random.randint(-10, 10)
        c, d = random.randint(-10, 10), random.randint(-10, 10)
        a, b, c, d = abcdNot0(a, b, c, d)
        
    primitives = [
        f'({a})*x + ({b})', f'({a})*x**2 + ({b})*x + ({c})',  
        f'( ({a})*x + ({b}) ) / ( ({c})*x + ({d}) )', f'sqrt( ({a})*x + ({b}) )', 
        f'exp( ({a})*x + ({b}) )', f'( ({a})*x + ({b}) )**{n}',
        f'({a})*x**3 + ({b})*x**2 + ({c})*x + ({d})', 
        f'( ( ({a})*x + ({b}) ) / ( ({c})*x + ({d}) ) )**{n}',
        f'sqrt( ( ({a})*x + ({b}) ) / ( ({c})*x + ({d}) ) )',
        'exp( - (x**2) / 2 ) / sqrt(2π)', 
        f'exp( - ( ( ( x - ({mu}) ) / {sigma} )**2 ) / 2 ) / ( {sigma}*sqrt(2π) )'
    ]
    derivatives = [
        f'{a}', f'2*({a})*x + ({b})',  
        f'{a*d-b*c} / ( ({c})*x + ({d}) )**2', f'{a} / ( 2*sqrt( ({a})*x + ({b}) )', 
        f'{a}*exp( ({a})*x + ({b}) )', f'{n}*({a})*( ({a})*x + ({b}) )**{n-1}',
        f'3*({a})*x**2 + 2*({b})*x + ({c})', 
        f'{n}*( {a*d-b*c} / ( ({c})*x + ({d}) )**2 ) * ( ({a})*x + ({b}) ) / ( ({c})*x + ({d}) )**{n-1}',
        f'( {a*d-b*c} / ( ({c})*x + ({d}) )**2 ) / ( 2 * sqrt( ( ({a})*x + ({b}) ) / ( ({c})*x + ({d}) ) )',
        '-x * exp( - (x**2) / 2 ) / sqrt(2π)', 
        f'( ( x - ({mu}) ) / {sigma} ) * exp( - ( ( ( x - ({mu}) ) / {sigma} )**2 ) / 2 ) / ( {sigma}*sqrt(2π) )'
    ]
    dict_hard_exos = {}
    for i in range(len(primitives)):
        pi, di = primitives[i], derivatives[i]
        dict_hard_exos[pi] = di
        
    return dict_hard_exos


def fake_index(prim_list, true_index):
    fake_index = random.randint(0, len(prim_list) - 1)
    if fake_index == true_index: 
        fake_index -= 1
    return fake_index


def practice_hard(dict_hard_exos):
    intro = "Now you are in HARD WORK mode so you need to take a pen and a paper.\n"
    intro += "For each question you will have 10 proposals so do not gamble!\n"
    intro += "Write down all the computation because your goal is to UNDERSTAND.\n"
    intro += "Good luck and just DO THE HARD WORK because that is the only truth!!!"
    print(intro.upper())
    input("Press ENTER to continue\n")
    primitives = list(dict_hard_exos.keys())
    score = 0
    attempts = 0
    cond = True
    while cond:
        attempts += 1
        p_index = random.randint(0, len(primitives) - 1)
        p = primitives[p_index]
        proposals = []
        solution = dict_hard_exos[p]
        proposals.append(solution)
        
        for i in range(3):
            fake_i = fake_index(prim_list=primitives, true_index=p_index)
            prim_i = primitives[fake_i]
            proposals.append(dict_hard_exos[prim_i])

        for i in range(6):
            if i % 4 == 0:
                coef = random.randint(2, 10)
                fake_ans = f"{coef} + " + solution
            elif i % 4 == 1:
                coef = random.randint(2, 10)
                pow = random.randint(2, 6)
                fake_ans = solution + f" + {coef}*x + {coef+1}*x**{pow}"
            elif i % 4 == 2:
                coef = random.randint(2, 10)
                pow = random.randint(2, 6)
                fake_ans = f"{coef}*x + {coef+1}*x**{pow} + {coef+2}*x**{pow+1}" + solution
            elif i % 4 == 3:
                coef = random.randint(3, 10)
                pow = random.randint(3, 6)
                fake_ans = solution + f" - {coef}*x + {coef+1}*x**{pow} + {coef-1}*x**{pow-1}"
            proposals.append(fake_ans)
            
        random.shuffle(proposals)
        solution_index = proposals.index(solution)
        
        print(f"f(x) = {p}\t=> f'(x) = ?\n\n")
        for i in range(10):
            print(f"Answer #{i}\t\tf'(x) = {proposals[i]}\n")

        user_response = int(input("Your response: (Just type a number between 0 and 9) "))
        print(f"Your response is: {user_response}")
        score = incr_score(score, user_response == solution_index, solution)
        continuer = input("Do you want to continue? (Y|N) ")
        if continuer.upper() == "N": 
            cond = False
            final_score(attempts, score)
            review_formulas = input("Do you want to review formulas ? (Y|N) ? ")
            if review_formulas.upper() == 'Y': watch_basic_formulas(dict_hard_exos)
            
    

basic_formulas = build_basic_formulas()
operation_formulas = operations_on_derivatives()
dict_hard_exos = build_hard_exercises()
menu = '''
0) Create Lesson files
1) Review the basic formulas
2) Practice the basic formulas
3) Review the operations on derivatives
4) Practice the operations on derivatives
5) Concrete HARD WORK
6) Do you find it too much difficult?
7) Do you want more?
8) Do you find it too easy?
9) Do you want private lessons with me?
Q) Quit
Your choice: '''
cond = True
while cond:
    choice = input(menu)
    if choice == '0':
        create_lesson_files()
    elif choice == '1':
        watch_basic_formulas(basic_formulas)
    elif choice == '2': practice_basics(basic_formulas)
    elif choice == '3': watch_operation_formulas(operation_formulas)
    elif choice == '4': practice_operations(operation_formulas)
    elif choice == '5': practice_hard(dict_hard_exos)
    elif choice == '6':
        request = "find these exercises too much difficult"
        options = [
            f"Review previous level: {pm2}", 
            f"Get more content from this level: {pm1}",
            f"Contact me on Superprof for private lessons: {annonce_superprof}"
        ]
        get_more(request, options)     
    elif choice == '7':
        request = "want more of my work"
        options = [
            f"Get more content from this level: {pm1}",
            f"Contact me on Superprof for private lessons: {annonce_superprof}",
            f"Subscribe to my YouTube channel: {pr_glump}"
        ]
        get_more(request, options)
    elif choice == '8':
        request = "want private lessons with me"
        options = [
            f"Contact me on Superprof for private lessons: {annonce_superprof}",
            f"If you are okay to pay me with bitcoins you can contact me at: {cl}",
            f"Join my affiliate program to access to Podia chat: {affiliate}"
        ]
        get_more(request, options)
    elif choice == '9':
        request = "want more of my work"
        options = [
            f"Get more content from this level: {pm1}",
            f"Contact me on Superprof for private lessons: {annonce_superprof}",
            f"Subscribe to my YouTube channel: {pr_glump}"
        ]
        get_more(request, options)
    elif choice.upper() == 'Q':
        cond = False
        request = "want to leave"
        options = [
            f"Get more content from this level: {pm1}",
            f"Contact me on Superprof for private lessons: {annonce_superprof}",
            f"Subscribe to my YouTube channel: {pr_glump}"
        ]
        get_more(request, options)
        print('Goodbye. See you soon.')
    else:
        print("ERROR!!! Please type '1' or '2' or 'Q'")
    
