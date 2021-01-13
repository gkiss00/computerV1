def c_sum(a, b):
    return (a + b)

def c_sub(a, b):
    return (a - b)

def c_mult(a, b):
    return (a * b)
    
def c_div(a, b):
    return (a * b)

#get the rest of the divion
def c_mod(a, b):
    tmp = int(a / b)
    return (a - (b * tmp))

#get abs value of a number
def c_abs(nb):
    if nb < 0:
        nb = nb * -1
    return nb

#get the power of a number
#work with integer only
def c_pow(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result

#get the root square of a number
#work with integer only and perfect square
def c_sqrt(nb):
    final_result = 0.0
    ratio = 1
    div = 10
    rest = 0.0
    pair_list = getList(nb)
    point = getPointPlace(nb)

    #imaginary number
    if int(float(nb)) < 0:
        return final_result
    
    for i in range(len(pair_list)):
        #get actual number
        pair_list[i] = (rest * 100) + pair_list[i]
        #n : number of the bigger square found
        n = findBiggerSquare(pair_list[i], ratio)
        #rest : rest of the divison
        rest = pair_list[i] - c_pow(n, 2)
        #if we are in int
        if (i < point):
            _range = getNumberRange(n) * 10
            final_result = (final_result * _range) + n
            ratio = final_result * 2
            #if we are in float
        else:
            final_result = final_result + (n / div)
            ratio = (final_result * div) * 2
            div *= div * 100
    return final_result

#utils
def getList(nb):
    pair_list = []
    res = float(nb) - int(float(nb))
    #for the part before the comma
    while int(float(nb)) != 0:
        tmp = int(float(nb)) % 100
        pair_list.append(tmp)
        nb = int(float(nb)) / 100
    reverse_list(pair_list)
    #for the part before the comma
    for i in range(3):
        res *= 100
        pair_list.append(int(float(res)))
        res = res - int(float(res))
    print(pair_list)
    return pair_list
#utils
def reverse_list(liste):
    for i in range(int(len(liste) / 2)):
        tmp = liste[i]
        liste[i] = liste[len(liste) - 1 - i]
        liste[len(liste) - 1 - i] = tmp
            
#get number range 1, 10, 100, 1000, ...
def getNumberRange(nb):
    _range = 1
    while int(float(nb)) > 9:
        _range *= 10
        nb /= 10
    return _range

#get number size 8 -> 1, 45 -> 2, 783 -> 3, ...
def getNumberSize(nb):
    size = 0
    if nb == 0:
        return 1
    while int(float(nb)) != 0:
        size += 1
        nb = int(float(nb)) / 10
    return size

#get place of point 4.5 -> 1, 47.5 -> 1, 478.9 -> 2, ...
def getPointPlace(nb):
    size = getNumberSize(nb)
    if size % 2 == 0:
        size = int(size / 2)
    else:
        size = int((size / 2)) + 1
    return size

#find the bigger number wich the square fit in the number 10 -> 3, 30 -> 5, ...
def findBiggerSquare(nb, ratio):
    max_sqrt = 0
    for i in range(int(nb + 1)):
        tmp = 0
        if ratio != 1:
            tmp = ((int(ratio) * (getNumberRange(i) * 10 ) + i) * i)
        else:
            tmp = i * i
        if tmp <= nb and tmp > max_sqrt:
            max_sqrt = (i)
        if tmp > nb:
            break
    return (max_sqrt)