# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-1-i) :
#             if arr[j]<arr[j+1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j] 


# def print_array(arr):
#     print(" ".join(map(str, arr)))


# if __name__ == "__main__":
#     data = [45, 10, 75, 25, 30, 60]

#     print("정렬 전 배열:", end=" ")
#     print_array(data)

#     bubble_sort(data)

#     print("정렬 후 배열:", end=" ")
#     print_array(data)


def bubble_sort_improved(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False 
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                # temp=arr[j] ##다른 문법에서도 사용 가능한 코드
                # arr[j]=temp[j+1]
                # arr[j+1]=temp
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  
            break


def print_array(arr):
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    data = [2, 1, 4, 5 ,3]

    print("정렬 전 배열:", end=" ")
    print_array(data)

    bubble_sort_improved(data)

    print("정렬 후 배열:", end=" ")
    print_array(data)


#목표: 가장 쉽고 간단한 "버블정렬"으로라도 스스로 정렬할 수 있는 개념을 마스터