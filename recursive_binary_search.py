"""
Notes: Space complexity is O(log n)
"""


def recursive_binary_search(list, target):
    """
    :param list:
    :param target:
    :return: true if target found, else returns false
    """
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print("Target found: ", result)


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = recursive_binary_search(numbers, 4)
    verify(result)


if __name__ == "__main__":
    main()