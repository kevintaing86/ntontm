"""
 encodesTM is a function from FSN(finite sequence of natural numbers) to Boolean
 This function will return whether or not an FSN can be a numeric turing machine
"""

def functional(table):
    """
    Checks if table has 2 distinct tuples where the first 2 coordinates are the same.
    If so return false
    Otherwise return true
    :param table: a set of 5-tuples
    :return: Boolean
    """
    if table == []:
        return False
    for t1 in table:
        for t2 in table:
            if t1[0:2] == t2[0:2] and t1[2:6] != t2[2:6]:
                return False
    return True

def correct_format(table):
    """
    Determines whether or not each instruction in table meets the NTM format.
    That is, 2nd and 4th coordinate is 0-10 and 5th coordinate it 0-1
    :param table: a set of 5-tuples
    :return: Boolean
    """
    for i in table:
        if i[1] < 0 or i[1] > 10:
            return False
        if i[3] < 0 or i[3] > 10:
            return False
        if i[4] != 1 and i[4] != 0:
            return False
    return True

def encodesTM(fsn):
    """
    Returns true if the fsn can be encoded into a numeric turing machine and false otherwise
    :param fsn: finite sequence of natural numbers
    :return: Boolean
    """
    if len(fsn) % 5 != 2:
        return False

    table = []
    for x in range(2,len(fsn),5):
        instruc = (fsn[x], fsn[x+1], fsn[x+2], fsn[x+3], fsn[x+4])
        table.append(instruc)

    if functional(table) and correct_format(table):
        return True
    else:
        return False


