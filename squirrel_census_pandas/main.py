import pandas

# data from https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw

# reads data from csv
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# stores only the "primary fur color column" in a series
squirrels_by_color = data["Primary Fur Color"]
# counts the unique values within the series
count_of_squirrels_by_color = squirrels_by_color.value_counts()
# converts result to dataframe
squirrel_color_df = pandas.DataFrame(count_of_squirrels_by_color)
# writes dataframe to csv
squirrel_color_df.to_csv("squirrels_by_color.csv")
