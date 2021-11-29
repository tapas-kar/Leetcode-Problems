def climbingStais(n):

    steps = {1:1, 2:2, 3:3}

    for i in range(4, n+1):

        steps[i] = steps[i-1] + steps[i-2]

    print(steps[n])

    return steps[n]


n = 4

climbingStais(n)