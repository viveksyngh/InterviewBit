__author__ = 'Vivek'

def backtrack(res, a, k, L, B) :
    if B < 0 or k >= len(L) :
        return
    else :
        if B == 0:
            res.append(tuple(a[:]))
        else :
            while k < len(L) and B - L[k] >= 0:
                a.append(L[k])
                backtrack(res, a, k+1, L, B-L[k])
                a.pop()

def comb(A, B) :
    res = []
    a = []
    A.sort()
    backtrack(res, a, 0, A, B)
    res = set(res)
    result = []
    for r in res :
        result.append(list(r))
    result.sort()
    return result

print comb([2,3,6,7], 7)
