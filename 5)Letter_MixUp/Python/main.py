def kelime_karistirma(name1,name2):
    if len(name1) == len(name2):
        for i in name1:
            if i in name2:
                return True
    else:
        return False


if __name__ == '__main__':
    print(kelime_karistirma('Sumeyra','meyaruS'))


