def is_valid(s):
    op,cp='([{',')]}'
    st=''
    for i in s:
        if i in op:
            st+=i
        elif not st=='' and i==cp[op.index(st[-1])]:
            st=st[:-1]
        else:
            return False
    if st=='':
        return True
    else:
        return False

s=input('enter the parentheses: ')

if is_valid(s):
    print('The parentheses are valid.')
else:
    print('The parentheses are invalid.')