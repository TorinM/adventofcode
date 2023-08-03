
def get_input():
    f = open("in.txt", "r")

    group_id = 0
    
    groups = [[]]
    for i, line in enumerate(f.readlines()):
        if i % 3 == 0 and i != 0:
            group_id += 1
            groups.append([])
        
        groups[group_id].append(line.strip())

    f.close()

    return groups


def find_group_id(groups) -> str:
    return (set(groups[0]) & set(groups[1]) & set(groups[2])).pop()


def get_priority(groups):
    
    total_priority = 0
    for group in groups:
        shared = find_group_id(group)
        if shared == shared.lower(): # is not lowercase
            priority = ord(shared) - 96
        else:
            priority = ord(shared) - 38

        total_priority += priority

    return total_priority

if __name__=="__main__":
    groups = get_input()

    print(get_priority(groups))