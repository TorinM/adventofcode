def get_input():
    f = open("in.txt", "r")

    pairs = []
    for line in f.readlines():
        pair_times = line.strip().split(",")

        pair = []
        for time in pair_times:
            times = time.split("-")

            pair.append((int(times[0]), int(times[1]))) # start, end tuple

        pairs.append(pair) # list of list of tuples

    return pairs


def find_complete_overlap(pairs):
    overlaps = 0
    for pair in pairs:
        elf1 = pair[0]
        elf2 = pair[1]

        elf1_start = elf1[0]
        elf1_end = elf1[1]

        elf2_start = elf2[0]
        elf2_end = elf2[1]

        # check if elf1 overlaps elf2
        if elf1_start <= elf2_start and elf1_end >= elf2_end:
            overlaps += 1
        
        # check if elf2 overlaps elf1
        elif elf2_start <= elf1_start and elf2_end >= elf1_end:
            overlaps += 1

    return overlaps


def find_some_overlap(pairs):
    overlaps = 0
    for pair in pairs:
        elf1 = pair[0]
        elf2 = pair[1]

        elf1_start = elf1[0]
        elf1_end = elf1[1]

        elf2_start = elf2[0]
        elf2_end = elf2[1]

        if (elf1_start <= elf2_start <= elf1_end) or (elf1_start <= elf2_end <= elf1_end): # elf2 in elf1 range
            overlaps += 1
        elif (elf2_start <= elf1_start <= elf2_end) or (elf2_start <= elf1_end <= elf2_end): # elf1 in elf2 range
            overlaps += 1

    return overlaps

if __name__=="__main__":
    pairs = get_input()

    # print(find_complete_overlap(pairs))
    print(find_some_overlap(pairs))