'''
Problem Statement

Given an array prices where prices[i] is the stock price on day i, find the best day to buy and sell to maximize profit.
Return the maximum profit you can achieve.
If no profit can be made, return 0.
'''
# it is kinda embarrasing how simple this solution is ... 
def BestProfit(lista):
    buyprice = float('inf')
    maxprof = 0

    for i in range(0,len(lista)):
        if lista[i] < buyprice:
            buyprice = lista[i]
        if lista[i] - buyprice > maxprof:
            maxprof = lista[i] - buyprice

    return maxprof

print(BestProfit([7,1,5,3,6,4]))
print(BestProfit([7,6,4,3,2,1]))