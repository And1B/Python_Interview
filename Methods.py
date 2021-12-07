import random
import os

# reads a given text-file and saves every line into an array.
def read_data(filename):
    with open(filename) as r:
        lines = r.read().splitlines()
    return lines


# generates test_data
def generate_data(filename):
    # this list provides data for the test cases
    fruit_list = ["Apple", "Apples", "Nectarine", "Mango", "Mango's", "Coconut", "Coconuts", "Blueberry", "Blueberries",
                  "Orange", "Oranges"]
    # removes text-file if it already exists
    if os.path.isfile(filename):
        os.remove(filename)

    # Creates lines for a new textfile with random amount of data
    with open(filename, 'x') as w:
        for i in range(len(fruit_list) - random.randrange(1, 7, 1)):
            random_number = random.randrange(0, len(fruit_list), 1)
            w.write(fruit_list.pop(random_number))
            w.write('\n')


# creates a dictionary out of the two lists
# def combine_lists(measured_list, specified_list):
#     if len(measured_list) > len(specified_list):
#         print('list 1 bigger than list 2')
#         merged_list = dict(zip(specified_list, measured_list))
#     elif len(measured_list) < len(specified_list):
#         print('list 1 smaller than list 2')
#         merged_list = dict(zip(specified_list, measured_list))
#     else:
#         merged_list = dict(zip(specified_list, measured_list))
#     return merged_list


# checks for differences in the two provided lists.
# using provided names for clarity, usually it should be list1, list2 so the order doesn't matter.
def check_differences(measured_list, specified_list):
    missing_measured = []
    missing_specified = []
    for element in measured_list:
        if element not in specified_list:
            # print(element)
            missing_specified.append(element)
    for element in specified_list:
        if element not in measured_list:
            # print(element)
            missing_measured.append(element)
    
    if len(missing_measured) > 0:
        print('Measured list is missing these elements from the specified list:', missing_measured)
    else:
        print('All elements of measured list are in the specified list')

    if len(missing_specified) > 0:
        print('Measured list contains elements that are not included in the specified list:', missing_specified)
    else:
        print('All elements of specified list are in the measured list')