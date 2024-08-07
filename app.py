import os

data_file = "./data/data.txt"

if os.path.exists(data_file):
    with open(data_file, 'r') as f:
        count = int(f.read())
else:
    count = 0

count += 1

with open(data_file, 'w') as f:
    f.write(str(count))

print(f"Count is {count}")
