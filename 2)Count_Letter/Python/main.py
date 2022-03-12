def count_letter(name):
    counts = dict()
    words = []

    for i in name:
        words.append(i)
    # words =['P', 'y', 'c','h', 'a', 'r', 'm','m']

    for word in words:
        if word in counts:
            counts[word] += 1
        else:

            counts[word] = 1

    return counts


if __name__ == '__main__':
    print(count_letter('PyCharmm'))


