__author__ = 'Vivek'

#Given a collection of candidate numbers (C) and a target number (T),
#find all unique combinations in C where the candidate numbers sums to T.
#Each number in C may only be used once in the combination.

def is_solution(a, k, L, B) :
    return k == B

def construct_candidates(a, k, L, B) :
    temp = L[:]
    for i in a[:k] :
        temp.remove(i)
    return temp

def backtrack(res, a, k, L, B) :
    if B < 0  or k > len(L):
        return
    else :
        if B == 0:
            res.append(tuple(sorted(a[:])))
        else :
            cand = construct_candidates(a, k, L, B)
            for i in range(len(cand)) :
                a.append(cand[i])
                backtrack(res, a, k+1, L, B-cand[i])
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

print comb([ 8, 10, 6, 11, 1, 16, 8 ], 28)
print comb([ 1 , 1, 1, 1, 1], 5)
