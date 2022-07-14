def compare_point(array1, array2):
    a_point = 0
    b_point = 0

    for i in range(len(array1)):  # use for iterable
        if array1[i] > array2[i]:
            a_point += 1
        else:
            b_point += 1
    return a_point, b_point


if __name__ == '__main__':
    print(compare_point([1, 2, 3, 4], [5, 6, 7, 8])) 
