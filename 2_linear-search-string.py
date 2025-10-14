# def linear_search(a, val):
#     for i in range(len(a)):
#         if a[i] == val:
#             return i
#     return -1

# if __name__ == "__main__":
#     data = ["apple", "banana", "cherry", "date", "fig", "grape"]
#     target = "cherry"
#     result = linear_search(data, target)

#     if result != -1:
#         print(f'문자열 "{target}"는 인덱스 {result}에 있습니다.')
#     else:
#         print(f'문자열 "{target}"는 배열에 존재하지 않습니다.')


def linear_search(a, val):
    for i in range(len(a)):
        if a[i].lower() == val.lower():
                return i
    return -1

if __name__ == "__main__":
    data = ["apple", "banana", "cherry", "date", "fig", "grape"]
    target = "cherry"
    result = linear_search(data, target)

    if result != -1:
        print(f'문자열 "{target}"는 인덱스 {result}에 있습니다.')
    else:
        print(f'문자열 "{target}"는 배열에 존재하지 않습니다.')