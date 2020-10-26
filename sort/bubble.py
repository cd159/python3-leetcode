# import range
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr


def bubbleSort2(arr: list, reverse=True):
    for i in range(1, len(arr)):
        # 冒泡排序还有一种优化算法，就是立一个 flag，当在一趟序列遍历中元素没有发生交换，则证明该序列已经有序
        flag = 0
        for j in range(0, len(arr)-i):
            # 升序
            if reverse:
                if arr[j] < arr[j+1]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]
                    flag = 1
            # 降序
            else:
                if arr[j] > arr[j+1]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]
        if flag == 0:
            return arr
    return arr

if __name__ == '__main__':
    list = [1, 5, 8, 123, 22, 54, 7, 99, 300, 222]
    print("List source is:", list)
    result = bubbleSort2(list)
    print("List sort is:", result)