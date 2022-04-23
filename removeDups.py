import pandas as pd

data = pd.read_csv('test_file.csv')

clean = data.drop_duplicates(subset=['address'])
clean = clean.drop_duplicates(subset=['fname', 'lname'])
clean = clean.drop_duplicates(subset=['email'])
print(clean)

# if firstname and last name are the same between 2 entries
# if email appears more than once
# If an address appears more than once