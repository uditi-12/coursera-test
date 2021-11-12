def problem2_8(l):
    s=0
    for i in l:
        s+=i
    s/=len(l)
    print("Average:",s)
    print("High:",max(l))
    print("Low:",min(l))

