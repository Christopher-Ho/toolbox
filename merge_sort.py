def merge_sort(list):
    """
    Sorts a list in ascending order
    Takes O(n log n) time to run
    Takes O(n) space complexity
    :param list: to be sorted
    :return: a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Consquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divide the unsorted list at midpoitn into sublists
    Takes overall O(log n) time
    :param list:
    :return: two sublists - left and right
    """

    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merge ltwo lists(arrays), sorting them in the process
    Runs in overall O(n) time
    :param left:
    :param right:
    :return: a new merged list
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])


def main():
    alist = [54, 62, 93, 17, 77, 31, 44, 55, 20]
    l = merge_sort(alist)
    print(verify_sorted(alist))
    print(verify_sorted(l))


if __name__ == "__main__":
    main()