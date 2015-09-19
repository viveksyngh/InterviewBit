__author__ = 'Vivek'

#Given an array of integers, sort the array into a wave like array and return it,
#In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....
# @param A : A List of integers
# @return List of integers

def wave(A):
      A.sort()
      i = 0
      while i < len(A) :
          if i + 1 < len(A) :
              A[i], A[i+1] = A[i+1], A[i]
              i = i + 2
          else :
             i = i + 1
      return A

