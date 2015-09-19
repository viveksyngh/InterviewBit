__author__ = 'Vivek'
def strStr(self, haystack, needle):
        """
        :param:
        :haystack: A string
        :needle: A string
        :return: index of the first ocurrence of needle in haystack
        """
        if len(needle) == 0 or len(haystack)==0 :
            return -1
        elif needle == haystack :
            return 0
        else :
            n = len(needle)
            for i in range(0, len(haystack) - n + 1) :
                if haystack[i : i + n] == needle :
                    return i
            return -1
