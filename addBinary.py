b1,b2=map(str,input('enter b1,b2: ').split(','))
sl,lb1,lb2=0,len(b1),len(b2)
c=0
res=''
if lb1>lb2:
    b2='0'*(lb1-lb2)+b2
    sl=lb1
else:
    b1='0'*(lb2-lb1)+b1
    sl=lb2
for i in range(sl-1,-1,-1):
    if b1[i]=='1':
        if b2[i]=='1':
            if c==1:
                res+='1'
            else:
                res+='0'
                c=1
        else:
            if c==1:
                res+='0'
            else:
                res+='1'
    else:
        if b2[i]=='1':
            if c==1:
                res+='0'
            else:
                res+='1'
        else:
            if c==1:
                res+='1'
                c=0
            else:
                res+='0'
if c==1:
    res+='1'
res=res[::-1]
print('b1 + b2 = ',res)