# You come across a dictionary of sorted words in a language you've never seen before.
# Write a program that returns the correct order of letters in this language.
#
# For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'],
# you should return ['x', 'z', 'w', 'y'].

def solution():
    matrix = ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']
    ans = []

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if (matrix[i])


def compareStringAndUpdate(first, second, stack):
    window = 0
    if len(first) > len(second):
        window = first
    else:
        window = second

    for i in range(first):


if __name__ == "__main__":
    solution()