class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


def linear_search(items, val):
    for  ■■■■■■:
        if  ■■■■■■:  
            return i
    return -1


if __name__ == "__main__":
    data = [
        Item("apple", 1000),
        Item("banana", 1200),
        Item("cherry", 3000),
        Item("date", 2500),
        Item("fig", 1800),
        Item("grape", 2200),
    ]

    target = "cherry"
    result = linear_search(data, target)

    if result != -1:
        print(f"'{target}'는 인덱스 {result}에 있으며, 가격은 {data[result].price}원입니다.")
    else:
        print(f"'{target}'는 배열에 존재하지 않습니다.")