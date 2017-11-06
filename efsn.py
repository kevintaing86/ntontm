"""
 efsn is a surjection from natural numbers to FSN(set of all finite sequences of natural numbers)
"""

def efsn(k):
    """
    function g(k)
    :param k: Any natural number
    :return: list of natural numbers
    """
    prmf = prime_factorization(k)
    s = []
    if len(prmf) == 0 or not in_range_f(prmf):
        return []
    else:
        while prmf != []:
            s.append(prmf.count(prmf[0]) - 1)
            prmf = removeFromList(prmf[0], prmf)
    return s

def in_range_f(prmf):
    if len(prmf) == 0:
        return False

    x = 1
    current = prime(x)
    while current != prmf[-1]:
        if prmf.count(current) == 0:
            return False
        x = x + 1
        current = prime(x)
    return True

def prime_factorization(k):
    """
    determines the prime factorization of a natural number
    :param k: natural number
    :return: list of the prime factorization
    """
    pf = []
    num = 1

    if not is_prime(k) and not k <= 1:
        while k != 1:
            if k % prime(num) == 0:
                k = k / prime(num)
                pf.append(prime(num))
                num = 1
            else:
                num = num + 1
    return pf

def prime(i):
    """
    returns the ith prime number
    :param i: index
    :return: prime number
    """
    num = 1
    while i != 0:
        num = num + 1
        if is_prime(num):
            i = i - 1
    return num

def is_prime(num):
    """
    Returns whether a number is prime or not
    :param num: a number
    :return: boolean
    """
    if num <= 1:
        return False
    for x in range(1, num-1):
        if x == 1:
            pass
        elif num % x == 0:
            return False
    return True

def removeFromList(el, list):
    newList = []
    for x in list:
        if x != el:
            newList.append(x)
    return newList