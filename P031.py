import numpy as np


# This is just a bunch of nested for loops written generically
def brute_force(money, N):
    # data structure to simulate len(money)-nested for loop
    money = np.array(money)
    number_of_coins = np.zeros_like(money)
    upper_bound = [N//v for v in money]
    
    # for-loop counter and output list
    i = 0
    combinations = []

    # first for loop iteration needs to be done outside the loop
    if np.dot(number_of_coins, money) == N:
        print(number_of_coins)
        combinations.append( list(number_of_coins) )

    while i < len(money):
        # reached the end of one nested forloop cycle
        if number_of_coins[i] >= upper_bound[i]:
            number_of_coins[i] = 0
            i += 1
            continue
        
        # incrementing the for loop iteration
        number_of_coins[i] += 1
        i = 0

        # if we find a combination, add it
        if np.dot(number_of_coins, money) == N:
            print(number_of_coins)
            combinations.append( list(number_of_coins) )
        
        # pruning step, if we have too much money we can break and incremennt the largest
        if np.dot(number_of_coins, money) > N:
            number_of_coins[i] = 0
            i += 1

    return len(combinations)



# Let's use dynamic programming!
def dynamic_programming(money, N):
    
    money = list(sorted(money))
    M = len(money)
    C = np.zeros((N+1, M), dtype=int)   # C[t, m] = number of ways to make a total of t pence using only the first m coins
    
    C[0, :] = 1                         # base-case: number of ways to make a total of 0 is 1...do nothing
    for m in range(M):
        v = money[m]
        C[:v, m] = C[:v, m-1]           # if t < v, then C[t, m] = C[t, m-1]
        for t in range(v, N+1):
            C[t, m] = C[t, m-1] + C[t-v, m]
    
    return C[N, M-1]


def dynamic_programming_more_elegant(money, N):
    money = list(sorted(money))
    
    C = [0] * (N+1)         # C[t] = number of ways to make a total of t pence with the available coins
    C[0] = 1                # base-case: number of ways to make a total of 0 is 1...do nothing

    for v in money:
        for t in range(v, N+1):
            C[t] += C[t - v]
    
    return C[N]

""" Explanation:
Let N = the total we are trying to make
Let M = the total number of distinct coins we can use
Let the coins be indexed the variable m and v_m be the value of the mth coin

Let C[t, m] = the number of ways to make total t using all coins <= m
Then we can define the recurrence:
        v = value of the mth coin
        C[t, m] = C[t, m-1] + C[t-v, m]     if t >= v
                = C[t, m-1]                 otherwise

Intuitively, this recurrence is just 
    (# of ways to make t with <= m coins) = (# of ways to make t without coin m) + (# of ways to make t forcing at least 1 coin m to be used)

The answer will be the last element: C[N, M]
The time complexity of this is only O(NM), which is much better than O(M^N) as in the brute force method


We can make the code a bit more elegent by doing this summation in a more clever way
by removing redundant information, since we only care about C[t, M] for all t
Therefore, let C[t] = the number of ways to make total t using all coins
Essentially, in each iteration of the for-loop C[t] = C[t, m]
"""


def main(N=200):
    
    money  = [1, 2, 5, 10, 20, 50, 100, 200]
    #num_combinations = brute_force(money, N)
    #num_combinations = dynamic_programming(money, N)
    num_combinations = dynamic_programming_more_elegant(money, N)

    print(f"The number of different ways £{N/100:.2f} = {N}p be made using any number of coins is:", num_combinations)
    return num_combinations

if __name__ == "__main__":
    main()