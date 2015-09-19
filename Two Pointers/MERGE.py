__author__ = 'Vivek'

#Given two sorted integer arrays A and B, merge B into A as one sorted array.
#Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
#TIP: C users, please malloc the result into a new array and return the result.
#If the number of elements initialized in A and B are m and n respectively,
#the resulting size of array A after your code is executed should be m + n

def merge(self, A, B):
        i , j = 0, 0
        temp = A[:]
        A = []
        while i < len(temp) and j < len(B) :
            if temp[i] > B[j] :
                A.append(B[j])
                j += 1
            else :
                A.append(temp[i])
                i += 1
        while i < len(temp) :
            A.append(temp[i])
            i += 1

        while j < len(B) :
            A.append(B[j])
            j += 1
        return A