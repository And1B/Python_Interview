from Methods import generate_data, read_data, check_differences, SPECIFIEDFILE, MEASUREDFILE

if __name__ == '__main__':
    # generate_data(SPECIFIEDFILE)
    # generate_data(MEASUREDFILE)
    specifiedList = read_data(SPECIFIEDFILE)
    measuredList = read_data(MEASUREDFILE)
    check_differences(measuredList, specifiedList)

