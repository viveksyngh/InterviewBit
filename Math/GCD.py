__author__ = 'Vivek'

#Given 2 non negative integers m and n, find gcd(m, n)

def gcd(A, B):
      while B != 0 :
          A , B = B , A%B
      return A