__author__ = 'Vivek'
def lengthOfLastWord(A):
        start =0
        end = 0
        if len(A) == 0 :
            return 0
        lastLength = 0
        curLength = 0
        for i in range(len(A)) :
            if A[i] != ' ' :
                curLength += 1
            else :
                if curLength != 0 :
                    lastLength = curLength
                curLength = 0
        if  curLength != 0 :
            lastLength = curLength
        return lastLength
print(lengthOfLastWord('   '))