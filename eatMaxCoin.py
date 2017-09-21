# -*- coding: utf-8 -*-

# Question
# in a N x N map, from top left to bottom right, only down or right, find the path which collects the most coins


# dynamic programming:
# (also known as dynamic optimization) is a method for solving a complex problem by breaking it down
# into a collection of simpler subproblems, solving each of those subproblems just "once", and storing their solutions.


# SOLUTION:
# all possible solution: 2(n-1) C (n-1)
# except the top left and down right, we could choose direction of movement on other steps which are 2n -2 steps
# and for each possible route, only half of them are able to choose
# because the other half will touch the the edge of the map
# 除掉头尾两步，一共有2n - 2 步可以走，而只有其中的一半可以选择行进方向，因为碰到地图的边之后只能朝一个方向走了


from copy import deepcopy


def pathFinder(map):
    pathMap = []
    #number of steps to finish point is fixed
    numberOfSteps = len(map) * 2 -1

    initialPath = PathAndCoins()
    initialPath.path.append((0,0))
    initialPath.coins += map[0][0]
    pathMap.append(initialPath)

    pathMap = findPathRecur(map, pathMap, numberOfSteps)
    # pathMap.sort(key=getKey)
    pathMap.sort(key=lambda x:x.coins, reverse=True)
    # pathMap = sorted(pathMap, key=lambda x: x.coins)
    return pathMap[0]




def findPathRecur(map, pathMap, allSteps):
    newPathMap = []

    if len(pathMap[0].path) == allSteps:
        return pathMap

    for singlePath in pathMap:
        # take right or down
        latestStep = singlePath.path[-1]
        pathGoDown = singlePath.copy()
        pathGoRight = singlePath.copy()

        if latestStep[0] >= len(map)-1 and latestStep[1] >= len(map)-1:
            newPathMap.append(singlePath)
        else:
            # down  (x,y)
            if latestStep[0] < len(map)-1:
                coordX = latestStep[0] + 1
                coordY = latestStep[1]
                pathGoDown.path.append((coordX, coordY))
                pathGoDown.coins += map[coordX][coordY]
                newPathMap.append(pathGoDown)
            # right
            if latestStep[1] < len(map)-1:
                coordX = latestStep[0]
                coordY = latestStep[1] + 1
                pathGoRight.path.append((coordX, coordY))
                pathGoRight.coins += map[coordX][coordY]
                newPathMap.append(pathGoRight)
    print "next level deeper"
    return findPathRecur(map, newPathMap, allSteps)


class PathAndCoins:
    path = []   #array of coord
    coins = 0   #sum of coins

    def copy(self):
        newCopy = PathAndCoins()
        newCopy.path = deepcopy(self.path)
        newCopy.coins = deepcopy(self.coins)
        return newCopy

    def getKey(self):
        return self.coins



#****************************#

map = [[1,2,3],
       [1,0,3],
       [3,1,2]]

maxCointPath = pathFinder(map)
print map[0]
print map[1]
print map[2]
print maxCointPath.path
print maxCointPath.coins


# print coord1, coord2
# print allPath
# print map[0][2]
# print len(map)