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


