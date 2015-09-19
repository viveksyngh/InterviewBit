__author__ = 'Vivek'
#Given a roman numerals, convert it into integer
def romanToInt(A):
        rtoi_dict = {'I': 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        num = 0
        for i in range(0, len(A)) :
            if A[i] == 'I' and i < len(A) - 1 :
                if A[i+1] == 'V' or A[i+1] == 'X' :
                    num += -(rtoi_dict[A[i]])
                else :
                    num += rtoi_dict[A[i]]
            elif A[i] == 'X' and i < len(A) - 1 :
                if A[i+1] == 'L' or A[i+1] == 'C' :
                    num += -(rtoi_dict[A[i]])
                else :
                    num += rtoi_dict[A[i]]
            elif A[i] == 'C' and i < len(A) - 1 :
                if A[i+1] == 'D' or A[i+1] == 'M' :
                    num += -(rtoi_dict[A[i]])
                else :
                    num += rtoi_dict[A[i]]
            else :
                num += rtoi_dict[A[i]]
        return num
