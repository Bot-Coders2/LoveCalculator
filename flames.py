def flames(s1,s2):
    s1=(s1.upper())
    s2=(s1.upper())
    p=len(s1)+len(s2)
    l=['F','L','A','M','E','S']
    for i in range(len(s1)):
        c=s1[i]
        if(c in s2):
            s1=s1.replace(c,'*',1)
            s2=s2.replace(c,'*',1)
            p-=2
    while(len(l)!=1):
        e=(l[(p-1)%(len(l))])
        l=l[(p-1)%(len(l))+1:]+l[:(p-1)%(len(l))]
    return(l[0])
