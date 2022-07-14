def sum_array(name):
    sum = 0
    for i in name:
        sum += i
    return sum


if __name__ == '__main__':
    print(sum_array([1, 2, 3, 4]))
