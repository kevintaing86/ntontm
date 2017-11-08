"""
 Determines if a natural number can be encoded to a NTM
"""
import encodesTM
import efsn

def numEncodesTM(n):
    """
    Returns true is n can be encoded to a NTM, false otherwise
    :param n: natural number
    :return: boolean
    """
    fsn = efsn(n)

    if encodesTM(fsn):
        return True
    else:
        return False
