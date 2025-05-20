# import csv
# temperature = []
# with open(r"C:\Users\garen\Documents\Project Work\Us states guesser\weather_data.csv") as dateinfo:
#     data = csv.reader(dateinfo)
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print (temperature)
import pandas   # Standard pandas import convention

# data = pandas.read_csv("weather_data.csv")
# day =data[data['temp'] == data['temp'].max()]  # Fixed column access syntax
# tempinF = day.temp * (9/5) + 32
data = pandas.read_csv("data.csv")
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
Red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_count= len(data[data["Primary Fur Color"] == "Black"])

print (grey_count, Black_count , Red_count)
data_dict ={
    "Fur Colours" : ["Grey","Cinnamon","Black"],
    "Count" : [grey_count,Red_count,Black_count]
    }
Squirrels_data =pandas.DataFrame(data_dict)
Squirrels_data.to_csv("New data")