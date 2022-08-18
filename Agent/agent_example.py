import Setup
import numpy as np
from time import time

def agent_example(p_state, temp_file, per_file):
    if len(per_file) < 2:
        per_file = [0,0]
    
    list_action = Setup.get_list_action(p_state)
    act_idx = np.random.randint(0, len(list_action))
    if Setup.check_victory(p_state) == 1:
        per_file[0] += 1
    elif Setup.check_victory(p_state) == 0:
        per_file[1] += 1
    
    return list_action[act_idx], temp_file, per_file

a = time()
print(Setup.normal_main([Setup.random_player,Setup.random_player,Setup.random_player,Setup.random_player], 1, True))
print(time()-a)

a = time()
print(Setup.normal_main([Setup.random_player,Setup.random_player,Setup.random_player,Setup.random_player], 1000, False))
print(time()-a)