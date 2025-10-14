def binary_search(a, val):
    first = 0
    last =  len(a)

    while first <= last:
        mid =  int(last/2)
        
        if  a[mid] == val:
            return mid
        elif  a[mid] != val:
            last = mid - 1
        else:
            first = mid + 1

    return -1


if __name__ == "__main__":
    data = [10, 25, 30, 45, 60, 75] 
    target = 45
    result = binary_search(data, target)

    if result != -1:
        print(f"값 {target}는 인덱스 {result}에 있습니다.")
    else:
        print(f"값 {target}는 배열에 존재하지 않습니다.")
