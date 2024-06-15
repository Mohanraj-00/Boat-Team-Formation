def max_teams(N, weights):
    from collections import Counter
    
    # Count occurrences of each weight
    weight_counter = Counter(weights)
    
    max_teams = 0
    
    # Check for all possible sums s from 2 to 2N
    for s in range(2, 2 * N + 1):
        temp_counter = weight_counter.copy()
        teams = 0
        
        for weight in weights:
            if temp_counter[weight] > 0 and temp_counter[s - weight] > 0:
                if weight == s - weight and temp_counter[weight] < 2:
                    continue
                temp_counter[weight] -= 1
                temp_counter[s - weight] -= 1
                teams += 1
        
        max_teams = max(max_teams, teams)
    
    return max_teams

# Read input
N = int(input())
weights = list(map(int, input().split()))

# Get the maximum number of teams
result = max_teams(N, weights)
print(result)
