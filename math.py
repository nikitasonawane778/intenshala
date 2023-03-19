
def filterX(list1):
    list2 = []

    for i in list1:
        if i == 2:
            list2.append(i)
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                list2.append(i)
                break
    return list2


def mapX(list2):
    list3 = []
    for i in list2:
        ans = i * 2
        list3.append(ans)
    return list3


def reduceX(list3):
    mValue = 0
    for i in list3:
        if i > mValue:
            mValue = i

    return mValue


def main():
    num = int(input("enter the number :"))
    list1 = []
    print("Entering the numbers ")

    for i in range(0, num, 1):
        value = int(input())
        list1.append(value)
    print("Data is :", list1)

    filter_result = filterX(list1)
    print("filter result ", filter_result)

    map_result = mapX(filter_result)
    print("map result ", map_result)

    reduce_result = reduceX(map_result)
    print("reduce result ", reduce_result)


if __name__ == "__main__":
    main()
