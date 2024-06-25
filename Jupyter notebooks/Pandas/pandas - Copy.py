import pandas as pd
 
# Function to add
def add_values(row):
    return row['A'] + row['B'] + row['C']
 
def main():
    # Create a dictionary with three fields each
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}
 
    # Convert the dictionary into DataFrame
    df = pd.DataFrame(data)
    print("Original DataFrame:\n", df)
 
    # Apply the user-defined function to every row
    df['add'] = df.apply(add_values, axis=1)
 
    print('\nAfter Applying Function: ')
    # Print the new DataFrame
    print(df)
 
main()