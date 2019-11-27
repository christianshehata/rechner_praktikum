try:
    # python2
    from urllib2 import Request, urlopen
except ImportError:
    # python3
    from urllib.request import Request, urlopen

from api_preprocessing import *
from priority_check import *
from api_search import data_search, subject_list
import json
import pprint


url = 'https://bach.wu.ac.at/z/BachAPI/courses/'


# function that return specific information for each lv in list:
def list_iter(lv_list, semester):
    data_list = []
    for i in range(len(lv_list)):
        for j in range(len(lv_list[i])):
            data = {
            'id': lv_list[i][j],
            'method': 'get_events',
            'params': (lv_list[i][j], semester),
            }

            data = json.dumps(data)
            data = data.encode('utf-8')
            headers = {
            'Content-Type': 'application/json-rpc',
            }

            req = Request(url, data, headers)

            resp = urlopen(req)
            data = resp.read()
            data = data.decode('utf-8')

            data = json.loads(data)

            data_list.append(data["result"])
            pprint.pprint(data)
            # print(data["result"])

    # print(data_list)
    return data_list

# ----function calls---- #

subject_inp_list = ['Mathematik', 'Statistik']

filter_data(data_search, subject_inp_list, '19W')

list_iter(filter_data(data_search, subject_inp_list, '19W'), '19W')

time_converter(list_iter(filter_data(data_search, subject_inp_list, '19W'), '19W'))

rem_items(time_converter(list_iter(filter_data(data_search, subject_inp_list, '19W'), '19W')))

counter_subject(rem_items(time_converter(list_iter(filter_data(data_search, subject_inp_list, '19W'), '19W'))),
                filter_data(data_search, subject_inp_list, '19W'))

check_freq_sub(
    counter_subject(rem_items(time_converter(list_iter(filter_data(data_search, subject_inp_list, '19W'), '19W'))),
                    filter_data(data_search, subject_inp_list, '19W')))