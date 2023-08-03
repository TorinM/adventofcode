def get_input():
    f = open("in.txt", "r")

    cal_total = 0
    calories = []
    for line in f.readlines():
        if line == "\n" or "":
            calories.append(cal_total)
            cal_total = 0
        else:
            cal_total += int(line)

    f.close()
    return calories

if __name__=="__main__":
    calories = get_input()

    # print(max(calories)) # part 1
    
    # part 2
    calories.sort()
    print(sum(calories[-3:]))
