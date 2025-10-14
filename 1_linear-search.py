# 선형 방식

## while문 처리
def linear_search(a, val):
    i = 0 #반복하기 위함, 카운터 변수
    while i < len(a):
        if a[i] == val:
            return i #값을 찾으면 리턴
        i+=1
    return -1 ## 값을 못찾으면 리턴

if __name__ == "__main__":
    data = [10, 25, 30, 45, 60, 75]
    target = 45
    result = linear_search(data, target)

    if result != -1:
        print(f"값 {target}는 인덱스 {result}에 있습니다.")
    else:
        print(f"값 {target}는 배열에 존재하지 않습니다.")


## for문 처리
def linear_search1(a, val):
    i = 0 #반복하기 위함, 카운터 변수
    for i in range(a):
        if a[i] == val:
            return i
        i+=1
    return -1

    # while i < 6:
    #     if a[i] == val:
    #         return i #값을 찾으면 리턴
    #     i+=1
    # return -1 ## 값을 못찾으면 리턴

if __name__ == "__main__":
    data = [10, 25, 30, 45, 60, 75]
    target = 45
    result = linear_search(data, target)

    if result != -1:
        print(f"값 {target}는 인덱스 {result}에 있습니다.")
    else:
        print(f"값 {target}는 배열에 존재하지 않습니다.")
