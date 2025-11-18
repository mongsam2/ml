import pandas as pd
import os


CATEGORY_LIST = ["circle", "diagonal_left", "diagonal_right", "horizontal", "vertical"]


def load_data():
    """
    load data into pandas dataframe
    """
    for folder_name in ("data1", "data2"):
        for category in CATEGORY_LIST:
            folder_path = os.path.join(folder_name, category)

            for data_file in os.listdir(folder_path):
                data_file_path = os.path.join(folder_path, data_file)
                data = pd.read_csv(data_file_path)
