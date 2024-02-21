##
# @file get_csv.py
# @brief This file implements loading list from A column in csv file.
# @author yukinagata3184

import csv

def get_list_from_csv(csv_path, row_num=0):
    """! Get list from A column in csv file.
    @param csv_path [str] Path to the csv file.
    @retval get_list Get list from A column in csv file.
    """
    get_list = []
    with open(csv_path) as f:
        for row in csv.reader(f):
            get_list.append(row[row_num])
    return get_list