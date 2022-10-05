import random

def setup_window(f, xmin, xmax, ymin, ymax):
    xy = f"xmin={xmin}, xmax={xmax}, ymin={ymin}, ymax={ymax},\n"
    f.write(xy)
    xytick = "xtick={" + f"{xmin}, {xmin+1},..., {xmax}" + "}, ytick={" 
    xytick += f"{ymin}, {ymin+1},...,{ymax}" + "},]\n"
    f.write(xytick)
    frame = "\\clip(" + f"{xmin-1}, {ymin-1}" + ") rectangle " 
    frame += f"({xmax+1}, {ymax+1})" + ";\n"
    f.write(frame)
    
def constant(f):
    c = random.randint(-3, 3)
    while c == 0: c = random.randint(-3, 3)
    if c > 0: 
        if c > 4: 
            xmin, xmax = -(c+1), (c+1)
        else:
            xmin, xmax = -5, 5
    else: 
        if c < -4:
            xmin, xmax = (c+1), -(c+1)
        else:
            xmin, xmax = -5, 5
    ymin, ymax = xmin, xmax
    setup_window(f, xmin, xmax, ymin, ymax)
    
    f_line = "% y = f(x)\n"
    f_line += "\\draw[line width=2pt,color=green,smooth,samples=100,"
    f_line += f"domain={xmin}:{xmax}] "
    f_line += "plot(\\x,{" + f"{c}" + "});\n"
    f.write(f_line)
    
    f_prim_line = "% y = f'(x)\n"
    f_prim_line += "\draw[line width=2pt,color=red,smooth,samples=100,"
    f_prim_line += f"domain={xmin}:{xmax}] "
    f_prim_line += "plot(\\x,{0});\n\n"
    f.write(f_prim_line)
    
    begin_script = "\\begin{scriptsize}\n"
    f.write(begin_script)
    
    f_label = "\\draw[color=green] " + f"({xmin/4}, {c+.5}" 
    f_label += ") node {$f(x) = " + f"{c}" + "$};\n"
    f.write(f_label)
    
    f_prim_label = "\\draw[color=red] " + f"({xmax/4},-.5)" + "node {$f'(x) = 0$};\n"
    f.write(f_prim_label)


def affine(f, a, b):
    xmin, xmax = -5, 5
    ymin, ymax = xmin, xmax 
    setup_window(f, xmin, xmax, ymin, ymax)
    
    f_line = "% y = f(x)\n"
    f_line += "\\draw[line width=2pt,color=green,smooth,samples=100,"
    f_line += f"domain={xmin}:{xmax}] "
    f_line += "plot(\\x,{" + f"{a}" + "(\\x) + " + f"{b}" + "});\n"
    f.write(f_line)
    
    f_prim_line = "% y = f'(x)\n"
    f_prim_line += "\draw[line width=2pt,color=red,smooth,samples=100,"
    f_prim_line += f"domain={xmin}:{xmax}] "
    f_prim_line += "plot(\\x,{" + f"{a}" + "});\n\n"
    f.write(f_prim_line)
    
    begin_script = "\\begin{scriptsize}\n"
    f.write(begin_script)
    
    f_label = "\\draw[color=green] " + f"({xmax/2}, {ymax/2}" + ") node {$f(x) = " 
    f_label += f"{a}x + {b}" + "$};\n"
    f.write(f_label)
    
    f_prim_label = "\\draw[color=red] (1.6," + f"({xmin/2},{ymin/2}" 
    f_prim_label += ") node {$f'(x) = " + f"{a}" + "$};\n"
    f.write(f_prim_label)


def puissance(f, n):
    if 5**n > 45:
        xmin, xmax = -2, 2
    else:
        xmin, xmax = -5, 5
    ymin, ymax = xmin, xmax
    setup_window(f, xmin, xmax, ymin, ymax)
    
    f_line = "% y = f(x)\n"
    f_line += "\\draw[line width=2pt,color=green,smooth,samples=100,"
    f_line += f"domain={xmin}:{xmax}] "
    f_line += "plot(\\x,{(\\x)^" + f"{n}" + "});\n"
    f.write(f_line)
    
    f_prim_line = "% y = f'(x)\n"
    f_prim_line += "\draw[line width=2pt,color=red,smooth,samples=100,"
    f_prim_line += f"domain={xmin}:{xmax}] "
    f_prim_line += "plot(\\x,{" + f"{n}" + "*(\\x)^ " + f"{n-1}" + "});\n\n"
    f.write(f_prim_line)
    
    begin_script = "\\begin{scriptsize}\n"
    f.write(begin_script)
        
    f_label = "\\draw[color=green] " + f"({xmax/2}, {ymax/2}" + ") node {$f(x) = x^" 
    f_label += f"{n}" + "$};\n"
    f.write(f_label)
    
    f_prim_label = "\\draw[color=red] " + f"({xmin/2},{ymin/2}" + ") node {$f'(x) = " 
    f_prim_label += f"{n}" + "x^" + f"{n-1}" + "$};\n"
    f.write(f_prim_label)


def create_tex_file(dict_prim_deriv):
    tex_intro_template = '''\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{amsmath, amssymb, amsfonts}
\\usepackage{pgfplots}
\\pgfplotsset{compat=1.15}
\\usepackage{mathrsfs}
\\usetikzlibrary{arrows}

\\title{Derivative Formulas}
\\author{Laurent \\textsc{Garnier}}
\\date{\\today}

\\begin{document}

\\maketitle

\\section{Basic Formulas}

'''
    primitives = list(dict_prim_deriv.keys())
    derivatives = list(dict_prim_deriv.values())
    with open("derivative.tex", 'w') as f:
        f.write(tex_intro_template)
        for i in range(len(primitives)):
            pi, di = primitives[i], derivatives[i]
            formula = f"f(x) = {pi}\\Rightarrow f'(x) = {di}"
            subsection = "\\subsection { $" + f"{formula}" + "$} \n\n"
            f.write(subsection)
            phrase = f"If $f(x) = {pi}$ then $f'(x) = {di}$.\n\n"
            f.write(phrase)
            begin_tikz = '''
\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1cm,y=1cm]
\\begin{axis}[
    x=1cm,y=1cm,
    axis lines=middle,
    ymajorgrids=true,
    xmajorgrids=true,
'''
            f.write(begin_tikz)
            if i == 0: constant(f)
            elif i == 1: affine(f, a=1, b=0)
            elif i == 2: 
                a, b = random.randint(-3, 3), random.randint(-3, 3)
                while a == 0 or a == 1: a = random.randint(-3, 3)
                affine(f, a, b)
            elif i == 3: puissance(f, n=2)
            elif i == 4: 
                n = random.randint(3, 5)
                puissance(f, n)
            elif i == 5: puissance(f, n=-1)
            elif i == 6: puissance(f, n=0.5)
            end_script = '''
\\end{scriptsize}
\\end{axis}
\\end{tikzpicture}\n\n'''
            f.write(end_script)
            
        end_tikz = "\\end{document}"
        f.write(end_tikz)
        return "Go visit: https://www.overleaf.com/"