def QuickSort(arr):

    length = len(arr)
    if length <= 2:
        if length != 2:
            return arr
        if arr[0] > arr[1]:
            return [arr[1],arr[0]]
        else:
            return arr

    pivot = arr[0]
    greater = []
    smaller = []
    same = []


    for ele in arr:
        if ele > pivot:
            greater.append(ele)
        elif ele < pivot:
            smaller.append(ele)
        else:
            same.append(ele)
    
    return QuickSort(smaller) + same + QuickSort(greater)


def PlatformAssignment(trainsArr):
    
    trainsArr = sorted(trainsArr, key=lambda x: x[1])
    departuresArr = []
    arrivalsArr = []
    for train in trainsArr:
        arrivalsArr.append(train[0])
        departuresArr.append(train[1])

    

    activelanes = []
    activelanesDept = []
    schedule = []
    
    for i in range(0,len(departuresArr)):
        scheduled = False
        for a in range(len(activelanes) -1 ,-1, -1):
            if activelanesDept[a] <= arrivalsArr[i]:
                activelanes.pop(a)
                activelanesDept.pop(a)

        if len(activelanes) >= 1:
            for a in range(0,max(activelanes)+1):
                if a not in activelanes:
                    activelanes.append(a)
                    activelanesDept.append(departuresArr[i])
                    scheduled = True
                    break
        if not scheduled:
            if len(activelanes) >= 1:
                activelanes.append(max(activelanes)+1)
            else:
                activelanes.append(0)
            activelanesDept.append(departuresArr[i])

        schedule.append(activelanes[-1])

    return schedule

# print(PlatformAssignment([(1220, 1300) ,(930, 1000)]))
print(PlatformAssignment([(830, 920), (700, 840), (930, 1100)]))     
print(PlatformAssignment([(700, 1000), (750, 1050), (800, 1100)]))
print(PlatformAssignment([(700, 800), (750, 850), (800, 900), (830, 950), (900, 1000)]))

        
                

        

