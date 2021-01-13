import sys
from cmath.cmath import *

class Computer:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def start(self):
        while(True):
            try:
                _input = self.getInput()
                self.solve(_input)
            except KeyboardInterrupt:
                # quit
                sys.exit()

    def getInput(self):
        print(">", end='')
        _input = input()
        return _input

    def solve(self, equation):
        print("sqrt ", c_sqrt(equation))

    #solve equation second degre
    def getSolutions(self, a, b, c):
        solutions = []
        delta = (b*b) - (4 * a * c)
        if delta == 0:
            s1 = -b / (2 * a)
            solutions.append(s1)
        elif delta > 0:
            s1 = (-b + pow(delta)) / (2 * a)
            s2 = (-b - pow(delta)) / (2 * a)
            solutions.append(s1)
            solutions.append(s2)
        return solutions
    
computer = Computer()
computer.start()