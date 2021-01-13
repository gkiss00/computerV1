import sys
from cmathdir.cmath import *

class Computer:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.args = []
        self.sign = []

    def start(self):
        while(True):
            try:
                _input = self.getInput()
                if self.checkError(_input) == False:
                    print("Input error")
                else:
                    self.solve(_input)
            except KeyboardInterrupt:
                # quit
                sys.exit()

    def getInput(self):
        ret = ""
        print(">", end='')
        _input = input().strip()
        for i in range(len(_input)):
            if _input[i] != ' ':
                ret += _input[i]
        return ret

    def solve(self, _input):
        self.getEquation(_input)
        #equation = self.getEquation(_input)
        #sign = self.getSign(_input)
    
    #set the equation as 2 list of args
    def getEquation(self, _input):
        self.args.clear()
        self.sign.clear()
        i = 0

        if self.isoperand(_input[0]) == False:
            self.sign.append(1)
        while i < len(_input):
            if self.isoperand(_input[i]) == True:
                tmp = self.goodDelimiter(_input[i])
                self.sign.append(tmp)
                if tmp == 0 or tmp == 6:
                    if self.isoperand(_input[i + 1]) == False:
                        self.sign.append(1)
                i += 1
            else:
                j = i
                tmp = ""
                while (j < len(_input)) and (_input[j].isdigit() == True or _input[j].isalpha() == True or _input[j] == '.'):
                    tmp += _input[j]
                    j += 1
                self.args.append(tmp)
                i = j
        print(self.args)
        print(self.sign)

    #solve the entire equation
    def solveEquation(self):
        act = 0
        par = 0
        start = -1
        end = -1
        act_nb = self.args[act]

    #solve equation second degre
    def getSolutions(self, a, b, c):
        solutions = []
        delta = (b*b) - (4 * a * c)
        if delta == 0:
            s1 = -b / (2 * a)
            solutions.append(s1)
        elif delta > 0:
            s1 = (-b + c_sqrt(delta)) / (2 * a)
            s2 = (-b - c_sqrt(delta)) / (2 * a)
            solutions.append(s1)
            solutions.append(s2)
        return solutions

    #Error input
    def checkError(self, _input):
        if self.checkEqual(_input) == False:
            print("Symbole = must apear once and only once")
            return False
        if self.checkImplementation(_input) == False:
            print("Something goes wrong in your input")
            return False
        return True

    def checkEqual(self, _input):
        #check for the =
        equals = 0
        for i in range(len(_input)):
            if _input[i] == '=':
                equals += 1
        return equals == 1

    def checkImplementation(self, _in):
        #check bad inplementation 1 = digit || 2 = + - * / ^ % || 3 = ' '
        args = _in.split("=")
        for k in range(len(args)):
            _input = args[k]
            last = 0
            act = 0
            for i in range(len(_input)):
                if _input[i].isdigit() == True or _input[i].isalpha() == True or _input[i] == '.':
                    last = act
                    act = 1
                elif self.isoperand(_input[i]) ==  True:
                    last = act
                    act = 2
                else:
                    return False
                if last == 2 and act != 1:
                    return False
            if _input[len(_input) - 1].isdigit == False:
                return False
        return True
    
    def isoperand(self, c):
        return (c in "+-*/^=")

    def goodDelimiter(self, c):
        op = "-=+*/^"
        for i in range(len(op)):
            if c == op[i]:
                return i - 1
        return -10

computer = Computer()
computer.start()