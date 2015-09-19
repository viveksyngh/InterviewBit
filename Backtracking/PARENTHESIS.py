__author__ = 'Vivek'
def isValid(A):
    stack = []
    for char in A :
        if char == '(' :
            stack.append('(')
        else :
            if len(stack) == 0:
                return 0
            else :
                stack.pop()
    if len(stack) == 0:
        return 1
    else :
        return 0

def is_solution(a, k, L, B) :
    if k == B :
        return isValid(a[:k])
    else :
        return False

def construct_candidates(a, k, L, B) :
    temp = L[:]
    for i in a[:k] :
        temp.remove(i)
    return temp

def backtrack(res, a, k, L, B) :
    if is_solution(a, k, L, B) :
        res.append(tuple(a[:]))
        return
    cand = construct_candidates(a, k, L, B)
    for j in range(len(cand)) :
        a[k] = cand[j]
        backtrack(res, a, k+1, L, B)


def parenthesis(n) :
    res = []
    a = [-1] * (2*n)
    A = ["("] * n + [")"] * n
    #print A
    B = 2 * n
    backtrack(res, a, 0, A, B)
    res = set(res)
    result = []
    for r in res :
        result.append("".join(list(r)))
    result.sort()
    return result
print(parenthesis(3))