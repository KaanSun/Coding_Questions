# 
# slow solution intended for unsorted list.
# for sorted height list, the solution is O(n)
# however, for unsorted list, the solution is O(n^2)
#
class Solution(object):
    def maxArea(self, height):
        places = []
        for i in range(0,len(height)):
            places.append(i)
        
        biggestvol = 0
        if len(height) == 2:
            if height[0]<height[1]:
                return height[0] 
            else:
                return height[1]


        for i in range(0,len(height)-1):
            biggestH = 0
            if i not in places:
                continue
            for j in range(len(height)-1,i,-1):
                shortestH = 0
                if height[j] <= biggestH:
                    height.remove(j)
                    places.remove(j)
                    continue
                if height[i] <= height[j]:
                    shortestH = height[i]
                else:
                    shortestH = height[j]
                volrn = shortestH * (places[j]-places[i])
                if volrn > biggestvol:
                    biggestvol=volrn
                    biggestH = height[j]

        
        return biggestvol
        

        
        
print(Solution().maxArea([1,2,4,3]))