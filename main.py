import sys
import heapq
import time

Pancake_Usage = "Syntax: '[value, value, value, ...., value]' \
 (All must be size 1 to 10 with no repeats)"
Algo_Usage = "Syntax: 'UCS' or 'A*'"
Goal_State = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def main():
    user_input = input("Give me a random stack of pancakes "
    "size 10\nSyntax: '[value, value2, value3, ...., value10]'"
    " (All must be size 1 to 10 with no repeats)\n"
    "Stack: ")
    pancakes = user_input[1:-1]
    try:
        pancakes = [int(num_str) for num_str in pancakes.split(", ")]
        if len(pancakes) != 10 or len(set(pancakes)) != 10 \
        or min(pancakes) < 1 or max(pancakes) > 10:
            raise ValueError
    except Exception:
        print("ERROR: invalid pancake input")
        print(Pancake_Usage)
        sys.exit(1)
    user_input = input("Specify which algorithm you want to solve with.\n"
    "Syntax: 'UCS' or 'A*'\n""Algorithm: ")
    start_time = time.time()
    if user_input == "UCS":
        UCS_search(pancakes)
    elif user_input == "A*":
        A_search(pancakes)
    else:
        print("ERROR: invalid algo input")
        print(Algo_Usage)
        sys.exit(1)
    end_time = time.time()
    print(f'Runtime: {end_time - start_time:.4f} seconds')


def UCS_search(nums: list[int]):
    visited = dict()
    frontier = [(0, nums, [])]  # (cost, state, actions)
    while frontier:
        cost, current_state, actions = heapq.heappop(frontier)
        if current_state == Goal_State:
            print("Found Solution (Insert under index #, one indexed):", actions)
            return
        for i in range(len(nums) - 2, -1, -1): #flipping top pancake is useless
            new_state = current_state[:i] + current_state[i:][::-1]
            new_cost = cost + (len(nums) - i)
            new_actions = actions + [i+1]
            
            t_s = tuple(new_state) # lists cannot be used as keys in dict
            if t_s not in visited or \
            new_cost < visited.get(t_s, float('inf')):
                visited[t_s] = new_cost
                heapq.heappush(frontier, (new_cost, new_state, new_actions))
    return
    #For loop will prioritize our cost (How many pancakes we flip)
    #Solution will always be found so don't need to do much else
                


def A_search(nums: list[int]):
    visited = dict()
    frontier = [(0, nums, [])]  # (cost, state, actions)
    while frontier:
        cost, current_state, actions = heapq.heappop(frontier)
        if current_state == Goal_State:
            print("Found Solution (Insert under index #, one indexed):", actions)
            return
        for i in range(len(nums) - 2, -1, -1): #flipping top pancake is useless
            new_state = current_state[:i] + current_state[i:][::-1]
            new_cost = gap_heuristic(new_state) + cost + (len(nums) - i)
            new_actions = actions + [i+1]
            
            t_s = tuple(new_state) # lists cannot be used as keys in dict
            if t_s not in visited or \
            new_cost < visited.get(t_s, float('inf')):
                visited[t_s] = new_cost
                heapq.heappush(frontier, (new_cost, new_state, new_actions))
    return

def gap_heuristic(nums: list[int]):
    count = 0
    for i in range(len(nums) - 1): #we stop one index early for avoiding range error
        if abs(nums[i] - nums[i+1]) != 1:
            count += 1
    return count

if __name__ == "__main__":
    main()