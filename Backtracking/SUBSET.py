__author__ = 'Vivek'

#Given a set of distinct integers, S, return all possible subsets.

def is_solution(a, k, L) :
    return k == len(L)

def construct_candidates(a, k, L) :
    return [0, 1]

def backtrack(res, a, k, L) :
    if is_solution(a, k, L) :
        temp = []
        for i in range(len(L)) :
            if a[i] == 1 :
                temp.append(L[i])
        res.append(temp[:])
        return
    cand = construct_candidates(a, k, L)
    for j in range(len(cand)) :
        a[k] = cand[j]
        backtrack(res, a, k+1, L)

def subset(A) :
    A.sort()
    res = []
    a = [-1] * len(A)
    backtrack(res, a, 0, A)
    res.sort()
    return res
print(subset([ 15, 20, 12, 19, 4 ]))
