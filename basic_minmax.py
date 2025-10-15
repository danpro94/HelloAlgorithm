def max(data):
    n = range(data)
    i = 0
    max = 0
    for i in n-1:
        for j in data[n+j]:
            if data[i] > data[i+j]:
                max = data[i]
                

def min(data):
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j 


if __name__ == "__main__":
    data = [10, 25, 30, 45, 60, 75] 
    
    print("가장 큰 값: ",max(data))
    print("가장 작은 값: ",min(data))