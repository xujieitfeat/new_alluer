import yaml


def analyze_data(file_name, key):
    with open("./data/" + file_name, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        temp_list = list()
        for i in data[key].values():
            temp_list.append(i)

        return temp_list
