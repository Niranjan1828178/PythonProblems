# climbing steps 
# enter the number of steps to climb: 4
# possiblities are:
# [1, 1, 1, 1]
# [1, 1, 2]
# [1, 2, 1]
# [2, 1, 1]
# [2, 2]
def possible(n,combinations=[]):
    if n==0:
        print(combinations)
    if n>=1:
        possible(n-1,combinations+[1])
    if n>=2:
        possible(n-2,combinations+[2])

n=int(input('enter the number of steps to climb: '))
possible(n)