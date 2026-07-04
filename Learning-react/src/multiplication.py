data = [15, 7, 30, 45, 8, 60, 3, 20]

for index, value in enumerate(data):

    if value % 5 == 0 and value % 3 == 0:
        print("Index:", index, "Value:", value)