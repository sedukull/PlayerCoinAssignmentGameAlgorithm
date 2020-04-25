# Player Coin Assignment Game Algorithm
Given set of coins 'n', and set of players 'm', and 'x' number of rounds. Assigns a unique coin to each player in different rounds of a game.


## Problem Statement:

 Imagine if we have (m) players and (n) coins. 
    Assumption1: n >= m.
    Assumption2: each coin is unique.
    -- There are x rounds in a given game. In each round, each player will be assigned a unique coin from given (n) coins.
    -- We need to find all combinations of coin assignments to m players in different rounds.
    -- The coin assigned in each round to a player should be different from the earlier assignments. 

### Algorithm/Solution:
    The number of ways "n" items can be assigned to "m" people is (n) combinatories of (m) i.e, n!/(n-m)!*m! 
    In a given round,
        1. We have n coins, and m players to begin with.
        2. So, player1 can be assigned with n coins in  n C 1 ways i.e., (n!/(n-1)!*1!)
        3. Since 1 coin is assigned to player1, now player2 will only have (n-1) coins to be assigned with in n-1c1 ways i.e, (n-1)!/(n-2)!*1!
        4. As such two coins are already asigned. So, player3 can be assigned with n-2 C 1 ways i.e., (n-2)!/((n-3)!1!) ways. 
        5. Similarly, player x can be assigned with n-x-1 C 1 ways, i.e, (n-x-1)!/(n-x-2)!*1!
        6. Now, iterate the above approach for various rounds. However, in each round keep track of previous assignments to the players so as to make the assignment unique.

#### Inputs:
[m1, m2, m3, m4...]: Array of m players.
[n1, n2, n3, n4...]: Array of n coins.
x: number of rounds.


### Validate constraints:
    Constraint1: validate n >= m.
    Constraint2: validate n >= x.

### Global assignment buffers:
    player_assignment_buffer = {} //Keeps track of individual assignment of coins to each player in each round.
    final_output_assignment = {} //Represents the final assignments for different rounds.

* set nSize = n.size()
* set mSize = m.size()
Note: pij ==> denotes the assignment for round 'i' and player 'j'

#### round1:
   * Set player1_coin_assignment(p11)  = (n)  % rand(0, nSize)  
   * Set player2_coin_assignment(p12) = (n - p11) % rand(0, nSize-1)
   * Similarly, set player3_coin_assignment(p13) = (n - (p11+p12)) % rand(0, nSize-2) 
   .... So, on player_n_coin_assignment = (n- (p11+p12+p13...p1n-1)) % rand(0, nSize-n)
 
   Now, update player_assignment_buffer = {'m1': [p11], 'm2': [p12], 'm3': [p13]...}
   * Set final_output_assignment = {'round1': player_assignment_buffer} 

#### round2:
   * Set player1_coin_assignment(p21) = (n-p11) % rand(0, nSize-1)
   * Set player2_coin_assignment(p22) = (n-p21-p12) % rand(0, nSize-2)
   * Set player3_coin_assignment(p23) = (n-p21-p12-p22) % rand(0, nSize-3)
   * Similarly, set player_n_coin_assignment = (n - (p21+p22+p23) - p1n) % rand(0, nSize-n)
   
   Now, update player_assignment_buffer = {'m1': [p11, p21], 'm2': [p12, p21]...}
   * Set final_output_assignment = { 'round1' : {}, 'round2': {} }
   
   ** continue the above approach of assignment till round(x).

** The final_output_assignment contains the final assignments for all rounds.

#### Solution
The solution and few testss were added under PlayerCoinAssignmentGameAlgorithm.py
