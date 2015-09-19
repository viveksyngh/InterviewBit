__author__ = 'Vivek'

#Given an array of strings, return all groups of strings that are anagrams.
#Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.

def anagrams(self, A):
        groups = dict()
        for i in range(len(A)) :
            string = A[i]
            temp = "".join(sorted(string))
            if groups.get(temp, []) == [] :
                groups[temp] = []
                groups[temp].append(i+1)
            else :
                groups[temp].append(i+1)
        return groups.values()



