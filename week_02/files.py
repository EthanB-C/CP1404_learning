guitar_deets = open("guitardata.txt", "r")
for line in guitar_deets:
    guitar_deets_line = line.split(",")
    print("Guitar: {}\nYear: {:}\nPrice: ${}".format(guitar_deets_line[0], guitar_deets_line[1], guitar_deets_line[2]))
guitar_deets.close()
