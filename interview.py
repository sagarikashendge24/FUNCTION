# name =["snowball","chrewy","bubbles","gruff"]
# animal=["cat","dog","fish","goat"]
# age=[1,2,2,6]
# i=0
# while i<len(name):
#     print(name[i],"the",animal[i],"is",age[i])
#     i=i+1


# def expand(a):
#     i=0
#     k=0
#     while i<a:
#         b=(2**k)
#         c=b*a[-i]
#         i=i+1
#     print((c))
# expand(20) 
# def expand(n):
#     rev=0
#     while n>0:
#         reminder=n%10
#         rev=(rev*n)+reminder
#         n=n//10
#     print(rev)
# expand(23)

# def expand(num1):
#     rev= (num%10)
#     rev1= (num//10)
#     print(rev1*10,'+',rev)
        
# num = int(input("Enter the number"))
# expand(num)


# def expand(num):
#     n=num
#     r=num%10
#     k=num//10
#     z=num%100
#     # print(k*10,"+",z,"+",r)
#     print(z*10,"+",r)
# expand(234)

# a=int(input("enter"))
# a=str(a)
# if len(a)==1:
#     print("1")
# elif len(a)==2:
#     print("2")    
# elif len(a)==3:
#     print()    



# def expand(num):
#     result=[]
#     for index,digit, in enumerate(str(num))[::-1]:
#         if int(digit)!=0:
#             result.append(digit +('0'*index))
#         return '+'.join(result[::-1])    
# expand(2345)        


# def function(num):
#     digits = str(num) # convert number to string
#     output = []
#     for i, digit in enumerate(digits):
#         output.append("(" + digit + "x10^" + str(len(digits)-i-1) + ")")
#         return " + ".join(output)
# print(function(1234))

def expand(num):
    a=str(num)
    c=len(a)-1
    print(c)
    # i=0
    # while i<num:
expand(234)        

