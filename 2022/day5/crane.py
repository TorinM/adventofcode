def get_input():
    f = open("in.txt", "r")

    stacks = {}
    procedures = [] # __ crates from __ to __
    for line in f.readlines():
        if "[" in line:
            # lines are broken into chunks of 4
            line_length = len(line)
            stack_ptr = 1   
            for chunk_start in range(0, line_length, 4):
                if line[chunk_start] == "[": # is box
                    if stack_ptr in stacks:
                        stacks[stack_ptr].append(line[chunk_start+1])
                    else:
                        stacks[stack_ptr] = [line[chunk_start+1]]

                stack_ptr += 1

        elif line.startswith("move"): # is procedure line
            procedure = []

            prev = ""
            for c in line:
                if c.isdigit():
                    if prev.isdigit():
                        procedure[-1] += c
                    else:
                        procedure.append(c) 

                prev = c

            int_proc = [int(p) for p in procedure]
            procedures.append(int_proc.copy())

    f.close()

    return stacks, procedures


def execute_procedures(stacks, procedures):
    new_stacks = stacks.copy() # potentially just do in place

    for proc in procedures:
        num_crates = proc[0]
        from_stack = proc[1]
        to_stack = proc[2]

        new_stacks[to_stack].extend(new_stacks[from_stack][num_crates:])
        new_stacks[from_stack] = new_stacks[from_stack][-num_crates:]

        print(new_stacks)

    return new_stacks


if __name__=="__main__":
    stacks, procedures = get_input()

    new_stacks = execute_procedures(stacks, procedures)

    for stack in sorted(new_stacks.keys()): # print the top of each stack in order
        print(new_stacks[stack][0], end="")

    print("")
