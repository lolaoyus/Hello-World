import csv
from statistics import mean

with open("DATA475_lab_rectangles_data.csv", newline="") as f:
    reader = csv. reader(f)
    next(reader)

    # list comprehension
    areas = [float(line[1]) * float(line[2]) for line in reader]

    # loop
    # areas = []
    # for line in reader:
    #     w = float(line[1])
    #     l = float(line[2])
    #     area = w * l
    #     areas. append(area)
    # make a change

    
print(max(areas))
print(min(areas))
print(sum(areas))
print(mean(areas))
print(len(areas))


columns_names = {
    "Total Count": len(areas),
    "Total Area": sum(areas),
    "Ave area": mean(areas),
    "Max area": max(areas),
    "Min area": min(areas),
}

for key, value in column_names.iteams():
    print(f"{key}: {value}")

with open("summary.csv", "w", newlines"") as f:
    writer = csv.writer(f)
    writer.writerow(column_names.keys())
    writer.writerow(column_names.values())




    
    




















