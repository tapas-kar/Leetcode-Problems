def insert(intervals, newInterval):

    # starts = []
    #
    # ends = []
    #
    # for i in range(len(intervals)):
    #
    #     starts.append(intervals[i][0])
    #
    #     ends.append(intervals[i][1])
    #
    # # print(starts)
    # # print(ends)
    # print(intervals)
    # print(newInterval)

    # interval comparison and merge method
    # def intervalcomparison(interI, interNew):
    #
    #     inter = []
    #
    #     if interI[1] >= interNew[0]:
    #
    #         inter.append([interI[0], interNew[1]])
    #
    #     return inter
    #
    # print(intervalcomparison([1, 3], [2, 5]))
    #
    # for i in range(len(intervals)):
    #
    #     if intervalcomparison(intervals[i], newInterval):
    #         intervals[i] = intervalcomparison(intervals[i], newInterval)
    #         print(intervals)
    #         return intervals

    s, e = newInterval

    left, right = [], []

    for a, b in intervals:

        if b < s:
            left += [[a, b]]
        elif e < a:
            right += [[a, b]]
        else:
            s = min(a, s)
            e = max(e, b)

    return left + [[s, e]] + right


intervals = [[1, 3], [6, 9]]

newInterval = [2, 5]

insert(intervals, newInterval)
