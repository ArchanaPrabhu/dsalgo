# for loop for every entry, find the other 2 integers from the rest of the array
def find_pair_with_sum(array, sum_for_two):
    new_array = array
    my_set = set(new_array)
    print("%%%", array, my_set)
    for i in array:
        a = i
        b = sum_for_two - i
        print("test", a, b)
        my_set.remove(a)
        if b in my_set:
            print("match", a, b)
            return a, b
        my_set.add(a)
    return None, None


# [3, 7, 1, 2, 8, 4, 5], 21
def solution(array, sum):
    ans = []
    size = len(array)
    for i in range(0, size):
        c = array[i]
        sum_of_pair = sum - array[i]
        new_array = array[0:i] + array[(i + 1):(size)]
        print("***", c, new_array, sum_of_pair)
        a, b = find_pair_with_sum(new_array, sum_of_pair)
        # print(a, b)
        if a is not None and b is not None:
            ans_val = (a, b, c)
            ans.append(ans_val)
            print("###", ans)

    if len(ans) > 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(solution(
        [3, 7, 1, 2, 8, 4, 5], 21))
