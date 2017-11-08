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

    for t1 in table:
        for t2 in table:
            if t1[0:2] == t2[0:2] and t1[2:6] != t2[2:6]:
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
    # TODO: get the instruction to match NTM format
    for x in range(2,len(fsn),5):
        instruc = (fsn[x], fsn[x+1], fsn[x+2], fsn[x+3], fsn[x+4])
        table.append(instruc)

    if functional(table):
        return True
    else:
        return False


