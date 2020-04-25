'''
Problem Statement:
    Imagine if we have (m) players and (n) coins. 
    Assumption1: n >= m.
    Assumption2: each coin is unique.
    -- There are x rounds in a given game. In each round, each player will be assigned a unique coin from given (n) coins.
    -- We need to find all combinations of coin assignments to m players in different rounds.
    -- The coin assigned in each round to a player should be different from the earlier assignments. 

Algorithm/Solution:

    The number of ways "n" items can be assigned to "m" people is (n) combinatories of (m) i.e, n!/(n-m)!*m! 
    In a given round
        1. We have n coins, and m players to begin with.
        2. So, player1 can be assigned with n coins in  n C 1 ways i.e., (n!/(n-1)!*1!)
        3. Since 1 coin is assigned to player1, now player2 will only have (n-1) coins to be assigned with in n-1c1 ways i.e, (n-1)!/(n-2)!*1!
        4. As such two coins are already asigned. So, player3 can be assigned with n-2 C 1 ways i.e., (n-2)!/((n-3)!1!) ways. 
        5. Similarly, player x can be assigned with n-x-1 C 1 ways, i.e, (n-x-1)!/(n-x-2)!*1!
        6. Now, continue the above approach for different rounds.  
Inputs:

[m1, m2, m3, m4...]: Array of m players.

[n1, n2, n3, n4...]: Array of n coins.

x: number of rounds.

Validate constraints:
    Constraint1: validate n >= m.
    Constraint2: validate n >= x.

Global assignment buffers:
    player_assignment_buffer = {} //Keeps track of individual assignment of coins to each player in each round.
    final_output_assignment = {} //Represents the final assignments for different rounds.

set nSize = n.size()
set mSize = m.size()

Note: pij ==> denotes the assignment for round 'i' and player 'j'

round1:
   Set player1_coin_assignment(p11)  = (n)  % rand(0, nSize)  
   Set player2_coin_assignment(p12) = (n - p11) % rand(0, nSize-1)
   Similarly, set player3_coin_assignment(p13) = (n - (p11+p12)) % rand(0, nSize-2) 

   .... So, on player_n_coin_assignment = (n- (p11+p12+p13...p1n-1)) % rand(0, nSize-n)
 
   Now, update player_assignment_buffer = {'m1': [p11], 'm2': [p12], 'm3': [p13]...}
   Set final_output_assignment = {'round1': player_assignment_buffer} 


round2:
   Set player1_coin_assignment(p21) = (n-p11) % rand(0, nSize-1)
   Set player2_coin_assignment(p22) = (n-p21-p12) % rand(0, nSize-2)
   Set player3_coin_assignment(p23) = (n-p21-p12-p22) % rand(0, nSize-3)
   Similarly, set player_n_coin_assignment = (n - (p21+p22+p23) - p1n) % rand(0, nSize-n)
   
   Now, update player_assignment_buffer = {'m1': [p11, p21], 'm2': [p12, p21]...}
   Set final_output_assignment = { 'round1' : {}, 'round2': {} }

....

Continue the above approach of assignment till round(x).

return final_output_assignment.   
'''

import random

class CoinAssignmentAlgorithm:

    def __init__(self, n, m, x):
        self.coin_list = n
        self.player_list = m
        self.total_rounds = x
        if not  self.coin_list or not self.player_list:
            raise 'Empty inputs for coins (or) players. Please check'
        
        self.coin_listSize = len(n)
        self.player_listSize = len(m)
        
        self.player_assignment_tracker = {} 
        self.final_output_assignment = {}


    def __validate(self):
        if (self.coin_listSize < self.player_listSize) or (self.coin_listSize  < self.total_rounds):
            raise Exception('''Constraints failed. Please check the inputs
                 Constraint1: validate number of coins >= number of players.
                 Constraint2: validate number of coins >= number of rounds.
              ''')
        print "constraints passed."


    def __algorithm(self):

        for member in self.player_list:
            self.player_assignment_tracker[member] =  [] 

        for i in range(1, self.total_rounds+1):
            
            round_info = 'round_' + str(i)
            self.final_output_assignment[round_info] = {}
            print '\n\n===== Current round: {} ===='.format(round_info)
            current_round_assignment = {}
            round_assignment_list = []

            for player in self.player_list:
                available_assignment_list = list(set(self.coin_list) - set(self.player_assignment_tracker[player])) 
                player_coin_assignment = available_assignment_list[random.randint(0, len(available_assignment_list)-1)]
                round_assignment_list.append(player_coin_assignment)
                self.player_assignment_tracker[player].append(player_coin_assignment)
                current_round_assignment[player] = player_coin_assignment 
           
            print 'round: {}.  Assignment:  {}'.format(round_info, current_round_assignment)
            self.final_output_assignment[round_info] = current_round_assignment
           
        print '\n\n============== Final Assignment: {} ==========='.format(self.final_output_assignment)


    def run(self):
        self.__validate()
        self.__algorithm()



if "__name__" != "__main__":
    ### test1: outputs: {'round_2': {'y': 'b', 'x': 'a'}, 'round_1': {'y': 'a', 'x': 'b'}}
    caa = CoinAssignmentAlgorithm(['a', 'b'], ['x', 'y'], 2)
    caa.run()
    
    ### test2: outputs: {'round_2': {'y': 'b', 'x': 'c', 'z': 'b'}, 'round_1': {'y': 'c', 'x': 'b', 'z': 'a'}}
    caa = CoinAssignmentAlgorithm(['a', 'b', 'c'], ['x', 'y', 'z'], 2)
    caa.run()

    ### test3: outputs: {'round_2': {'y': 'a', 'x': 'b', 'z': 'a'}, 'round_3': {'y': 'b', 'x': 'a', 'z': 'c'}, 'round_1': {'y': 'c', 'x': 'c', 'z': 'b'}}
    caa = CoinAssignmentAlgorithm(['a', 'b', 'c'], ['x', 'y', 'z'], 3)
    caa.run()

    ### test4: throws an exception as number of rounds are more than number of coins available.
    caa = CoinAssignmentAlgorithm(['a', 'b', 'c'], ['x', 'y', 'z'], 4)
    caa.run()

