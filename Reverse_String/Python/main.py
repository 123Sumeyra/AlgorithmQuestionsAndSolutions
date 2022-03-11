# First way
def ters_cevir(isim):
    isim = isim[::-1]
    print(isim)


#Second way
def reverse_name(name):
    new_name = ""
    i = 1

    while i <= (len(name)):
        new_name += (name[-i])
        i += 1
    print(new_name)


if __name__ == '__main__':
    reverse_name('Sumeyra')
    ters_cevir("Sümeyra")
