import math

#Digit Generation from the positive integer
n=57
digits=[int(x) for x in str(n)]
#print(digits)

#Number Series generation starting from 1
def generateNumber(num):
    mylist = []
    for i in range(num+1):
         mylist.append(i)
    return mylist
x = generateNumber(len(digits))
del x[0]
#print(x)

#Matrix Multiplication of both arrays
res_list=[]
for i in range (0, len(digits)):
    res_list.append(digits[i]*x[i])
    
#def multiplyList(list):
#    result=1
#    for x in list:
#        result=result*x
#    return result

weighted_sum=sum(res_list)
print(weighted_sum)
