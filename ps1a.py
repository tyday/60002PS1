###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    with open(filename) as f: #gets textfile with cowname,weight
        read_data = f.readlines()
        cow_dict = {}
        for line in read_data:  #splits each line by comma sep. Adds to dictionary: cow_dict
            cow_info = line.split(',')
            cow_dict[cow_info[0]] = cow_info[1].strip()
    return cow_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    tuple_cows = sorted(cows.items(), key = lambda x:x[1])
    tuple_cows.reverse()
    #print(tuple_cows) useful for debugging
    cowlists = []
    # run this while there are cows to transport and they are at limit or under
    while len(tuple_cows) > 0: # this doesn't check to see if cows are overweight(How??)
        startweight = 0
        cowlist = []
        remlist = []
        for cow in tuple_cows:
            if int(cow[1]) + startweight <= limit:
                startweight += int(cow[1])
                cowlist.append(cow[0])
                remlist.append(cow)
        cowlists.append(cowlist)
        for i in remlist:
            tuple_cows.remove(i)
    return cowlists


# cows = load_cows('ps1_cow_data.txt')
# print(greedy_cow_transport(cows,10))

# listocows =[]
# for partition in get_partitions([1,2,3]):
#     print(partition)
#     listocows.append(partition)


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    copycows = cows.copy()  #copy of the cow dictionary
    scenariolist = []  #store all permutations in this list
    bestrun = []    #store list of the best run
    ''' How does the iteration work here?
    
        '''
    for partition in get_partitions(copycows):
        scenariolist.append(partition)
    # look at each scenario individually
    # The scenarios consist of trips and the trips consist of cows
    # if any trip weighs more than the limit then the entire scenario can be discarded
    scraptrip = False
    bestrun = [] 
    for scenario in range(1,len(scenariolist), 1):
        scraptrip = False
        for trip in scenariolist[scenario]:
            if scraptrip == True:
                break
            tot_weight = 0
            for cow in trip:
                tot_weight += int(cows[cow])
            if tot_weight > limit:
                scraptrip = True
                break
        if scraptrip == False:
            if bestrun == []:
                bestrun = scenariolist[scenario]
            elif len(scenariolist[scenario]) < len(bestrun):
                bestrun = scenariolist[scenario]
    return bestrun

# cows = load_cows('ps1_cow_data.txt')
# print( brute_force_cow_transport (cows,10))
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows('ps1_cow_data.txt')
    start = time.time()
    scen = (greedy_cow_transport(cows,10))
    end = time.time()
    print('Time:', str(end-start), len(scen), scen)
    start = time.time()
    scen = brute_force_cow_transport(cows, 10)
    end = time.time()
    print('Time:', '{:.2f}'.format((end-start)), len(scen),scen)


compare_cow_transport_algorithms()