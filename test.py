import pandas as pd

csv = pd.read_csv('16-nodes/_jobs.csv')
print(csv.sort_values('submission_time'))


