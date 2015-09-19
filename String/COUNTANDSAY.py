__author__ = 'Vivek'
#This will Generate count-and-say sequence
def countAndSay(A):
        seq = ''
        prevSeq = '1'
        if A==1 :
            return '1'
        for i in range(0, A-1) :
            seq = ''
            count = 1
            for j in range(0, len(prevSeq)) :
                if j < len(prevSeq)-1 and prevSeq[j] == prevSeq[j+1] :
                    count = count + 1
                elif j < len(prevSeq)-1 and prevSeq[j] != prevSeq[j+1] :
                    seq += str(count)
                    seq += str(prevSeq[j])
                    count = 1
                elif j == len(prevSeq)-1 :
                    seq += str(count) + str(prevSeq[j])
            prevSeq = seq
        return seq
