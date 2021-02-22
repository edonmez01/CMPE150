evidences = []
with open('crime_scene.txt', 'r') as file:
    maxW, totalT = (int(i) for i in file.readline().split())
    N = int(file.readline())
    for _ in range(N):
        evidences.append(tuple(int(i) for i in file.readline().split()))


def qsort(lst, lo, hi):
    if lo < hi:
        pivot = lst[lo]
        swap_index = lo + 1
        for i in range(lo + 1, hi + 1):
            if lst[i] < pivot:
                lst[i], lst[swap_index] = lst[swap_index], lst[i]
                swap_index += 1
        lst[lo], lst[swap_index - 1] = lst[swap_index - 1], lst[lo]

        qsort(lst, lo, swap_index - 2)
        qsort(lst, swap_index, hi)


def knapsack_weight(lst, curr_weight=0, curr_val=0, curr_pack=[]):
    if not lst:
        return curr_val, curr_pack

    elem_id, weight, time, value = lst[0]
    if curr_weight + weight > maxW:
        return knapsack_weight(lst[1:], curr_weight, curr_val, curr_pack)
    return max(knapsack_weight(lst[1:], curr_weight, curr_val, curr_pack), knapsack_weight(lst[1:], curr_weight + weight, curr_val + value, curr_pack + [elem_id]))


def knapsack_time(lst, curr_time=0, curr_val=0, curr_pack=[]):
    if not lst:
        return curr_val, curr_pack

    elem_id, weight, time, value = lst[0]
    if curr_time + time > totalT:
        return knapsack_time(lst[1:], curr_time, curr_val, curr_pack)
    return max(knapsack_time(lst[1:], curr_time, curr_val, curr_pack), knapsack_time(lst[1:], curr_time + time, curr_val + value, curr_pack + [elem_id]))


def knapsack_final(lst, curr_weight=0, curr_time=0, curr_val=0, curr_pack=[]):
    if not lst:
        return curr_val, curr_pack

    elem_id, weight, time, value = lst[0]
    if curr_weight + weight > maxW or curr_time + time > totalT:
        return knapsack_final(lst[1:], curr_weight, curr_time, curr_val, curr_pack)
    return max(knapsack_final(lst[1:], curr_weight, curr_time, curr_val, curr_pack), knapsack_final(lst[1:], curr_weight + weight, curr_time + time, curr_val + value, curr_pack + [elem_id]))


with open('solution_part1.txt', 'w') as file:
    outVal, outLst = knapsack_weight(evidences)
    qsort(outLst, 0, len(outLst) - 1)
    file.write(str(outVal) + '\n')
    file.write(' '.join(str(i) for i in outLst))

with open('solution_part2.txt', 'w') as file:
    outVal, outLst = knapsack_time(evidences)
    qsort(outLst, 0, len(outLst) - 1)
    file.write(str(outVal) + '\n')
    file.write(' '.join(str(i) for i in outLst))

with open('solution_part3.txt', 'w') as file:
    outVal, outLst = knapsack_final(evidences)
    qsort(outLst, 0, len(outLst) - 1)
    file.write(str(outVal) + '\n')
    file.write(' '.join(str(i) for i in outLst))

