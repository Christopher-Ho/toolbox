"""
Notes: Space complexity is O(1)
"""


def binary_search(list, target):
    """
    :param sortedList:
    :param target:
    :return: index position of the target if found, else returns None
    """
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        elif list[midpoint] > target:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = binary_search(numbers, 9)
    verify(result)


if __name__ == "__main__":
    main()

