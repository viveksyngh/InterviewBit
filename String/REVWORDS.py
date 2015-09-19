__author__ = 'Vivek'
#reverse the string word by word.
def reverseWords(A):
        """
        Reverse the string word by word, removes leading and trailing spaces,
        :param: string to be reversed
        :return: reversed string word by word
        """
        curWord = ''
        listOfWords = []
        for char in A :
            if char != ' ' :
                curWord += char
            else :
                if curWord != '' :
                    listOfWords.append(curWord)
                curWord = ''
        if curWord != '' :
            listOfWords.append(curWord)
        listOfWords.reverse()
        return " ".join(word for word in listOfWords)


