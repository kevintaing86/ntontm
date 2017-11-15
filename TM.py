"""
Surjection from natural numbers to NTM
"""
import numEncodesTM
import efsn

def tm(n):
    """
    Returns the n'th NTM
    :param n: natural number
    :return: numeric turing machine
    """
    if n > 0:
        num = 0
        while n > 0:
            num = num + 1
            if numEncodesTM.numEncodesTM(num):
                n = n - 1

        fsn = efsn.efsn(num)
        table = []
        for x in range(2, len(fsn), 5):
            instruc = (fsn[x], fsn[x + 1], fsn[x + 2], fsn[x + 3], fsn[x + 4])
            table.append(instruc)

        ntm = (fsn[0], fsn[1], table)

        return ntm

    return "n must be larger than 0"
