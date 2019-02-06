import sys


def linear_search(num, arr):
    for i in range(len(arr)):
        if int(num) == arr[i]:
            return True
    return False


if __name__ == '__main__':
    num = sys.argv[1]
    print("search number is {}".format(num))
    arr = [5, 3, 2, 3, 4, 5, 5]
    found = linear_search(num, arr)
    if found:
        print("Found")
    else:
        print("Not found")
