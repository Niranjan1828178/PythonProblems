n = int(input('Enter number of participents: '))
arr = list(map(int, input(f'enter {n} scores: ').split(',')))
m=max(arr)
for i in range(arr.count(m)):
    arr.remove(m)
if max(arr):
    print('RunnerUp score is:',max(arr))
else:
    print('No RunnerUp score!')