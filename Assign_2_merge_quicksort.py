
#########  MERGE SORT  #########
def mergeSort(arr, s, e):
    if s==e:
        return
    
    mid=(s+e)//2
    mergeSort(arr, s, mid)
    mergeSort(arr, mid+1, e)

    #Create two subparts of main array 
    left=arr[s:mid+1]
    right=arr[mid+1:e+1]

    i, j, k = 0, 0, s

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
            k+=1
        elif left[i]>right[j]:
            arr[k]=right[j]
            j+=1
            k+=1

    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1




########    QUICK SORT     ########

def partition(arr, s, e):
    #suppose pivote element is arr[s]
    pivot=arr[s]
    cnt=0                               #count to store no. of numbers less than pivot element
    for i in range(s+1, e+1):
        if arr[i]<=pivot:
            cnt+=1

    pivotIndex=s+cnt
    #putting pivote element at pivote index
    arr[s], arr[pivotIndex]=arr[pivotIndex], arr[s]

    # making all elements left to pivot element are less and all elements right to it are greater
    i, j=s, e
    while i<pivotIndex and j>pivotIndex:
        while i<pivotIndex and arr[i]<=pivot:
            i+=1
        while j>pivotIndex and arr[j]>=pivot:
            j-=1
        if i<pivotIndex and j>pivotIndex:
            arr[i], arr[j]=arr[j], arr[i]
            i+=1
            j-=1

    return pivotIndex

def quickSort(arr, s, e):
    #base condition
    if s>=e:
        return
    
    #Index of pivot element
    p=partition(arr, s, e)

    #recursively sorting left part
    quickSort(arr, s, p-1)

    #recursively sorting right part
    quickSort(arr, p+1, e)


#Function call
# arr1=[99, 23, 45, 12, 34, 9, 89]
# quickSort(arr1, 0, len(arr1)-1)
# print(arr1)

# arr2=[99, 0, 15, -12, 17, 49, 46, 39]
# mergeSort(arr2, 0, len(arr2))
# print(arr2)

size=int(input("Enter the size of array:"))
arr=[]
for i in range(size):
    x=int(input("enter the element: "))
    arr.append(x)

quickSort(arr, 0, size-1)
print(arr)

