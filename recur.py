def getfib(n, memo = {}):
    if n in memo:
        return memo[n]
    elif n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        memo[n] = getfib(n-1) + getfib(n-2)
        return memo[n]


# for i in range(1,120):
#     print(i,getfib(i))

def add_numb(nlist = [2,1], max = 3):
    if  max == 0:
        result = (0, nlist[0])
    elif nlist[0] > max:
        #explore right branch
        result = add_numb(nlist[1:], max)
    else:
        nextItem = nlist[0]
        #explore left branch
        withVal, numbreturned = add_numb(list, max - nextItem)
        withVal += nextItem
        #explore right branch
        withoutVal, withoutnumbReturned = add_numb(list[1:], max)

def recMC(coinValueList,change, knownResults):
   minCoins = change
   if change in coinValueList:
       knownResults[change] = 1
       return 1
   elif knownResults[change] > 0:
        return knownResults[change]
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i, knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   print(knownResults)
   return minCoins

print(recMC([1,5],10, [0] * 11))