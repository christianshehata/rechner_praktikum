'''
Some steps to clean the data.
'''

from api_search import data_search
# from api import list_iter <-- import error
import datetime


# filter thru all data and create a list with just the important information(all lvs with title):
def filter_data(data, subject_list, semester):
    list_data = []
    k = 0
    for l in range(len(data)):
        list_data.append(list())
        for i in range(len(data[l])):
            for j in range(len(data[l][i])):
                if data[l][i][j][2] in subject_list and data[l][i][j][0] == semester:
                    list_data[k].append(data[l][i][j][1])
        k += 1
    # print(list_data)
    return list_data


# converting a string into datetime:
def time_converter(input_list):  # problem: no week days
    format_time = '%Y-%m-%dT%H:%M:%S'
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            input_list[i][j][5] = datetime.datetime.strptime(input_list[i][j][5], format_time)
            input_list[i][j][6] = datetime.datetime.strptime(input_list[i][j][6], format_time)
    # print(input_list)
    return input_list


# remove room and building:
def rem_items(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            del (data[i][j][3:5])
            del (data[i][j][0])
    # print(data)
    return data


# print(data_search)
# print(filter_data(data_search, 'Mathematik', 'W19'))

#list_iter(filter_data(data_search, 'Mathematik', '19W'), '19W')

# rem_items(time_converter(list_iter(filter_data(data_search, 'Mathematik', '19W'), '19W')))
