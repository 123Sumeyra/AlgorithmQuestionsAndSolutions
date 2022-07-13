def check_duplicate(name):

    for i in range(len(name)):
        for j in range(len(name)):

            if name[i] == name[j] and i != j:
                return True


if __name__ == '__main__':
    if check_duplicate([1, 2, 3, 4,4]):
        print("Duplicated")
    else:
        print("Not Duplicated")


