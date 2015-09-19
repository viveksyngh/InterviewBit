__author__ = 'Vivek'
#Given a read only set of n + 1 integers between 1 and n,
#find one number that repeats in linear time using less then O(n) space
# and traversing the stream sequentially O(1) times.

# @param A : tuple of integers
# @return an integer
def repeatedNumber(A):
    count_dict = {}
    for a in A :
        count_dict[a] = count_dict.get(a, 0) + 1
    for key in count_dict.keys() :
        if count_dict[key] > 1:
            return key
