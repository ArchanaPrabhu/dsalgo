def solution(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
      L     R
    T 1 2 3 4

    B
    """
    ans = []
    top, bottom = 0, len(matrix)
    left, right = 0, len(matrix[0])

    while left < right and top < bottom:
        # go left to right
        for i in range(left, right):
            ans.append(matrix[top][i])
        top = top + 1

        # go top to bottom
        for i in range(top, bottom):
            ans.append(matrix[i][right - 1])
        right = right - 1

        # this needs to be done to check the cases for the single column or single row matrix
        if not (left < right and top < bottom):
            break

        # go from right to left
        for i in range(right - 1, left - 1, -1):
            ans.append(matrix[bottom - 1][i])
        bottom = bottom - 1

        for i in range(bottom - 1, top - 1, -1):
            ans.append(matrix[i][left])
        left = left + 1

    return ans


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [12, 13, 14, 5],
              [11, 16, 15, 6],
              [10, 9, 8, 7]]
    print(solution(matrix))
