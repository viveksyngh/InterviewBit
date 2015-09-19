__author__ = "Vivek"

#Implement pow(A, B) % C.
#In other words, given A, B and C,
#find (AB)%C.

# @param A : integer
# @param B : integer
# @param C : integer
# @return an integer
def Mod(self, A, B, C):
    if A == 0 :
        return 0
    if B == 0:
        return 1
    elif B%2 == 0 :
        y =  self.Mod(A, B/2, C)
        return (y * y)%C
    else :
        return (A%C * self.Mod(A, B - 1, C))%C
