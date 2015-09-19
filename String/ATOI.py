__author__ = 'Vivek'
#Convert a string to number, if Integer Overflows return INT_MAX if number is positive , otherwise INT_MIN
def atoi(A):
        """
        :param: A string which need to be converted to integer
        :return: An integer
        """
        num = 0
        A = A.strip()
        INT_MAX = 2**31 - 1
        INT_MIN = -INT_MAX - 1
        isneg = False
        for char in A :
            if num == 0 and char == '-' :
                isneg = True
            elif num == 0 and char == '+' :
                isneg = False
            elif char in "0123456789" :
                num = num * 10 + int(char)
            else :
                break
        if num > INT_MAX and not isneg :
            return INT_MAX
        elif num > INT_MAX+1 and isneg :
            return INT_MIN
        elif isneg:
            return -num
        else :
            return num

print(atoi("  +78 UA 8194-4   ")) # Will Return +78
print(atoi("-7385 @U 3505")) # Will return -7385
print(atoi(" -512346768969 89q-4")) #Will return -2147483648
print(atoi(" 512346768969 89q-4")) #Will return 2147483648
