from Methods import generate_data, read_data, check_differences

if __name__ == '__main__':
    # generate_data('SpecifiedList.txt')
    # generate_data('MeasuredList.txt')
    specifiedList = read_data('SpecifiedList.txt')
    measuredList = read_data('MeasuredList.txt')
    check_differences(measuredList, specifiedList)

