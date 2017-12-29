###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    if (len(egg_weights), target_weight) in memo:
        result = memo[(len(egg_weights), target_weight)]
    elif egg_weights == [] or target_weight == 0:
        result = (0,())
    elif egg_weights[0] > target_weight:
        #Explore right branch only
        result = dp_make_weight(egg_weights[1:], target_weight, memo)
    else:
        nextItem = egg_weights[0]
        #Explore left branch
        withVal, withToTake = dp_make_weight(egg_weights[1:], target_weight - nextItem, memo)
        withVal += nextItem
        #Explore right branch
        withoutVal, withoutToTake = dp_make_weight(egg_weights[1:], target_weight, memo)
        #choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(egg_weights), target_weight)] = result
    print(result)
    return result
    

def partitions(egg_weights):
    if not egg_weights:
        yield []
        return
    for i in range(2**len(egg_weights)//2):
        parts = [set(), set()]
        for item in egg_weights:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]] + b

def get_partitions(egg_weights):
    for partition in partitions(egg_weights):
        yield [list(elt) for elt in partition]

# egg_weights = (1, 5, 10, 25)
# scenlist = []
# for partition in get_partitions(egg_weights):
#     scenlist.append(partition)
# print(scenlist)
# print(len(scenlist))

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 6
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()