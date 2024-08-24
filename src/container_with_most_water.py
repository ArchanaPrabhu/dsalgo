# 2, 8, 6, 3, 5, 4, 7
# 7, 7, 2
# 1, 5

# solution([1, 8, 6, 2, 5, 4, 8, 3, 7])

def calculate_volume(left_ind, right_ind, array):
    width = right_ind - left_ind
    height = min(array[left_ind], array[right_ind])
    print(left_ind, array[left_ind], right_ind, array[right_ind])
    print(width, height)
    return width * height


def solution(array):
    left = 0
    right = len(array) - 1
    left_max = -1
    right_max = -1
    max_vol = 0
    while left < right:
        print(left, right)
        print(left_max, right_max)
        vol = calculate_volume(left, right, array)
        if vol > max_vol:
            max_vol = vol
        left += 1
        right -= 1
        print("***")
    return max_vol


if __name__ == "__main__":
    print(solution([1, 8, 6, 2, 5, 4, 8, 3, 7]))
