import pandas as pd
from openpyxl import Workbook, load_workbook
from os import path, listdir, getcwd
from shutil import copyfile


class ExcelUtility:

    def __init__(self):
        # Get inputs from the user
        self.base_path = path.join('..', 'base')
        self.base_file = listdir(self.base_path)[0]

    # Get all the files to add to the data sheet
    def get_list_of_files_to_add(self):
        files_path = path.join("..", "add")
        return listdir(files_path)

    # First save a backup copy of the file
    def copy_backup_of_base_file(self):
        pass

    # Get the workbook, find the correct worksheet
    def get_base_workbook(self):
        wb = load_workbook(f'../base/{self.base_file}')
        ws = wb.active

        for sheet in wb:
            if sheet.title == "data":
                wb.active = sheet

    # Ensure the column names match; if not, throw an error and let the user
    # know that the columns do not match

    # Ensure the number of column labels matches the number of columns of data.
    # The Amazon ad console export function often exports data in the wrong
    # columns.

    # Find the end of the data in the worksheet so that the new data (more rows)
    # can be appended to the current data.


if __name__ == "__main__":
    # fl = get_list_of_files_to_add()
    # for file in fl:
    #     print(file)
    print("===== How to use this script =====\nOnly one file should be in the "
          "'/base/' directory.\n(This is the base file to which you would like"
          " to append data.)\nBe sure to use the following naming convention "
          "for the 'data' files:\n(YYYYMMDD-YYYYMMDD) where the date before"
          "the hyphen is the start date\nof the data and the date after the"
          "hyphen is the end date of the data.")

    xlu = ExcelUtility()
    xlu.get_base_workbook()

    # Get path of files to operate on

    # Get path
    # input("What is the filename of the base file to which you"
    #       "like to append data? ")
