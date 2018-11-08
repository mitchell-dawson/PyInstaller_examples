#!/usr/bin/env python2

import utils
import sys
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS

    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main():

    print('hello')

    size_tuple = (3, 2)

    print(utils.random_array(size_tuple))

    csv_files = ('MOCK_DATA.csv', 'MOCK_DATA2.csv')

    csv_paths = [os.path.join('data', X) for X in csv_files] 

    csv_paths = [resource_path(X) for X in csv_paths]

    for csv_path in csv_paths:

        print("Reading data from %s" % csv_path)

        print(utils.read_csv_data(csv_path)[:5])


if __name__ == '__main__':
    main()
