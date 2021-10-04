def linear_search(list, target):
    """
    :param list:
    :param target:
    :return: intex position of the target if found, else returns None

    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = linear_search(numbers, 12)
    verify(result)


if __name__ == "__main__":
    main()
