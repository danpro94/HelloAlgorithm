# 1부터 5까지의 합을 구하는 알고리즘
## sum1 함수는 문법적 구현에 가까우며 알고리즘과는 거리가 멀다.
# def sum1(n) :
#     sum = 0
#     for i in range(n+1):
#         sum += i
#     return sum

# print(sum1(100))

### 가우스 공식
def sum2(n) :
    return n * (n+1) // 2

print(sum2(10))