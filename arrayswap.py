import time


def minimumSwaps(arr):
    # l=arr
    s = 0
    # d=dict(enumerate(arr,1))

    for i in range(len(arr), 1, -1):
        if arr[i-1] != i:
            arr[arr.index(i)] = arr[i-1]
            # for j,k in enumerate(d):
            #     if k==i:
            #         d[j+1]=d[i]
            #         arr[j]=arr[i-1]
            # d.pop(i)
            arr.pop()
            s += 1
        else:
            arr.pop()
    return s


# arr = []
# for i in range(10000):
#     arr.append(i)
arr = list(map(int, input("enter").rstrip().split()))
starttime = time.time()
print(minimumSwaps(arr))
print("execution time:", time.time()-starttime)
