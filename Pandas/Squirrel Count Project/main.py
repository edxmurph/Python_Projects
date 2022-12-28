# import csv

# with open("Book1.csv") as data:
#     weather_data = csv.reader(data)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas

# data = pandas.read_csv("Book1.csv")
# monday = data[data.day == 'Monday']
# print(monday.temp + 32)

import pandas

data = pandas.read_csv("squirrel_data.csv")
grey_squirrel = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrel = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Count": [grey_squirrel, red_squirrel, black_squirrel]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

# colors = []
# for fur_color in data['Primary Fur Color']:
#     if fur_color not in colors:
#         colors.append(fur_color)

# data_dict = {}
# for color in colors:
#     color_count = len(data[data['Primary Fur Color'] == color])
#     data_dict[color] = color_count

# print(data_dict)