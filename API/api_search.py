import ast
import urllib3
urllib3.disable_warnings()

try:
    # python2
    import urllib3
    urllib3.disable_warnings()
except ImportError:
    # python3
    import urllib


def get_data(subjects):
    data_list = []
    k = 0
    for i in range(len(subjects)):
        data_list.append(list())
        for subject in subject_list[i]:
            url = "https://bach.wu.ac.at/z/BachAPI/courses/search?query=" + subject
            pool_manager = urllib3.PoolManager()
            request = pool_manager.request("GET", url)
            content = request.data.decode("utf-8")
            data = ast.literal_eval(content)
            data_list[k].append(data)
        k += 1
    return data_list


# define a list of subjects:
subject_list = [['Mathematik'], ['Statistik']]

data_search = get_data(subject_list)

# print(data_search)