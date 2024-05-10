a=[
    [8,3,4],
    [1,5,9],
    [6,7,2]
]
b=len(a)
row1,row2,row3,col1,col2,col3,dia1,dia2=0,0,0,0,0,0,0,0
i=0
while i<b:
    c=len(a[i])
    j=0
    while j<c:
        if i==0:
            row1=row1+a[i][j]
            col1=col1+a[j][i]
        elif i==1:
            row2=row2+a[i][j]
            col2=col2+a[j][i]
        else:
            row3=row3+a[i][j]
            col3=col3+a[j][i]
        j=j+1            
    i=i+1
m=0
k=2
while m<c:
    dia1=dia1 + a [m][m] 
    dia2 = dia2 + a [m][m]
    m=m+1
    k=k+1
if row1==row2==row3==col1==col2==col3==dia1==dia2:
    print("IT IS A MAGIC SQUARE")
else:
    print("IT IS NOT A MAGIC SQUARE")               