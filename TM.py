"""
Surjection from natural numbers to NTM
"""
import numEncodesTM
import efsn

def tm(n):
    """
    Returns the ntm encoded by the n'th natural number
    :param n: natural number
    :return: numeric turing machine
    """
    if n >= 0 :
        if numEncodesTM.numEncodesTM(n):
            fsn = efsn.efsn(n)

            table = []
            for x in range(2, len(fsn), 5):
                instruc = (fsn[x], fsn[x + 1], fsn[x + 2], fsn[x + 3], fsn[x + 4])
                table.append(instruc)

            ntm = (fsn[0], fsn[1], table)

            return ntm
        else:
            return []
    return "n must be larger than -1"
