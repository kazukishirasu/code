import csv

file_path = '/home/kazuki/takashi_ws/src/nav_cloning/data/loss/00_02/4000/'
list = [[],[]]
count = 0

for i in range(1, 31):
    with open(file_path + str(i) + '.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            list[0].insert(i * count, float(row[0]))
            list[1].insert(i * count, count + 1)
            count += 1
    count = 0
with open(file_path + 'com1.csv', 'w') as f:
    writer = csv.writer(f)
    for row in list[1]:
        writer.writerow([row])