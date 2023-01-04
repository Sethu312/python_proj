
data_list = [ 23, 43, 1, 5, 46, 22, 30, 40, 32, 43 ]
sorted_list = [ ]

while data_list:
    minimum = data_list[0]
    for x in data_list:
        if x < minimum:
            minimum = x
    sorted_list.append(minimum)
    data_list.remove(minimum)
print("data_list", data_list)
print("sorted_list:", sorted_list)
