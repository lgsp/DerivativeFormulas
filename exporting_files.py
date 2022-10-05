tex_template = """\\documentclass[11pt]{article}
\\usepackage[utf8]{inputenc}
\\usepackage[T1]{fontenc}
\\usepackage{graphicx}
\\usepackage{grffile}
\\usepackage{longtable}
\\usepackage{wrapfig}
\\usepackage{rotating}
\\usepackage[normalem]{ulem}
\\usepackage{amsmath}
\\usepackage{textcomp}
\\usepackage{amssymb}
\\usepackage{capt-of}
\\usepackage{hyperref}
\\usepackage{amssymb}
\\author{Laurent Garnier}
\\date{\\today}
\\title{Derivatives}
\\hypersetup{
 pdfauthor={Laurent Garnier},
 pdftitle={Derivatives},
 pdfkeywords={},
 pdfsubject={},
 pdfcreator={Emacs 27.2 (Org mode 9.4)}, 
 pdflang={English}}
\\begin{document}

\\maketitle
\\tableofcontents


\\section{Source}
\\label{sec:org3c243fb}

This content is a part of \\href{https://laurentgarnier.podia.com/pratiques-mathematiques-en-1ere}{Pratiques Mathematiques} (in French)
created by Laurent Garnier.

This document (in English) has borrowed some inspiration from the
Oxford IB (International Baccalaureate) Diploma programme that you
can get on Amazon: \\url{https://amzn.to/3SamRaK}

You can get the full course here:
\\url{https://laurentgarnier.podia.com/pratiques-mathematiques-en-1ere}


\\section{Basic Formulas}
\\label{sec:org3c45c4c}
\\subsection{General definition}
\\label{sec:org72ab43d}

The derivative in mathematics is the rate at which one quantity
alters in relation to another. \\textbf{Differentiation} is the name given to
the process of determining the derivative. The calculus is a branch
of mathematics that is based on these concepts.

\\subsubsection{Example}
\\label{sec:orgbb97393}

At any time \\(t\\) seconds, \\(t > 1\\), and \\(d = -t^2 + t + 6\\), a ball
traveling toward the edge of a ping-pong table is \\(d\\) cm away from
the edge. Calculate the ball's average speed between the first and
third seconds.

Average speed = total distance \\(\\div\\) total time.

\\[\\dfrac{\\left[-(3)^2 + 3 + 6\\right]-\\left[-(1)^2+1+6\\right]}{3-1}
    = -3\\]

The speed of the ball is 3 cm\\(s^{-1}\\).

\\subsubsection{Definition 1}
\\label{sec:orgd997582}

Typically, a function's average rate between two input values, \\(x_1\\)
and \\(x_2\\), is provided by

\\[\\dfrac{\\Delta y}{\\Delta x} = \\dfrac{f(x_2)-f(x_1)}{x_2-x_1}\\]

(read as 'the change in \\(y\\) divided by the change in \\(x\\)' where
\\(\\Delta\\) is the Greek letter delta.)


\\subsubsection{Definition 2}
\\label{sec:orga7f3571}

The gradient of a curve \\[y = f(x)\\] at the point \\[(x_0, f(x_0))\\] is
\\[ \\lim_{h\\to 0}\\dfrac{f(x_0 + h) - f(x_0)}{h} \\]  provided this
limit exists.

If this limit exists the gradient of of a curve \\[y = f(x)\\] at the
point \\[(x_0, f(x_0))\\] is written \\[f'(x_0)\\]

\\subsubsection{Examples}
\\label{sec:orgf7b4a1f}
\\begin{enumerate}
\\item Example 1
\\label{sec:orgda5591e}

Find the gradient of the curve \\(y = x^2\\) at the point \\(x_0 = -2\\).

\\item Solution 1
\\label{sec:orgfc2d898}


\\begin{align*}
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{(-2+h)^2-(-2)^2}{(-2+h)-(-2)}\\\\
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{4-4h+h^2-4}{h}\\\\
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{-4h+h^2}{h}\\\\
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{h(-4+h)}{h}\\\\
\\dfrac{\\Delta y}{\\Delta x} &= -4+h
\\end{align*}


Hence \\[\\lim_{h\\to 0} (-4+h) = -4\\]



\\item Example 2
\\label{sec:orge653c89}

Find the points on the curve \\(y = \\dfrac{1}{x}\\) such that the
gradient at these points is \\(-\\dfrac{1}{9}\\).

\\item Solution 2
\\label{sec:org881f60d}

Consider the point \\(\\left(x_0, \\dfrac{1}{x_0}\\right)\\) and a
neighboring point \\(\\left(x_0 + h, \\dfrac{1}{x_0 + h}\\right)\\).



\\begin{align*}
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{\\dfrac{1}{x_0 + h}-\\dfrac{1}{x_0}}{(x_0+h)-x_0}\\\\
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{\\dfrac{x_0-(x_0+h)}{x_0(x_0+h)}}{h}\\\\
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{\\dfrac{-h}{x_0^2+x_0h}}{h}\\\\
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{-1}{x_0^2+x_0h}
\\end{align*}


Therefore:

\\[\\lim_{h\\to 0} \\dfrac{-1}{x_0^2+x_0h} = -\\dfrac{1}{x_0^2}\\]

So \\(-\\dfrac{1}{x_0^2} = -\\dfrac{1}{9}\\) hence \\(x_0 = \\pm 3\\).

The points are \\(\\left(3, \\dfrac{1}{3}\\right)\\) and \\(\\left(-3,
     -\\dfrac{1}{3}\\right)\\).
\\end{enumerate}





\\subsubsection{Exercices}
\\label{sec:orgf53ca17}

\\begin{enumerate}
\\item Find the gradient of the curve at the given value of \\(x\\).
\\begin{enumerate}
\\item \\(y = 3x^2 - 2x - 1\\) at \\(x = 5\\)
\\item \\(y = \\dfrac{3}{x}\\) at \\(x = -2\\)
\\item \\(y = x^3\\) at \\(x = 7\\)
\\end{enumerate}
\\item Find the point on the curve \\(y = \\dfrac{1}{x^2}\\), such that the
gradient at the point is 3.
\\item Find the gradient function of the curve \\(y = 2x^2 +
       \\dfrac{1}{x}\\) and then the point on the curve where the
gradient is 3.
\\end{enumerate}

\\subsubsection{Definition 3}
\\label{sec:org0c4a22d}

The \\textbf{derivative}, or \\textbf{gradient function}, of a function \\(f\\) with
respect to \\(x\\) is the function \\[f'(x) = \\lim_{h\\to
    0}\\dfrac{f(x+h)-f(x)}{h}\\], provided this limit exists.

If \\(f'\\) exists, then \\(f\\) has a derivative at \\(x\\), or is
\\textbf{differentiable} at \\(x\\). (\\(f'(x)\\) is read '\\(f\\) dash' or '\\(f\\)
prime', of \\(x\\).) Another notation for the derivative is
\\(\\dfrac{dy}{dx}\\), the derivative of the function \\(y = f(x)\\) with
respect \\(x\\).

A function is differentiable if the derivative exists for all \\(x\\)
in the domain of \\(f\\).

\\subsubsection{Examples}
\\label{sec:orgf7267b0}
\\begin{enumerate}
\\item Example 1
\\label{sec:orgb27dff6}

Find \\(f'(x)\\) given that \\(f(x) = 2x^2 + x\\), and hence find the
gradient of the function at \\(x = -3\\).

\\begin{align*}
f'(x) &= \\lim_{h\\to 0}\\dfrac{2(x+h)^2+(x+h)-(2x^2+x)}{h}\\\\
f'(x) &= \\lim_{h\\to 0}(4x+1+2h)\\\\
f'(x) &= 4x+1\\\\
f'(-3) &= -11
\\end{align*}

\\item Example 2
\\label{sec:org8d96471}

A particle moves in a straight line so that its position from its
starting point at any time \\(t\\), in seconds, is given by \\(s =
     4t^2\\), where \\(s\\) is in metres. The particle passes through a
point \\(P\\) when \\(t = a\\) and then sometime later it passes through
point \\(Q\\) when \\(t = a + h\\). Find the average velocity as the
particle travels from point \\(P\\) to point \\(Q\\), and deduce its
velocity at the instant it passes through \\(P\\).

\\(P(a, 4a^2)\\) and \\(Q(a+h, 4(a+h)^2)\\)

\\begin{align*}
\\text{Average velocity } &= \\dfrac{4(a+h)^2-4a^2}{(a+h)-a}\\\\
\\text{Average velocity } &= \\dfrac{4(a^2+2ah+h^2)-4a^2}{h}\\\\
\\text{Average velocity } &= \\dfrac{4h^2+8ah}{h}\\\\
\\text{Average velocity } &= h\\dfrac{4h+8a}{h}\\\\
\\text{Average velocity } &= 4h+8
\\end{align*}

Velocity at P = 8am\\(s^{-1}\\).
\\end{enumerate}

\\subsubsection{Exercices}
\\label{sec:org5e89ccc}

\\begin{enumerate}
\\item Find the gradient function of the given curve, and then the
value of the gradient to the curve at the given point.
\\begin{enumerate}
\\item \\(y = 4x^2 - 5x + 1\\) at \\(x = \\dfrac{3}{8}\\).
\\item \\(y = \\sqrt{x}\\) at \\(x = 4\\).
\\item \\(y = \\dfrac{2}{x}\\) at \\(x = 3\\).
\\item \\(y = \\sqrt{x - 2}\\) at \\(x = 11\\).
\\item \\(y = \\dfrac{1}{\\sqrt{x}}\\) at \\(x = 25\\).
\\end{enumerate}
\\item A particle moves in a straight line so that its position from
its starting point after \\(t\\) seconds is \\(12-5t^2\\). If the
particles passes through point \\(A\\) when \\(t = a\\), and point \\(B\\)
when \\(t = a + h\\), find
\\begin{enumerate}
\\item the average velocity of the object as it moves from \\(A\\) to
\\(B\\)
\\item the velocity as it passes through point \\(A\\).
\\end{enumerate}
\\end{enumerate}
\\end{document}"""

def create_tex_file(tex_template):
    with open("derivative.tex", 'w') as f:
        f.write(tex_template)
    print("Open the file derivative.tex")


org_template = '''
#+TITLE: Derivatives
#+AUTHOR: Laurent Garnier
#+LATEX_HEADER: \\usepackage{amssymb}

* Source

  This content is a part of [[https://laurentgarnier.podia.com/pratiques-mathematiques-en-1ere][Pratiques Mathematiques]] (in French)
  created by Laurent Garnier.

  This document (in English) has borrowed some inspiration from the
  Oxford IB (International Baccalaureate) Diploma programme that you
  can get on Amazon: [[https://amzn.to/3SamRaK]]

  You can get the full course here:
  [[https://laurentgarnier.podia.com/pratiques-mathematiques-en-1ere]]
  
  
* Basic Formulas
** General definition

   The derivative in mathematics is the rate at which one quantity
   alters in relation to another. *Differentiation* is the name given to
   the process of determining the derivative. The calculus is a branch
   of mathematics that is based on these concepts.
   
*** Example

    At any time $t$ seconds, $t > 1$, and $d = -t^2 + t + 6$, a ball
    traveling toward the edge of a ping-pong table is $d$ cm away from
    the edge. Calculate the ball's average speed between the first and
    third seconds.

    Average speed = total distance $\\div$ total time.

    \\[\\dfrac{\\left[-(3)^2 + 3 + 6\\right]-\\left[-(1)^2+1+6\\right]}{3-1}
    = -3\\]

    The speed of the ball is 3 cm$s^{-1}$.

*** Definition 1

    Typically, a function's average rate between two input values, $x_1$
    and $x_2$, is provided by

    \\[\\dfrac{\\Delta y}{\\Delta x} = \\dfrac{f(x_2)-f(x_1)}{x_2-x_1}\\]

    (read as 'the change in $y$ divided by the change in $x$' where
    $\\Delta$ is the Greek letter delta.)

    
*** Definition 2
    
   The gradient of a curve \\[y = f(x)\\] at the point \\[(x_0, f(x_0))\\] is
   \\[ \\lim_{h\\to 0}\\dfrac{f(x_0 + h) - f(x_0)}{h} \\]  provided this
   limit exists.

   If this limit exists the gradient of of a curve \\[y = f(x)\\] at the
   point \\[(x_0, f(x_0))\\] is written \\[f'(x_0)\\]

*** Examples
**** Example 1
     
     Find the gradient of the curve $y = x^2$ at the point $x_0 = -2$.

**** Solution 1


     \\begin{align*}
     \\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{(-2+h)^2-(-2)^2}{(-2+h)-(-2)}\\\\
     \\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{4-4h+h^2-4}{h}\\\\
     \\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{-4h+h^2}{h}\\\\
     \\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{h(-4+h)}{h}\\\\
     \\dfrac{\\Delta y}{\\Delta x} &= -4+h
     \\end{align*}


     Hence \\[\\lim_{h\\to 0} (-4+h) = -4\\]

     

**** Example 2

     Find the points on the curve $y = \\dfrac{1}{x}$ such that the
     gradient at these points is $-\\dfrac{1}{9}$.

**** Solution 2

     Consider the point $\\left(x_0, \\dfrac{1}{x_0}\\right)$ and a
     neighboring point $\\left(x_0 + h, \\dfrac{1}{x_0 + h}\\right)$.



     \\begin{align*}
     \\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{\\dfrac{1}{x_0 + h}-\\dfrac{1}{x_0}}{(x_0+h)-x_0}\\\\
     \\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{\\dfrac{x_0-(x_0+h)}{x_0(x_0+h)}}{h}\\\\
     \\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{\\dfrac{-h}{x_0^2+x_0h}}{h}\\\\
     \\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{-1}{x_0^2+x_0h}
     \\end{align*}


     Therefore:

     \\[\\lim_{h\\to 0} \\dfrac{-1}{x_0^2+x_0h} = -\\dfrac{1}{x_0^2}\\]

     So $-\\dfrac{1}{x_0^2} = -\\dfrac{1}{9}$ hence $x_0 = \\pm 3$.

     The points are $\\left(3, \\dfrac{1}{3}\\right)$ and $\\left(-3,
     -\\dfrac{1}{3}\\right)$.

     

     

*** Exercices

    1. Find the gradient of the curve at the given value of $x$.
       1. $y = 3x^2 - 2x - 1$ at $x = 5$
       2. $y = \\dfrac{3}{x}$ at $x = -2$
       3. $y = x^3$ at $x = 7$
    2. Find the point on the curve $y = \\dfrac{1}{x^2}$, such that the
       gradient at the point is 3.
    3. Find the gradient function of the curve $y = 2x^2 +
       \\dfrac{1}{x}$ and then the point on the curve where the
       gradient is 3.

*** Definition 3

    The *derivative*, or *gradient function*, of a function $f$ with
    respect to $x$ is the function \\[f'(x) = \\lim_{h\\to
    0}\\dfrac{f(x+h)-f(x)}{h}\\], provided this limit exists.

    If $f'$ exists, then $f$ has a derivative at $x$, or is
    *differentiable* at $x$. ($f'(x)$ is read '$f$ dash' or '$f$
    prime', of $x$.) Another notation for the derivative is
    $\\dfrac{dy}{dx}$, the derivative of the function $y = f(x)$ with
    respect $x$.

    A function is differentiable if the derivative exists for all $x$
    in the domain of $f$.

*** Examples
**** Example 1
     
    Find $f'(x)$ given that $f(x) = 2x^2 + x$, and hence find the
    gradient of the function at $x = -3$.

    \\begin{align*}
    f'(x) &= \\lim_{h\\to 0}\\dfrac{2(x+h)^2+(x+h)-(2x^2+x)}{h}\\\\
    f'(x) &= \\lim_{h\\to 0}(4x+1+2h)\\\\
    f'(x) &= 4x+1\\\\
    f'(-3) &= -11
    \\end{align*}
    
**** Example 2

     A particle moves in a straight line so that its position from its
     starting point at any time $t$, in seconds, is given by $s =
     4t^2$, where $s$ is in metres. The particle passes through a
     point $P$ when $t = a$ and then sometime later it passes through
     point $Q$ when $t = a + h$. Find the average velocity as the
     particle travels from point $P$ to point $Q$, and deduce its
     velocity at the instant it passes through $P$.

     $P(a, 4a^2)$ and $Q(a+h, 4(a+h)^2)$

     \\begin{align*}
     \\text{Average velocity } &= \\dfrac{4(a+h)^2-4a^2}{(a+h)-a}\\\\
     \\text{Average velocity } &= \\dfrac{4(a^2+2ah+h^2)-4a^2}{h}\\\\
     \\text{Average velocity } &= \\dfrac{4h^2+8ah}{h}\\\\
     \\text{Average velocity } &= h\\dfrac{4h+8a}{h}\\\\
     \\text{Average velocity } &= 4h+8
     \\end{align*}

     Velocity at P = 8am$s^{-1}$.
     
*** Exercices

    1. Find the gradient function of the given curve, and then the
       value of the gradient to the curve at the given point.
       1. $y = 4x^2 - 5x + 1$ at $x = \\dfrac{3}{8}$.
       2. $y = \\sqrt{x}$ at $x = 4$.
       3. $y = \\dfrac{2}{x}$ at $x = 3$.
       4. $y = \\sqrt{x - 2}$ at $x = 11$.
       5. $y = \\dfrac{1}{\\sqrt{x}}$ at $x = 25$.
    2. A particle moves in a straight line so that its position from
       its starting point after $t$ seconds is $12-5t^2$. If the
       particles passes through point $A$ when $t = a$, and point $B$
       when $t = a + h$, find
       1. the average velocity of the object as it moves from $A$ to
          $B$
       2. the velocity as it passes through point $A$.

'''

def create_org_file(org_template):
    with open("derivative.org", 'w') as f:
        f.write(org_template)
    print("Open the file derivative.org")


html_template = '''
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
<!-- 2022-09-17 Sat 17:28 -->
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Derivatives</title>
<meta name="generator" content="Org mode" />
<meta name="author" content="Laurent Garnier" />
<style type="text/css">
 <!--/*--><![CDATA[/*><!--*/
  .title  { text-align: center;
             margin-bottom: .2em; }
  .subtitle { text-align: center;
              font-size: medium;
              font-weight: bold;
              margin-top:0; }
  .todo   { font-family: monospace; color: red; }
  .done   { font-family: monospace; color: green; }
  .priority { font-family: monospace; color: orange; }
  .tag    { background-color: #eee; font-family: monospace;
            padding: 2px; font-size: 80%; font-weight: normal; }
  .timestamp { color: #bebebe; }
  .timestamp-kwd { color: #5f9ea0; }
  .org-right  { margin-left: auto; margin-right: 0px;  text-align: right; }
  .org-left   { margin-left: 0px;  margin-right: auto; text-align: left; }
  .org-center { margin-left: auto; margin-right: auto; text-align: center; }
  .underline { text-decoration: underline; }
  #postamble p, #preamble p { font-size: 90%; margin: .2em; }
  p.verse { margin-left: 3%; }
  pre {
    border: 1px solid #ccc;
    box-shadow: 3px 3px 3px #eee;
    padding: 8pt;
    font-family: monospace;
    overflow: auto;
    margin: 1.2em;
  }
  pre.src {
    position: relative;
    overflow: auto;
    padding-top: 1.2em;
  }
  pre.src:before {
    display: none;
    position: absolute;
    background-color: white;
    top: -10px;
    right: 10px;
    padding: 3px;
    border: 1px solid black;
  }
  pre.src:hover:before { display: inline;}
  /* Languages per Org manual */
  pre.src-asymptote:before { content: 'Asymptote'; }
  pre.src-awk:before { content: 'Awk'; }
  pre.src-C:before { content: 'C'; }
  /* pre.src-C++ doesn't work in CSS */
  pre.src-clojure:before { content: 'Clojure'; }
  pre.src-css:before { content: 'CSS'; }
  pre.src-D:before { content: 'D'; }
  pre.src-ditaa:before { content: 'ditaa'; }
  pre.src-dot:before { content: 'Graphviz'; }
  pre.src-calc:before { content: 'Emacs Calc'; }
  pre.src-emacs-lisp:before { content: 'Emacs Lisp'; }
  pre.src-fortran:before { content: 'Fortran'; }
  pre.src-gnuplot:before { content: 'gnuplot'; }
  pre.src-haskell:before { content: 'Haskell'; }
  pre.src-hledger:before { content: 'hledger'; }
  pre.src-java:before { content: 'Java'; }
  pre.src-js:before { content: 'Javascript'; }
  pre.src-latex:before { content: 'LaTeX'; }
  pre.src-ledger:before { content: 'Ledger'; }
  pre.src-lisp:before { content: 'Lisp'; }
  pre.src-lilypond:before { content: 'Lilypond'; }
  pre.src-lua:before { content: 'Lua'; }
  pre.src-matlab:before { content: 'MATLAB'; }
  pre.src-mscgen:before { content: 'Mscgen'; }
  pre.src-ocaml:before { content: 'Objective Caml'; }
  pre.src-octave:before { content: 'Octave'; }
  pre.src-org:before { content: 'Org mode'; }
  pre.src-oz:before { content: 'OZ'; }
  pre.src-plantuml:before { content: 'Plantuml'; }
  pre.src-processing:before { content: 'Processing.js'; }
  pre.src-python:before { content: 'Python'; }
  pre.src-R:before { content: 'R'; }
  pre.src-ruby:before { content: 'Ruby'; }
  pre.src-sass:before { content: 'Sass'; }
  pre.src-scheme:before { content: 'Scheme'; }
  pre.src-screen:before { content: 'Gnu Screen'; }
  pre.src-sed:before { content: 'Sed'; }
  pre.src-sh:before { content: 'shell'; }
  pre.src-sql:before { content: 'SQL'; }
  pre.src-sqlite:before { content: 'SQLite'; }
  /* additional languages in org.el's org-babel-load-languages alist */
  pre.src-forth:before { content: 'Forth'; }
  pre.src-io:before { content: 'IO'; }
  pre.src-J:before { content: 'J'; }
  pre.src-makefile:before { content: 'Makefile'; }
  pre.src-maxima:before { content: 'Maxima'; }
  pre.src-perl:before { content: 'Perl'; }
  pre.src-picolisp:before { content: 'Pico Lisp'; }
  pre.src-scala:before { content: 'Scala'; }
  pre.src-shell:before { content: 'Shell Script'; }
  pre.src-ebnf2ps:before { content: 'ebfn2ps'; }
  /* additional language identifiers per "defun org-babel-execute"
       in ob-*.el */
  pre.src-cpp:before  { content: 'C++'; }
  pre.src-abc:before  { content: 'ABC'; }
  pre.src-coq:before  { content: 'Coq'; }
  pre.src-groovy:before  { content: 'Groovy'; }
  /* additional language identifiers from org-babel-shell-names in
     ob-shell.el: ob-shell is the only babel language using a lambda to put
     the execution function name together. */
  pre.src-bash:before  { content: 'bash'; }
  pre.src-csh:before  { content: 'csh'; }
  pre.src-ash:before  { content: 'ash'; }
  pre.src-dash:before  { content: 'dash'; }
  pre.src-ksh:before  { content: 'ksh'; }
  pre.src-mksh:before  { content: 'mksh'; }
  pre.src-posh:before  { content: 'posh'; }
  /* Additional Emacs modes also supported by the LaTeX listings package */
  pre.src-ada:before { content: 'Ada'; }
  pre.src-asm:before { content: 'Assembler'; }
  pre.src-caml:before { content: 'Caml'; }
  pre.src-delphi:before { content: 'Delphi'; }
  pre.src-html:before { content: 'HTML'; }
  pre.src-idl:before { content: 'IDL'; }
  pre.src-mercury:before { content: 'Mercury'; }
  pre.src-metapost:before { content: 'MetaPost'; }
  pre.src-modula-2:before { content: 'Modula-2'; }
  pre.src-pascal:before { content: 'Pascal'; }
  pre.src-ps:before { content: 'PostScript'; }
  pre.src-prolog:before { content: 'Prolog'; }
  pre.src-simula:before { content: 'Simula'; }
  pre.src-tcl:before { content: 'tcl'; }
  pre.src-tex:before { content: 'TeX'; }
  pre.src-plain-tex:before { content: 'Plain TeX'; }
  pre.src-verilog:before { content: 'Verilog'; }
  pre.src-vhdl:before { content: 'VHDL'; }
  pre.src-xml:before { content: 'XML'; }
  pre.src-nxml:before { content: 'XML'; }
  /* add a generic configuration mode; LaTeX export needs an additional
     (add-to-list 'org-latex-listings-langs '(conf " ")) in .emacs */
  pre.src-conf:before { content: 'Configuration File'; }

  table { border-collapse:collapse; }
  caption.t-above { caption-side: top; }
  caption.t-bottom { caption-side: bottom; }
  td, th { vertical-align:top;  }
  th.org-right  { text-align: center;  }
  th.org-left   { text-align: center;   }
  th.org-center { text-align: center; }
  td.org-right  { text-align: right;  }
  td.org-left   { text-align: left;   }
  td.org-center { text-align: center; }
  dt { font-weight: bold; }
  .footpara { display: inline; }
  .footdef  { margin-bottom: 1em; }
  .figure { padding: 1em; }
  .figure p { text-align: center; }
  .equation-container {
    display: table;
    text-align: center;
    width: 100%;
  }
  .equation {
    vertical-align: middle;
  }
  .equation-label {
    display: table-cell;
    text-align: right;
    vertical-align: middle;
  }
  .inlinetask {
    padding: 10px;
    border: 2px solid gray;
    margin: 10px;
    background: #ffffcc;
  }
  #org-div-home-and-up
   { text-align: right; font-size: 70%; white-space: nowrap; }
  textarea { overflow-x: auto; }
  .linenr { font-size: smaller }
  .code-highlighted { background-color: #ffff00; }
  .org-info-js_info-navigation { border-style: none; }
  #org-info-js_console-label
    { font-size: 10px; font-weight: bold; white-space: nowrap; }
  .org-info-js_search-highlight
    { background-color: #ffff00; color: #000000; font-weight: bold; }
  .org-svg { width: 90%; }
  /*]]>*/-->
</style>
<script type="text/javascript">
// @license magnet:?xt=urn:btih:e95b018ef3580986a04669f1b5879592219e2a7a&dn=public-domain.txt Public Domain
<!--/*--><![CDATA[/*><!--*/
     function CodeHighlightOn(elem, id)
     {
       var target = document.getElementById(id);
       if(null != target) {
         elem.classList.add("code-highlighted");
         target.classList.add("code-highlighted");
       }
     }
     function CodeHighlightOff(elem, id)
     {
       var target = document.getElementById(id);
       if(null != target) {
         elem.classList.remove("code-highlighted");
         target.classList.remove("code-highlighted");
       }
     }
    /*]]>*///-->
// @license-end
</script>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        displayAlign: "center",
        displayIndent: "0em",

        "HTML-CSS": { scale: 100,
                        linebreaks: { automatic: "false" },
                        webFont: "TeX"
                       },
        SVG: {scale: 100,
              linebreaks: { automatic: "false" },
              font: "TeX"},
        NativeMML: {scale: 100},
        TeX: { equationNumbers: {autoNumber: "AMS"},
               MultLineWidth: "85%",
               TagSide: "right",
               TagIndent: ".8em"
             }
});
</script>
<script type="text/javascript"
        src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_HTML"></script>
</head>
<body>
<div id="content">
<h1 class="title">Derivatives</h1>
<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgb718685">1. Source</a></li>
<li><a href="#org0d55b32">2. Basic Formulas</a>
<ul>
<li><a href="#orgb7bb2de">2.1. General definition</a>
<ul>
<li><a href="#orge7d3e3f">2.1.1. Example</a></li>
<li><a href="#org0de68b3">2.1.2. Definition 1</a></li>
<li><a href="#org42cace2">2.1.3. Definition 2</a></li>
<li><a href="#orgfcc5b0e">2.1.4. Examples</a></li>
<li><a href="#org911e064">2.1.5. Exercices</a></li>
<li><a href="#org77bc97c">2.1.6. Definition 3</a></li>
<li><a href="#orgad58148">2.1.7. Examples</a></li>
<li><a href="#org0ce79e1">2.1.8. Exercices</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

<div id="outline-container-orgb718685" class="outline-2">
<h2 id="orgb718685"><span class="section-number-2">1</span> Source</h2>
<div class="outline-text-2" id="text-1">
<p>
This content is a part of <a href="https://laurentgarnier.podia.com/pratiques-mathematiques-en-1ere">Pratiques Mathematiques</a> (in French)
created by Laurent Garnier.
</p>

<p>
This document (in English) has borrowed some inspiration from the
Oxford IB (International Baccalaureate) Diploma programme that you
can get on Amazon: <a href="https://amzn.to/3SamRaK">https://amzn.to/3SamRaK</a>
</p>

<iframe sandbox="allow-popups allow-scripts allow-modals allow-forms allow-same-origin" style="width:120px;height:240px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="//ws-eu.amazon-adsystem.com/widgets/q?ServiceVersion=20070822&OneJS=1&Operation=GetAdHtml&MarketPlace=FR&source=ss&ref=as_ss_li_til&ad_type=product_link&tracking_id=wwwbecomefree-21&language=fr_FR&marketplace=amazon&region=FR&placement=0198390122&asins=0198390122&linkId=f4c41ba8d562cad8f3241d3ec08fd520&show_border=true&link_opens_in_new_window=true"></iframe>


<p>
You can get the full course here:
<a href="https://laurentgarnier.podia.com/pratiques-mathematiques-en-1ere">https://laurentgarnier.podia.com/pratiques-mathematiques-en-1ere</a>
</p>
</div>
</div>


<div id="outline-container-org0d55b32" class="outline-2">
<h2 id="org0d55b32"><span class="section-number-2">2</span> Basic Formulas</h2>
<div class="outline-text-2" id="text-2">
</div>
<div id="outline-container-orgb7bb2de" class="outline-3">
<h3 id="orgb7bb2de"><span class="section-number-3">2.1</span> General definition</h3>
<div class="outline-text-3" id="text-2-1">
<p>
The derivative in mathematics is the rate at which one quantity
alters in relation to another. <b>Differentiation</b> is the name given to
the process of determining the derivative. The calculus is a branch
of mathematics that is based on these concepts.
</p>
</div>

<div id="outline-container-orge7d3e3f" class="outline-4">
<h4 id="orge7d3e3f"><span class="section-number-4">2.1.1</span> Example</h4>
<div class="outline-text-4" id="text-2-1-1">
<p>
At any time \\(t\\) seconds, \\(t > 1\\), and \\(d = -t^2 + t + 6\\), a ball
traveling toward the edge of a ping-pong table is \\(d\\) cm away from
the edge. Calculate the ball's average speed between the first and
third seconds.
</p>

<p>
Average speed = total distance \\(\\div\\) total time.
</p>

<p>
\\[\\dfrac{\\left[-(3)^2 + 3 + 6\\right]-\\left[-(1)^2+1+6\\right]}{3-1}
    = -3\\]
</p>

<p>
The speed of the ball is 3 cm\\(s^{-1}\\).
</p>
</div>
</div>

<div id="outline-container-org0de68b3" class="outline-4">
<h4 id="org0de68b3"><span class="section-number-4">2.1.2</span> Definition 1</h4>
<div class="outline-text-4" id="text-2-1-2">
<p>
Typically, a function's average rate between two input values, \\(x_1\\)
and \\(x_2\\), is provided by
</p>

<p>
\\[\\dfrac{\\Delta y}{\\Delta x} = \\dfrac{f(x_2)-f(x_1)}{x_2-x_1}\\]
</p>

<p>
(read as 'the change in \\(y\\) divided by the change in \\(x\\)' where
\\(\\Delta\\) is the Greek letter delta.)
</p>
</div>
</div>


<div id="outline-container-org42cace2" class="outline-4">
<h4 id="org42cace2"><span class="section-number-4">2.1.3</span> Definition 2</h4>
<div class="outline-text-4" id="text-2-1-3">
<p>
The gradient of a curve \\[y = f(x)\\] at the point \\[(x_0, f(x_0))\\] is
\\[ \\lim_{h\\to 0}\\dfrac{f(x_0 + h) - f(x_0)}{h} \\]  provided this
limit exists.
</p>

<p>
If this limit exists the gradient of of a curve \\[y = f(x)\\] at the
point \\[(x_0, f(x_0))\\] is written \\[f'(x_0)\\]
</p>
</div>
</div>

<div id="outline-container-orgfcc5b0e" class="outline-4">
<h4 id="orgfcc5b0e"><span class="section-number-4">2.1.4</span> Examples</h4>
<div class="outline-text-4" id="text-2-1-4">
</div>
<ol class="org-ol">
<li><a id="orgbebea67"></a>Example 1<br />
<div class="outline-text-5" id="text-2-1-4-1">
<p>
Find the gradient of the curve \\(y = x^2\\) at the point \\(x_0 = -2\\).
</p>
</div>
</li>

<li><a id="org4b734eb"></a>Solution 1<br />
<div class="outline-text-5" id="text-2-1-4-2">
\\begin{align*}
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{(-2+h)^2-(-2)^2}{(-2+h)-(-2)}\\\\
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{4-4h+h^2-4}{h}\\\\
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{-4h+h^2}{h}\\\\
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{h(-4+h)}{h}\\\\
\\dfrac{\\Delta y}{\\Delta x} &= -4+h
\\end{align*}


<p>
Hence \\[\\lim_{h\\to 0} (-4+h) = -4\\]
</p>
</div>
</li>



<li><a id="org6dbe1eb"></a>Example 2<br />
<div class="outline-text-5" id="text-2-1-4-3">
<p>
Find the points on the curve \\(y = \\dfrac{1}{x}\\) such that the
gradient at these points is \\(-\\dfrac{1}{9}\\).
</p>
</div>
</li>

<li><a id="org5431e75"></a>Solution 2<br />
<div class="outline-text-5" id="text-2-1-4-4">
<p>
Consider the point \\(\\left(x_0, \\dfrac{1}{x_0}\\right)\\) and a
neighboring point \\(\\left(x_0 + h, \\dfrac{1}{x_0 + h}\\right)\\).
</p>



\\begin{align*}
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{\\dfrac{1}{x_0 + h}-\\dfrac{1}{x_0}}{(x_0+h)-x_0}\\\\
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{\\dfrac{x_0-(x_0+h)}{x_0(x_0+h)}}{h}\\\\
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{\\dfrac{-h}{x_0^2+x_0h}}{h}\\\\
\\dfrac{\\Delta y}{\\Delta x} &= \\dfrac{-1}{x_0^2+x_0h}
\\end{align*}


<p>
Therefore:
</p>

<p>
\\[\\lim_{h\\to 0} \\dfrac{-1}{x_0^2+x_0h} = -\\dfrac{1}{x_0^2}\\]
</p>

<p>
So \\(-\\dfrac{1}{x_0^2} = -\\dfrac{1}{9}\\) hence \\(x_0 = \\pm 3\\).
</p>

<p>
The points are \\(\\left(3, \\dfrac{1}{3}\\right)\\) and \\(\\left(-3,
     -\\dfrac{1}{3}\\right)\\).
</p>
</div>
</li>
</ol>
</div>





<div id="outline-container-org911e064" class="outline-4">
<h4 id="org911e064"><span class="section-number-4">2.1.5</span> Exercices</h4>
<div class="outline-text-4" id="text-2-1-5">
<ol class="org-ol">
<li>Find the gradient of the curve at the given value of \\(x\\).
<ol class="org-ol">
<li>\\(y = 3x^2 - 2x - 1\\) at \\(x = 5\\)</li>
<li>\\(y = \\dfrac{3}{x}\\) at \\(x = -2\\)</li>
<li>\\(y = x^3\\) at \\(x = 7\\)</li>
</ol></li>
<li>Find the point on the curve \\(y = \\dfrac{1}{x^2}\\), such that the
gradient at the point is 3.</li>
<li>Find the gradient function of the curve \\(y = 2x^2 +
       \\dfrac{1}{x}\\) and then the point on the curve where the
gradient is 3.</li>
</ol>
</div>
</div>

<div id="outline-container-org77bc97c" class="outline-4">
<h4 id="org77bc97c"><span class="section-number-4">2.1.6</span> Definition 3</h4>
<div class="outline-text-4" id="text-2-1-6">
<p>
The <b>derivative</b>, or <b>gradient function</b>, of a function \\(f\\) with
respect to \\(x\\) is the function \\[f'(x) = \\lim_{h\\to
    0}\\dfrac{f(x+h)-f(x)}{h}\\], provided this limit exists.
</p>

<p>
If \\(f'\\) exists, then \\(f\\) has a derivative at \\(x\\), or is
<b>differentiable</b> at \\(x\\). (\\(f'(x)\\) is read '\\(f\\) dash' or '\\(f\\)
prime', of \\(x\\).) Another notation for the derivative is
\\(\\dfrac{dy}{dx}\\), the derivative of the function \\(y = f(x)\\) with
respect \\(x\\).
</p>

<p>
A function is differentiable if the derivative exists for all \\(x\\)
in the domain of \\(f\\).
</p>
</div>
</div>

<div id="outline-container-orgad58148" class="outline-4">
<h4 id="orgad58148"><span class="section-number-4">2.1.7</span> Examples</h4>
<div class="outline-text-4" id="text-2-1-7">
</div>
<ol class="org-ol">
<li><a id="org8d6e3f3"></a>Example 1<br />
<div class="outline-text-5" id="text-2-1-7-1">
<p>
Find \\(f'(x)\\) given that \\(f(x) = 2x^2 + x\\), and hence find the
gradient of the function at \\(x = -3\\).
</p>

\\begin{align*}
f'(x) &= \\lim_{h\\to 0}\\dfrac{2(x+h)^2+(x+h)-(2x^2+x)}{h}\\\\
f'(x) &= \\lim_{h\\to 0}(4x+1+2h)\\\\
f'(x) &= 4x+1\\\\
f'(-3) &= -11
\\end{align*}
</div>
</li>

<li><a id="orgf901888"></a>Example 2<br />
<div class="outline-text-5" id="text-2-1-7-2">
<p>
A particle moves in a straight line so that its position from its
starting point at any time \\(t\\), in seconds, is given by \\(s =
     4t^2\\), where \\(s\\) is in metres. The particle passes through a
point \\(P\\) when \\(t = a\\) and then sometime later it passes through
point \\(Q\\) when \\(t = a + h\\). Find the average velocity as the
particle travels from point \\(P\\) to point \\(Q\\), and deduce its
velocity at the instant it passes through \\(P\\).
</p>

<p>
\\(P(a, 4a^2)\\) and \\(Q(a+h, 4(a+h)^2)\\)
</p>

\\begin{align*}
\\text{Average velocity } &= \\dfrac{4(a+h)^2-4a^2}{(a+h)-a}\\\\
\\text{Average velocity } &= \\dfrac{4(a^2+2ah+h^2)-4a^2}{h}\\\\
\\text{Average velocity } &= \\dfrac{4h^2+8ah}{h}\\\\
\\text{Average velocity } &= h\\dfrac{4h+8a}{h}\\\\
\\text{Average velocity } &= 4h+8
\\end{align*}

<p>
Velocity at P = 8am\\(s^{-1}\\).
</p>
</div>
</li>
</ol>
</div>

<div id="outline-container-org0ce79e1" class="outline-4">
<h4 id="org0ce79e1"><span class="section-number-4">2.1.8</span> Exercices</h4>
<div class="outline-text-4" id="text-2-1-8">
<ol class="org-ol">
<li>Find the gradient function of the given curve, and then the
value of the gradient to the curve at the given point.
<ol class="org-ol">
<li>\\(y = 4x^2 - 5x + 1\\) at \\(x = \\dfrac{3}{8}\\).</li>
<li>\\(y = \\sqrt{x}\\) at \\(x = 4\\).</li>
<li>\\(y = \\dfrac{2}{x}\\) at \\(x = 3\\).</li>
<li>\\(y = \\sqrt{x - 2}\\) at \\(x = 11\\).</li>
<li>\\(y = \\dfrac{1}{\\sqrt{x}}\\) at \\(x = 25\\).</li>
</ol></li>
<li>A particle moves in a straight line so that its position from
its starting point after \\(t\\) seconds is \\(12-5t^2\\). If the
particles passes through point \\(A\\) when \\(t = a\\), and point \\(B\\)
when \\(t = a + h\\), find
<ol class="org-ol">
<li>the average velocity of the object as it moves from \\(A\\) to
\\(B\\)</li>
<li>the velocity as it passes through point \\(A\\).</li>
</ol></li>
</ol>
</div>
</div>
</div>
</div>
</div>
<div id="postamble" class="status">
<p class="author">Author: Laurent Garnier</p>
<p class="date">Created: 2022-09</p>
<p class="validation"><a href="https://validator.w3.org/check?uri=referer">Validate</a></p>
</div>
</body>
</html>

'''

def create_html_file(html_template):
    with open("derivative.html", 'w') as f:
        f.write(html_template)
    print("Open derivative.html")



def create_lesson_files():
    menu = '''
    1) Generate a HTML file
    2) Generate an Org file
    3) Generate a TeX file
    Q) Quit
    Your choice: '''
    cond = True
    while cond:
        choice = input(menu)
        if choice == '1': 
            create_html_file(html_template)
        elif choice == '2':
            create_org_file(org_template)
        elif choice == '3':
            create_tex_file(tex_template)
        elif choice == 'Q':
            cond = False
        else:
            print("ERROR!!! Select 1 option from the menu")
