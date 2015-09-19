__author__ = 'Vivek'
#Given a set of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
#The same repeated number may be chosen from C unlimited number of times.

def backtrack(res, a, k, L, B) :
    if B < 0 :
        return
    else :
        if B == 0:
            res.append(tuple(a[:]))
        else :
            while k < len(L) and B - L[k] >= 0:
                a.append(L[k])
                backtrack(res, a, k, L, B-L[k])
                k += 1
                a.pop()

def comb(A, B) :
    res = []
    a = []
    backtrack(res, a, 0, A, B)
    res = set(res)
    result = []
    for r in res :
        result.append(list(r))
    result.sort()
    return result

print comb([2,3,6,7], 7)
