def draw_hallow_rectangle(l,b):
    for i in range(b):
        for j in range(l):
            if i==0 or i==b-1 or j==0 or j==l-1:
                print('* ',end='')
            else:
                print('  ',end='')
        print()

def draw_rectangle(l,b):
    for i in range(b):
        print(f'{'* '*l}')
    print()

def draw_right_solid_triangle(n):
    for i in range(n):
        print('* '*(i+1))
    print()

def draw_right_hallow_triangle(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j or j==1 or i==n:
                print('* ',end='')
            else:
                print('  ',end='')
        print()

def draw_left_solid_triangle(n):
    for i in range(n):
        print('  '*(n-i-1) + '* '*(i+1))
    print()

def draw_left_hallow_triangle(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i+j==n+1 or j==n or i==n:
                print('* ',end='')
            else:
                print('  ',end='')
        print()

def draw_prymid(n):
    for i in range(n):
        print(' '*(n-i-1) + '*'*((2*i)+1))
    print()

def draw_hallow_prymid(n):
    for i in range(1,n+1):
        for j in range(1,n*2):
            if i+j==n+1 or j-i==n-1 or i==n:
                print('*',end='')
            else:
                print(' ',end='')
        print()



while True:
    print('1:hallow rectangle')
    print('2:solid rectangle')
    print('3:solid rightangled triangle')
    print('4:solid left rightangled triangle')
    print('5:solid prymid')
    print('6:hallow prymid')
    print('7:hallow rightangled triangle')
    print('8:hallow left rightangled triangle')
    print('9:exit')
    pet=int(input('enter your choice: '))
    if pet==1:
        l,b=map(int,input('enter l,b for hallow rectangle : ').split(','))
        draw_hallow_rectangle(l,b)
    elif pet==2:
        l,b=map(int,input('enter l,b for solid rectangle : ').split(','))
        draw_rectangle(l,b)
    elif pet==3:
        n=int(input('enter n for solid right angled triangle : '))
        draw_right_solid_triangle(n)
    elif pet==4:
        n=int(input('enter n for solid left angled triangle : '))
        draw_left_solid_triangle(n)
    elif pet==5:
        n=int(input('enter n for solid prymid : '))
        draw_prymid(n)
    elif pet==6:
        n=int(input('enter n for hallow prymid : '))
        draw_hallow_prymid(n)
    elif pet==7:
        n=int(input('enter n for hallow Right sided triangle : '))
        draw_right_hallow_triangle(n)
    elif pet==8:
        n=int(input('enter n for hallow left sided triangle : '))
        draw_left_hallow_triangle(n)
    elif pet==9:
        exit('thank you for using!')
            