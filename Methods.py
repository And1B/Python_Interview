import random
import os


def read_data(filename):
    with open(filename) as r:
        lines = r.read().splitlines()
    return lines


def generate_data(filename):
    fruitList = ["Apple", "Apples", "Nectarine", "Mango", "Mango's", "Coconut", "Coconuts", "Blueberry", "Blueberries",
                 "Orange", "Oranges"]
    if os.path.isfile(filename):
        os.remove(filename)
    with open(filename, 'x') as w:
        for i in range(len(fruitList) - random.randrange(1, 7, 1)):
            random_number = random.randrange(0, len(fruitList), 1)
            w.write(fruitList.pop(random_number))
            w.write('\n')


def combine_lists(measured_list, specified_list):
    if len(measured_list) > len(specified_list):
        print('list 1 bigger than list 2')
        merged_list = dict(zip(specified_list, measured_list))
    elif len(measured_list) < len(specified_list):
        print('list 1 smaller than list 2')
        merged_list = dict(zip(specified_list, measured_list))
    else:
        merged_list = dict(zip(specified_list, measured_list))
    return merged_list


def check_differences(measured_list, specified_list):
    missing_measured = []
    missing_specified = []
    for element in measured_list:
        if element not in specified_list:
            # print(element)
            missing_specified.append(element)
    for element in specified_list:
        if element not in measured_list:
            print(element)
            missing_measured.append(element)
    print('Measured list is missing these elements from the specified list:', missing_measured)
    print('Measured list contains elements that are not included in the specified list:', missing_specified)
    # return missing_measured, missing_specified
