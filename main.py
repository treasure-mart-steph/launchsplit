import pandas as pd

# Set the input filename
filename = "input/launch.csv"

# Read in section 1
print("Extracting section 1...")
section1 = pd.read_csv(filename, skiprows=[0, 2], usecols=range(64, 116))

# Read in section 2
print("Extracting section 2...")
section2 = pd.read_csv(filename, skiprows=[0, 2], usecols=range(116, 143))

# Save each data frame as a separate CSV file
print("Saving sections...")
section1.to_csv('output/the_launches.csv', index=False)
print("Launches saved.")
section2.to_csv('output/data_builder.csv', index=False)
print("Data builder saved.")

print("Splitting complete!")
