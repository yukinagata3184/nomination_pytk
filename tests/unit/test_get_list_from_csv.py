##
# @file test_get_list_from_csv.py
# @brief Unit tests for get_list_from_csv.py.
# @author yukinagata3184

import pytest
from src import get_csv

def test_get_list_from_csv():
    """! When expected list and got csv list are assert, true is pass a test.
    """
    assert get_csv.get_list_from_csv(csv_path="nominate_list.csv", row_num=0) == \
           ["佐藤", "鈴木", "高橋", "田中", "伊藤"]