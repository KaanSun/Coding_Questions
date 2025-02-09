"""
This function implements the Divide and Conquer (DNC) algorithm to find the best buy/sell combination
for a given list of stock prices. The goal is to maximize the profit by identifying the optimal days
to buy and sell the stock.

Parameters:
    prices (list): A list of integers representing the stock prices on different days.

Returns:
    tuple: A tuple containing two integers:
        - The maximum profit that can be achieved.
        - A tuple with two elements representing the best day to buy and the best day to sell.

The function works by recursively dividing the list of prices into smaller sublists, finding the
maximum profit in each sublist, and then combining the results to find the overall maximum profit.
"""

def MaxPriceDNC(stockList, startindex, endindex):
    lenList = endindex - startindex + 1
    if lenList <= 5:
        maxprof = 0 
        bestbuy = -1
        bestsell = -1
        for i in range(startindex, endindex ):
            for j in range(i,endindex + 1):
                if stockList[j] - stockList[i] > maxprof:
                    maxprof = stockList[j] - stockList[i]
                    bestbuy = i
                    bestsell = j
        return bestbuy , bestsell 
    else:
        midpoint =  int((endindex + startindex)/2)
        ileft, jleft = MaxPriceDNC(stockList, startindex, midpoint)
        iright, jright = MaxPriceDNC(stockList, midpoint+1, endindex)

        if stockList[jleft] - stockList[ileft] >= stockList[jright] - stockList[iright] and stockList[jleft] - stockList[ileft] >= stockList[jright] - stockList[ileft]:
            return ileft, jleft
        elif stockList[jright] - stockList[iright] >= stockList[jright] - stockList[ileft]:
            return iright, jright
        else:
            return ileft, jright


stockList = [100, 180, 260, 310, 40, 535, 695]
startindex = 0
endindex = len(stockList) - 1
print(MaxPriceDNC(stockList, startindex, endindex))
# (4, 6))

# Additional test case
stockList = [120, 110, 50, 150, 90, 200, 220, 80, 300, 250, 400, 140 , 500]
startindex = 0
endindex = len(stockList) - 1
print(MaxPriceDNC(stockList, startindex, endindex))
# Expected output: (2, 12) - Buy at 50, sell at 500
    