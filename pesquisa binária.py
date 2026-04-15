def pb(l,i):
    b = 0
    a = len(l)-1
    while b<=a:
        m = (b+a)//2
        c = l[m]
        if c==i:
            return m
        if c>i:
            a = m-1
        else:
            b = m+1
    return None
ml = [1,3,5,7,9]
print(pb(ml,1))
print(pb(ml,9))