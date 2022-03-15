

def convert_time(saat):
    hour = saat // 60
    minute = saat % 60
    return str(hour)+ " saat " + str(minute)+ " dk"


if __name__ == '__main__':
   print(convert_time(58))

