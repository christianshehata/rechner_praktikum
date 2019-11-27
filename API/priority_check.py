"""
This file includes the function to create a priority order!
 1. create a counter for the number of lvs per subject
 2. create a subject list with all lvs per subject
 3. compare all subjects and pick the priority subject based on the frequency
 4. create a second priority based on the frequency of courses per day
 5. make a order by combining priority subject and priority day
"""

import datetime
# from api import data
from api_search import *
from api_preprocessing import *


# count how many lvs of a subject exists:
def counter_subject(data, lv_list):
    comp_list = []
    counter_list = []
    k = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j][1] not in comp_list:
                comp_list.append(data[i][j][1])
                counter_list.append(list())
                counter_list[k].append(data[i][j][1])
                counter_list[k].append(len(lv_list[len(comp_list) - 1]))
                k += 1
    # print(comp_list)
    # print(counter_list)
    return counter_list


# create a order based on the frequency:
def check_freq_sub(counter_list):
    sorted_sub_list = sorted(counter_list, key=lambda x: x[1])
    print('Priority order for subjects: ' + str(sorted_sub_list))
    return sorted_sub_list
