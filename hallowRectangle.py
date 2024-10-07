def draw_rectangle(l,b):
    for i in range(b):
        for j in range(l):
            if i==0 or i==b-1 or j==0 or j==l-1:
                print('* ',end='')
            else:
                print('  ',end='')
        print()

l,b=map(int,input('enter l,b: ').split(','))
draw_rectangle(l,b)