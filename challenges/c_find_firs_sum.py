# Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

# nums = [4, 5, 6, 2]
# goal = 8

# find_first_sum(nums, goal)  # [2, 3]

nums = [4, 5, 6, 2]
goal = 8

def find_first_sum(nums, goal):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == goal:
                return [i, j]

    return None


print(find_first_sum(nums, goal))