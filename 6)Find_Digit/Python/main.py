def kayıp_basamak(string):
    for i in range(10):
        c = string.replace("x",str(i))
        x = string.index("=") # it is showing which index


        if eval(c[:x]) == eval(c[x +1:]):
            return str(i)


if __name__ == '__main__':
    print(kayıp_basamak("10 -x =4 "))
    print(kayıp_basamak("1x * 3 = 33"))


