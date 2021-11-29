# This is needed to be done in place.
# Naive solution can be written in runtime of O(m * n)
# A copy of the matrix can be used to write a solution in runtime O(m + n)


def setZeeroes(matrix):

    ROWS, COLS = len(matrix), len(matrix[0])

    isZero = False

    for r in range(ROWS):
        for c in range(COLS):

            if matrix[r][c] == 0:

                # set the first element of that column to 0
                matrix[0][c] = 0

                # set the first element of that row to 0, if the row is above the first row
                if r > 0:
                    matrix[r][0] = 0
                else:
                    isZero = True

    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0

    if isZero:
        for c in range(COLS):
            matrix[0][c] = 0


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

