class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dic = {(0,0)}
        a = (0,0)
        for i in path:
            if i == "N":
                a = (a[0],a[1]+1)
            elif i == "S":
                a = (a[0],a[1]-1)
            elif i == "E":
                a = (a[0]+1,a[1])
            elif i == "W":
                a = (a[0]-1,a[1])
            if a in dic:
                return True
            else:
                dic.add(a)
        return False
               
