import pandas as pd

# Set the input filename
filename = "input/launch.csv"

# Read in the CSV file, skipping the first row
df = pd.read_csv(filename, skiprows=1)

# Split the data into two separate data frames
section1 = df.iloc[:, 63:115]  # columns 64 to 115
section2 = df.iloc[:, 115:143]  # columns 116 to 143

# Save each data frame as a separate CSV file
section1.to_csv('output/the_launches.csv', index=False)
section2.to_csv('output/data_builder.csv', index=False)
