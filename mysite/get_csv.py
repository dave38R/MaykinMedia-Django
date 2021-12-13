# this code was inspired from this website :
# https://www.geeksforgeeks.org/working-csv-files-python/

import csv

filenames = ["hotel.csv", "city.csv"]
# the _h indicates the hotel database, _c indicates the city database
codes_h = []  # The 'codes' are the initials like 'AMS' for Amsterdam or 'BER' for Berlin, they are the same as codes_c
ide_h = []  # The 'ide' are composed of the codes and a number, no 2 hotels have the same so they are the hotel ID's
names_h = []  # Simply the name of the hotels
codes_c = []  # Same as codes_h (ex: AMS for Amsterdam)
names_c = []  # The city names (ex: Amsterdam)

for file in filenames:
    rows = []
    with open(file, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile, delimiter=';', lineterminator='\n\n')

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
        if file == "hotel.csv":
            for row in rows:
                codes_h.append(row[0])
                ide_h.append(row[1])
                names_h.append(row[2])
        if file == "city.csv":
            for row in rows:
                codes_c.append(row[0])
                names_c.append(row[1])

# We save that information into arrays so that it is easier to access
hotel = [codes_h, ide_h, names_h]
city = [codes_c, names_c]


# In the models, I ordered the hotel class to be linked to the city class. Therefore, to create a hotel instance using
# the hotel and city list, I need a function to take as input a city code and output a City instance.

# The list of City instances is called Cities. Right now the way I do it is by opening the shell of manage.py and
# plugging in: "from hotelManager.models import City \n Cities = City.objects.all()

def funcity(Cities, code_name):
    for City in Cities:
        if City.code_name == code_name:
            return City
