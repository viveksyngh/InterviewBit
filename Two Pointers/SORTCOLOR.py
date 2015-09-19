__author__ = 'Vivek'

#Given an array with n objects colored red, white or blue,
#sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

def sortColors(self, A):
        red = []
        white = []
        blue = []
        for a in A :
            if a == 0 :
                red.append(a)
            elif a == 1 :
                white.append(a)
            else :
                blue.append(a)
        return red + white + blue
