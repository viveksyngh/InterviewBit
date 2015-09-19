__author__ = 'Vivek'
#You are in an infinite 2D grid where you can move in any of the 8 directions :
#(x,y) to
#    (x+1, y),
#    (x - 1, y),
#    (x, y+1),
#    (x, y-1),
#    (x-1, y-1),
#    (x+1,y+1),
#    (x-1,y+1),
#    (x+1,y-1)
#You are given a sequence of points and the order in which you need to cover the points.
#Give the minimum number of steps in which you can achieve it. You start from the first point.

def coverPoints(self, X, Y):
        totalStep = 0
        currentX = X[0]
        currentY = Y[0]
        for i in range(1, len(X)) :
            totalStep += max(abs(currentX - X[i] ), abs(currentY - Y[i]))
            currentX = X[i]
            currentY = Y[i]
        return totalStep


