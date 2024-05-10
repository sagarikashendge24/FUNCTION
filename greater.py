
def a(b):
    i=0
    c=b[0]
    k=[]
    while i<len(b):
        if b[i]<c:
            c=b[i]
        i=i+1
    print(c)    
k=[4,5,6,7,67,8,5,23,6]
a(k)    