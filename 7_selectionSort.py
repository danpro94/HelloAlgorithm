# 선택 정렬

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i  # 현재 위치를 가장 작은 값이라 가정
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j 
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]  


def print_array(arr):
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    data = [3, 5, 4, 2, 1]

    print("정렬 전 배열:", end=" ")
    print_array(data)

    selection_sort(data)

    print("정렬 후 배열:", end=" ")
    print_array(data)


## [개선] 이중 선택 정렬 (최댓값도 함께 정렬)
def double_selection_sort(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        min_index = ■■■■■■
        max_index = ■■■■■■

        for i in ■■■■■■:
            if ■■■■■■:
                min_index = i
            if ■■■■■■:
                max_index = i

        if ■■■■■■:
            arr[left], arr[min_index] = arr[min_index], arr[left]

            if ■■■■■■:
                max_index = min_index

        if ■■■■■■:
            arr[right], arr[max_index] = arr[max_index], arr[right]

        left ■■■■■■
        right ■■■■■■


def print_array(arr):
    print(" ".join(map(str, arr)))


if __name__ == "__main__":
    data = [3, 5, 4, 2, 1]

    print("정렬 전 배열:", end=" ")
    print_array(data)

    double_selection_sort(data)

    print("정렬 후 배열:", end=" ")
    print_array(data)

