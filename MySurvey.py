import statistics
import pandas

# Read the entire CSV file into a pandas DataFrame
df = pandas.read_csv('MySurvey.csv')

# Filter out the column, value_eur
Name_values = df['Name']
print(Name_values)

Age_values = df['Age']
print(Age_values)

Birthday_values = df['Birthday']
print(Birthday_values)

mean_value = round(statistics.mean(Age_values), 2)
print(mean_value)