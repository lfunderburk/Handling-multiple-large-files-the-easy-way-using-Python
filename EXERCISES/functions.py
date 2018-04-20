#### Handling multiple large files the easy way using Python
#### Workshop facilitator: Laura Gutierrez Funderburk | Department of Mathematics | Simon Fraser University
#### Script Author: Laura Gutierrez Funderburk | Department of Mathematics | Simon Fraser University
#### Workshop date: April 24 2018


"""Function Definition Area"""

def remove_repetitions(family_pair):
    uniq_array = []
    for x in family_pair:
        if x not in uniq_array:
            uniq_array.append(x)
    return uniq_array