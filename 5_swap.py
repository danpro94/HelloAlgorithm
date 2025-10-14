# 스왑: 두 변수의 값을 교환하는 알고리즘
num1 = 10
num2 = 5
print(num1, num2)

# 파이썬 문법
num1, num2 = num2, num1
print(num1, num2)

# 알고리즘
def swap(n1, n2):
    temp = 0
    temp = n1
    n1 = n2
    n2 = temp
    return n1, n2

print(swap(10,5))