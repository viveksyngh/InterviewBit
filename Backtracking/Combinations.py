__author__ = 'Vivek'

#Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.
#Make sure the combinations are sorted.

def is_solution(a, k, L, B) :
    return k == B

def construct_candidates(a, k, L, B) :
    if a[k-1] == -1 :
        return L[0:]
    else :
        temp = L.index(a[k-1])
        return L[temp+1:]

def backtrack(res, a, k, L, B) :
    if is_solution(a, k, L, B) :
        res.append(a[:])
        return
    cand = construct_candidates(a, k, L, B)
    for j in range(len(cand)) :
        a[k] = cand[j]
        backtrack(res, a, k+1, L, B)

def permuations(n, B) :
    A = range(1, n+1)
    res = []
    a = [-1] * B
    backtrack(res, a, 0, A, B)
    return res

print(permuations(4, 3))
