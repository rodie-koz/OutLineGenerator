from sympy import symbols
from sympy.plotting import plot
x = symbols('X')
p1 = plot(x+1, show=False , title="Milan's Graph")

p1.show()
