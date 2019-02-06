import sys


def binary_search(arr, num):
    lb = 0
    ub = len(arr) - 1
    if arr[lb] == num:
        return True
    if arr[ub] == num:
        return True

    while lb <= ub:
        mid = (lb + ub) / 2
        if arr[mid] == num:
            return True
        elif arr[mid] > num:
            ub = mid - 1
        else:
            lb = mid + 1
    return False


if __name__ == '__main__':
    num = int(sys.argv[1])
    arr = [1, 2, 3, 5, 6, 8, 23, 45, 67, 69]
    found = binary_search(arr, num)
    if found:
        print("found element")
    else:
        print("Not found")
