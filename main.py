import random


def binary_search(data, target, low, high):
    if low > high:
        return False

    mid = (low + high) // 2

    if data[mid] == target:
        return True
    elif data[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

    return binary_search(data, target, low, high)


def binary_search_loop(data, target, low, high):
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False


if __name__ == '__main__':
    data = sorted([random.randint(0, 100) for i in range(10)])

    print(data)

    target = int(input('What number would you like to find? '))

    found = binary_search_loop(data, target, 0, len(data) - 1)

    print(found)