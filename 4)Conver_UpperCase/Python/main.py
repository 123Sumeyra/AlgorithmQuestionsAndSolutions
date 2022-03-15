# first option


# def bas_harf_buyut(name):
#     new_word =""
#     for i in name.split(' '):
#         new_word += i.capitalize() + " "
#
#     return new_word


# Second option is
def bas_harf_buyut(name):
    words = name.split() # ['Kod', 'yazmak', 'musik', 'aleti', 'çalmak', 'gibi']
    for i in range(0,len(words)):
        words[i] = words[i][0].upper() + words[i][1::]
    return " ".join(words)  # Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'





if __name__ == '__main__':
   print(bas_harf_buyut('Kod yazmak musik aleti çalmak gibi'))
