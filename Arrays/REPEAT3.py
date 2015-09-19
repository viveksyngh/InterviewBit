__author__ = 'Vivek'

#You’re given a read only array of n integers.
# Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.
#If so, return the integer. If not, return -1.
#If there are multiple solutions, return any one.

def repeatedNumber(self, A):
    D = {}
    for a in A :
        if a not in D.keys() and len(D) < 2 :
            D[a] = D.get(a, 0) + 1
        elif a in D.keys() :
            D[a] += 1
        elif a not in D.keys() and len(D) == 2:
            for key in D.keys() :
                D[key] -= 1
                if D[key] == 0 :
                    del D[key]
    for key in D.keys() :
        if A.count(key) > len(A)//3 :
            return key
    return -1
