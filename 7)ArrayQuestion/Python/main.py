def print_solved(number):
    first_number = number[0] #4
    number = number[first_number:] + number[:first_number]
    return number


if __name__ == '__main__':
    print(print_solved([4,5,6,7,8,9,10])) #[8, 9, 10, 4, 5, 6, 7]


