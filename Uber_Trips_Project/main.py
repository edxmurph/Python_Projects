#To read the dataset
import pandas as pd 

#For visualization
import matplotlib.pyplot as plt

#Read the dataset
uber_df= pd.read_csv("uber_data.csv")
#Display the first 5 records
#uber_df.head(5)

#Display the last 5 records
#uber_df.tail()

#Find the shape of the dataset
#uber_df.shape

#Understand the dataset properties
#uber_df.info()

#Change the "Date/Time" column's data type from string to datetime
uber_df['Date/Time'] = pd.to_datetime(uber_df['Date/Time'])
print(uber_df['Date/Time'])

#Convert "Date/Time" column from string data type into DateTime
uber_df["Day"] = uber_df["Date/Time"].apply(lambda x: x.day)
uber_df["Hour"] = uber_df["Date/Time"].apply(lambda x: x.hour)
uber_df["Weekday"] = uber_df["Date/Time"].apply(lambda x: x.weekday())
uber_df.head(5)

# #TODO: Visualize the Density of rides per Day of month
# fig,ax = plt.subplots(figsize = (12,6))
# plt.hist(uber_df.Day, width= 0.6, bins= 30)
# plt.title("Density of trips per Day", fontsize=16)
# plt.xlabel("Day", fontsize=14)
# plt.ylabel("Density of rides", fontsize=14)


# #TODO: Visualize the Density of rides per Weekday
# fig,ax = plt.subplots(figsize = (12,6))
# plt.hist(uber_df.Weekday, width= 0.6, range= (0, 6.5), bins=7, color= "green")
# plt.title("Density of trips per Weekday", fontsize=16)
# plt.xlabel("Weekday", fontsize=14)
# plt.ylabel("Density of rides", fontsize=14)


# #TODO: Visualize the Density of rides per hour
# fig,ax = plt.subplots(figsize = (12,6))
# plt.hist(uber_df.Hour, width= 0.6, bins=24, color= "orange")
# plt.title("Density of trips per Hour", fontsize=16)
# plt.xlabel("Hour", fontsize=14)
# plt.ylabel("Density of rides", fontsize=14)


# #TODO: Visualize the Density of rides per location
# fig,ax = plt.subplots(figsize = (12,6))
# x= uber_df.Lon
# y= uber_df.Lat
# plt.scatter(x, y, color= "purple")
# plt.title("Density of trips per Hour", fontsize=16)
# plt.xlabel("Hour", fontsize=14)
# plt.ylabel("Density of rides", fontsize=14)


plt.show()