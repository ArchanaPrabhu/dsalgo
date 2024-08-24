# How to set up two pointers in an array

def two_pointers(array):
    left = 0
    right = len(array) - 1

    while left <= right:
        if array[left] != array[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(two_pointers(list("aba")))
