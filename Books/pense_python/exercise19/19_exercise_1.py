'''
def binomial_coeff(n, k):
    """Compute the binomial coefficient "n choose k".

    n: number of trials
    k: number of successes
    returns: int

    """
    if k == 0:
        return 1
    if n == 0:
        return 0
    res = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)

    return res
'''

from collections import defaultdict

#No memo:
def binomial_coeff_no_memo(n, k):
    return(
        1 if k == 0 else
        0 if n == 0 else
        binomial_coeff_no_memo(n-1, k) + binomial_coeff_no_memo(n-1, k-1)
    )

#With MEMO:
#know[n,k]
know = defaultdict(int)
know[(0,0)] = 0
def binomial_coeff(n, k): 
    value = (
        know[(n, k)] if (n,k) in know else
        1 if k == 0 else
        0 if n == 0 or k > n else
        None
    )
    if value is not None:
        return value
    know[(n, k)] = binomial_coeff(n-1, k) + binomial_coeff(n-1, k-1)
    return know[(n,k)]

print(binomial_coeff(6,3))

#CHATGPT: I didnt remember SETDEFAULT
'''

def binomial_coeff(n, k):
    value = (
        know[(n, k)] if (n, k) in know else
        1 if k == 0 else
        0 if n == 0 or k > n else
        None
    )
    return value if value is not None else know.setdefault((n, k), binomial_coeff(n - 1, k) + binomial_coeff(n - 1, k - 1))
'''