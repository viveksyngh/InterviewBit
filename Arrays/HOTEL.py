__author__= "Vivek"
from operator import itemgetter
def compare(a , b) :
        if a[0] <  b[0] :
            return -1
        elif a[0] == b [0] :
            if a[1] > b[1] :
                return -1
            elif a[1] == b[1] :
                return 0
            else :
                return 1
        else :
            return 1

# @param arrive : list of integers
# @param depart : list of integers
# @param K : integer
# @return a boolea
def hotel(arrive, depart, K):
        event = []
        for a in arrive :
            event.append((a, '0'))
        for d in depart :
            event.append((d, '1'))
        event.sort(cmp = compare)
        #print event
        count = 0
        for i in range(len(event)) :
            if event[i][1] == '0' :
                count += 1
            elif event[i][1] == '1' :
                count -= 1
            if count > K :
                return 0
        return 1


arrivve = [ 13, 14, 36, 19, 44, 1, 45, 4, 48, 23, 32, 16, 37, 44, 47, 28, 8, 47, 4, 31, 25, 48, 49, 12, 7, 8 ]
depart = [ 28, 27, 61, 34, 73, 18, 50, 5, 86, 28, 34, 32, 75, 45, 68, 65, 35, 91, 13, 76, 60, 90, 67, 22, 51, 53 ]
K = 23
print (hotel(arrivve, depart, K))