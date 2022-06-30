from itertools import permutations

def permutationShow(lists:list)->list:
    return list(permutations(lists))


print(permutationShow([4,3,2,1]))