temp = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

pos_temp = filter(lambda x: x[1] > 0,temp.items())

for i in pos_temp:
    print(i[0])