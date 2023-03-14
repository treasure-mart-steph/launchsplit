import pandas as pd

# Set the input filename
filename = "launch.csv"

# Read in the CSV file
df = pd.read_csv(filename)

# Split the data into three separate data frames based on the sections you described
section1 = df.iloc[:, :10] # replace 10 with the number of columns in section 1
section2 = df.iloc[:, 10:20] # replace 10 and 20 with the start and end column indices for section 2
section3 = df.iloc[:, 20:] # replace 20 with the start column index for section 3

# Save each data frame as a separate CSV file
section1.to_csv('section1.csv', index=False)
section2.to_csv('section2.csv', index=False)
section3.to_csv('section3.csv', index=False)
