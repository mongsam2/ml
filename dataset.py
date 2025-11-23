import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os


CATEGORY_LIST = ["circle", "diagonal_left", "diagonal_right", "horizontal", "vertical"]


def load_data(data_folder: str):
    """
    data_folder: 데이터 파일이 저장된 폴더 이름 (ex. data1 or data2)
    output: all_data
        - df: dataframe
    """
    all_datas = []
    for category in CATEGORY_LIST:  # 카테고리별로 데이터 수집
        folder_path = os.path.join(data_folder, category)

        # 포즈 하나의 데이터 추출 (ex. circle>1.txt, circle>2.txt)
        for data_id in os.listdir(folder_path):
            data_file_path = os.path.join(folder_path, data_id)
            pose_data = get_pose_data(data_file_path)  # 동작 하나의 데이터
            data_id = data_id.split(".")[0]
            pose_data = [
                [category, int(data_id), time_step, line[0], line[1], line[2]]
                for time_step, line in enumerate(pose_data)
            ]
            all_datas.extend(pose_data)
    # print(f"{len(all_datas)} x {len(all_datas[0])}")

    return pd.DataFrame(
        all_datas, columns=["category", "data_id", "time_step", "x", "y", "z"]
    )


def get_pose_data(file_path):
    """
    하나의 포즈 데이터를 추출하는 함수 (ex. 1.txt, 2.txt, 3.txt ...)
    output:
        [
            (x, y, z),
            (x, y, z),
            ...
        ]
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data_list = f.readlines()

    data_array = []  # 하나의 시계열 데이터
    for line in data_list:
        row = line.split(",")
        # print(f"하나의 행을 인코딩합니다. {row}")
        if len(row) < 7:
            continue
        x, y, z = map(int, row[6].split("/"))
        data_array.append((x, y, z))

    return data_array


def write_data(df, category: str, data_id: int):
    """
    # fig: 그림을 그릴 전체 캔버스 객체
    # pos: subplot 위치 (예: 121, 122)
    """
    series = df[(df["category"] == category) & (df["data_id"] == data_id)]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(series["x"], series["y"], series["z"])
    # plt.show()
    return fig


if __name__ == "__main__":
    df = load_data("data1")
    write_data(df, "circle", "1")
