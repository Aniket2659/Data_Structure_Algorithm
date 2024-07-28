def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        flag=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=True
        if not flag:
            break
    return arr

arr=[25,36,48,9,12,74,29]
print(bubble_sort(arr))