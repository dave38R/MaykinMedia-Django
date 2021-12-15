import requests
import csv

# Requests will use the username and password to connect to the website and get the data
auth = ('python-demo', 'claw30_bumps')

# This will return an object from which we extract the text
city_csv = requests.get("http://rachel.maykinmedia.nl/djangocase/city.csv", auth=auth).text
hotel_csv = requests.get("http://rachel.maykinmedia.nl/djangocase/hotel.csv", auth=auth).text

# We want to erase our files in case they already contain old data, so that we only have new data
open('city.txt', 'w').close()
open('hotel.txt', 'w').close()

# We put the new data in our files
with open('city.txt', 'w') as output_file:
    for letter in city_csv:
        output_file.write(letter)

with open('hotel.txt', 'w') as output_file:
    for letter in hotel_csv:
        output_file.write(letter)
# Now we have the csv files (or rather the text files) that contain the whole data from the website

# We want to get the data under lists to use them with Django
filenames = ["hotel.txt", "city.txt"]

# the _h indicates the hotel database, _c indicates the city database
codes_h = []  # The 'codes' are the initials like 'AMS' for Amsterdam or 'BER' for Berlin, they are the same as codes_c
ide_h = []  # The 'ide' are composed of the codes and a number, no 2 hotels have the same so they are the hotel ID's
names_h = []  # Simply the name of the hotels
codes_c = []  # Same as codes_h (ex: AMS for Amsterdam)
names_c = []  # The city names (ex: Amsterdam)

# This puts the data in the respective lists
for file in filenames:
    rows = []
    with open(file, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile, delimiter=';', lineterminator='\n\n')

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
        if file == "hotel.txt":
            for row in rows:
                codes_h.append(row[0])
                ide_h.append(row[1])
                names_h.append(row[2])
        if file == "city.txt":
            for row in rows:
                codes_c.append(row[0])
                names_c.append(row[1])

# We can test this program by uncommenting this part, you can check that everything was imported correctly
# print('codes_h', codes_h)
# print('ide_h', ide_h)
# print('names_h', names_h)
# print('codes_c', codes_c)
# print('names_c', names_c)

hotels = [codes_h, ide_h, names_h]
cities = [names_c, codes_c]

# In the models, I ordered the hotel class to be linked to the city class. Therefore, to create a hotel instance using
# the hotel and city list, I need a function to take as input a city code and output a City instance.

# The list of City instances is called Cities. Right now the way I do it is by opening the shell of manage.py and
# plugging in: "from hotelManager.models import City \n Cities = City.objects.all()

def funcity(Cities, code_name):
    for City in Cities:
        if City.code_name == code_name:
            return City
