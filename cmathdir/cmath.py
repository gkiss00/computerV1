def c_sum(a, b):
    return rounding(a + b)

def c_sub(a, b):
    return rounding(a - b)

def c_mult(a, b):
    return rounding(a * b)
    
def c_div(a, b):
    return rounding(a * b)

#get the rest of the divion
def c_mod(a, b):
    tmp = int(a / b)
    return (a - (b * tmp))

#get abs value of a number
def c_abs(nb):
    if "-" in str(b):
        nb = nb * -1
    return nb

#get the power of a number
def c_pow(a, b):
    result = 1
    #if b < 0
    if "-" in str(b):
        a = 1 / a
    for i in range(b):
        result *= float(a)
    return result

#get the root square of a number
def c_sqrt(nb):
    final_result = 0.0
    ratio = 0
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
        n = findBiggerSquare(pair_list[i], ratio * 2)
        #rest : rest of the divison
        if ratio == 0:
            tmp = n * n
        else:
            tmp = ((int(ratio * 2) * (getNumberRange(n) * 10 )) + n) * n
        rest = pair_list[i] - tmp
        #update ratio
        ratio = (ratio * (getNumberRange(n) * 10)) + n
        #if we are in int
        if (i < point):
            _range = getNumberRange(n) * 10
            final_result = (final_result * _range) + n
        #if we are in float
        else:
            final_result = final_result + (n / div)
            div *= 10
    return rounding(final_result)

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

def getPointSize(nb):
    size = 0
    nb = nb - int(float(nb))
    while nb != 0:
        nb = nb * 10
        tmp = int(nb)
        tmp = tmp + 0.0
        nb -= tmp
        size += 1
    return (size)

#utils find the bigger number wich the square fit in the number 10 -> 3, 30 -> 5, ...
def findBiggerSquare(nb, ratio):
    max_sqrt = 0
    for i in range(int(nb + 1)):
        tmp = 0
        if ratio != 0:
            tmp = ((int(ratio) * (getNumberRange(i) * 10 )) + i) * i
        else:
            tmp = i * i
        if tmp <= nb and tmp > max_sqrt:
            max_sqrt = (i)
        if tmp >= nb:
            break
    return (max_sqrt)

#3 decimal number
def rounding(nb):
    nb = nb * 10000
    nb = int(float(nb))
    last = nb % 10
    nb = nb / 10
    nb = int(float(nb))
    last2 = nb % 10
    nb = nb - last2
    if last > 5:
        last2 += 1
    nb += last2
    nb = nb / 1000
    return nb