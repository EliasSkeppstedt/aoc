def insert_sorted(list, num, low, high):
    if low >= high:
        if num < list[low]:
            insert(list, low, num)
        else:
            insert(list, low + 1, num)
        return

    mid = (low + high) // 2
    
    if num > list[mid]:
        insert_sorted(list, num, mid+1, high)
    else:
        insert_sorted(list, num, low, mid)

def insert(list, low, num): # list.insert()
    for i in range(low, len(list)):
        tmp = list[i]
        list[i] = num
        num = tmp
    list.append(num)

def load_column_lists(file_name, left, right):
    with open(file_name, "r") as file:
        pair =  file.readline().split()
        left.append(int(pair[0]))
        right.append(int(pair[1]))

        for line in file:
            pair =  line.split()
            insert_sorted(left, int(pair[0]), 0, len(left) - 1)
            insert_sorted(right, int(pair[1]), 0, len(right) - 1)

def distance(left_num, right_num):
    return abs(left_num - right_num)

def part1():
    left = []
    right = []
    answer = 0

    load_column_lists("data.txt", left, right)

    for i in range(0, len(left)):
        answer += distance(left[i], right[i])

    print("Total distance: ", answer)

def part2():
    left = []
    right = []
    answer = 0

    load_column_lists("data.txt", left, right)

    similarity = 0

    length = len(left)

    for i in range(0, length):
        multiplier = 0
        for j in range(0, length):
            if left[i] < right[j]:
                break
            elif left[i] == right[j]:
                multiplier += 1
        similarity += left[i] * multiplier

    print("Total distance: ", similarity)

part1()
part2()