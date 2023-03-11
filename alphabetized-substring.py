string=str(input())

#def isInAlphabeticalOrder(word):
#    return all((word[i+1] >= word[i] for i in range(len(word) - 1)))
#isInAlphabeticalOrder(string)
print(string)
l=list(string)
print(l)

def alphabetical(word):
    return list(word) == sorted(word)

print(alphabetical(string))

#Function to a split an array of alphabets
def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
        
        arr[n-1] = x
###
arr=l
n=len(l)
position=2


