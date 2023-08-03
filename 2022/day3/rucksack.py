
def get_input():
    f = open("in.txt", "r")

    sack = []
    for line in f.readlines():
        sack.append(line)

    f.close()

    return sack


def get_shared(s1, s2):
    s1_set = set(s1)
    s2_set = set(s2)

    if s1_set > s2_set: # loop through the smaller set
        max_set = s1_set
        min_set = s2_set
    else:
        max_set = s2_set
        min_set = s1_set

    for s in min_set:
        if s in max_set:
            return s
    
    return ""


def parse_sack(sacks):
    total_priority = 0
    for sack in sacks:
        compartment_len = len(sack) // 2
        
        first = sack[:compartment_len] # exclusive
        second = sack[compartment_len:] # inclusive

        shared = get_shared(first, second)

        if shared == shared.lower(): # is not lowercase
            priority = ord(shared) - 96
        else:
            priority = ord(shared) - 38

        total_priority += priority

    return total_priority

if __name__=="__main__":
    rucksacks = get_input()

    print(parse_sack(rucksacks))