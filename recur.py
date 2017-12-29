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

def add_numb(nlist = [2,1], max = 3, memo = {}):
    if  change in nlist:
        memo[change] = 1
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
   #http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
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
   for index, result in enumerate(knownResults):
       print(index,result)
   return minCoins


def dpMakeChange(coinValueList,change,minCoins):
   for cents in range(change+1):
      coinCount = cents
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
      minCoins[cents] = coinCount
   return minCoins[change]

#print(dpMakeChange([1,5,10,25],63, [0]* 64))
# print(recMC([1,5,10,25],4, [0] * 11))

def change(n, coins_available, coins_so_far):
    #https://www.youtube.com/watch?v=EScqJEEKC10
    if sum(coins_so_far) == n:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif coins_available == []:
        pass
    else:
        for c in change(n, coins_available[:], coins_so_far+[coins_available[0]]):
            yield c
        for c in change(n, coins_available[1:], coins_so_far):
            yield c
n = 32
coins = [1,5,10,25]
solutions =  [s for s in change(n, coins, [])]
for s in solutions:
    print(s)
print(min(solutions, key=len))