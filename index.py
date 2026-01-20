python
import pandas as pd
import matplotlib.pyplot as plt

# Load the transportation usage dataset
transport_df = pd.read_csv('Public_Transportation_Usage_Abu_Dhabi_2024.csv')

# Load the traffic accident dataset
accident_df = pd.read_excel('Traffic_Accident-v3.0 (values) Abu Dhabi 2024.xlsx')

# Analyze peak usage times in public transportation
peak_times = transport_df.groupby('time')['passenger_count'].sum().sort_values(ascending=False)

# Plot peak usage times
plt.figure(figsize=(10, 6))
plt.title('Peak Public Transportation Usage Times')
peak_times.plot(kind='bar')
plt.xlabel('Time of Day')
plt.ylabel('Passenger Count')
plt.show()

# Analyze accident patterns
accident_patterns = accident_df.groupby('weather_condition')['number_of_accidents'].sum()

# Plot accident patterns based on weather conditions
plt.figure(figsize=(10, 6))
plt.title('Traffic Accidents Based on Weather Conditions')
accident_patterns.plot(kind='bar', color='orange')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Accidents')
plt.show()

# Merge datasets to find correlations
merged_df = pd.merge(transport_df, accident_df, left_on='date', right_on='report_date')

# Correlation analysis between passenger count and number of accidents
correlation = merged_df['passenger_count'].corr(merged_df['number_of_accidents'])
print(f'Correlation between passenger count and number of accidents: {correlation}')
