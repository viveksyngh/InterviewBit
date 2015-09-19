__author__ = 'Vivek'
def is_solution(a, k, L) :
    return k == len(L)

def construct_candidates(a, k, L) :
    return list(set(L[:])-set(a[:k]))

def backtrack(res, a, k, L) :
    if is_solution(a, k, L) :
        res.append(a[:])
        return
    cand = construct_candidates(a, k, L)
    for j in range(len(cand)) :
        a[k] = cand[j]
        backtrack(res, a, k+1, L)
        #cand[j],cand[j-1] = cand[j -1], cand[j ]
def permuations(A) :
    res = []
    a = [-1] * len(A)
    backtrack(res, a, 0, A)
    return res

print(permuations([1,2,3]))