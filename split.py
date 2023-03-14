import pandas as pd

# Set the input filename
filename = "input/launch.csv"

# Read in the CSV file, skipping the first row
print("Removing first row...")
df = pd.read_csv(filename, skiprows=1)

# Split the data into two separate data frames
print("Splitting file...")
section1 = df.iloc[:, 63:115]  # columns 64 to 115
section2 = df.iloc[:, 115:143]  # columns 116 to 143

# Save each data frame as a separate CSV file
print("Saving sections...")
section1.to_csv('output/the_launches.csv', index=False)
print("Launches saved.")
section2.to_csv('output/data_builder.csv', index=False)
print("Data builder saved.")

print("Splitting complete!")
