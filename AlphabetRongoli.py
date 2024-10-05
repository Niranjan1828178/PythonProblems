size=int(input('enter the size: '))
st=''

l=(size*2)-1
for i in range(int(l/2)+1):
    st=''
    let=96+size
    st+=f"{'--'*(size-i-1)}"
    for j in range(i+1):
        st+=f"{chr(let)}-"
        let-=1
    let+=2
    for j in range(i):
        st+=f"{chr(let)}-"
        let+=1
    st=st[:-1]
    st+=f"{'--'*(size-i-1)}"
    print(st)
for i in range(int(l/2)):
    st=''
    let=96+size
    st+=f"{'--'*(i+1)}"
    for j in range(int(l/2)-i):
        st+=f"{chr(let)}-"
        let-=1
    let+=2
    for j in range(int(l/2)-i-1):
        st+=f"{chr(let)}-"
        let+=1
    st=st[:-1]
    st+=f"{'--'*(i+1)}"
    print(st)
    