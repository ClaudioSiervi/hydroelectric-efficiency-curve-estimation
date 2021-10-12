from typing import Tuple

from pandas import DataFrame, read_excel
from os import path


def read_hill_curve(
        sheet_name: str = "THG1",
        PATH_DATASET: str = "PATH-TO-FOLDER/hydroelectric-efficiency-curve-estimation/src/data/",
        WORKBOOK_NAME: str = "DadosExperimento.xls",
) -> DataFrame:
    """The dataset is in Excel (.xls),
    each sheet of the workbook is a hydropower turbine,
    with Hill Curve data: "net head", "flow", "efficiency. """

    file_path = path.join(PATH_DATASET, WORKBOOK_NAME)

    uhe_thg = read_excel(file_path, sheet_name=sheet_name)
    uhe_thg.columns = ["queda", "vazao", "rendimento"]

    return uhe_thg


def read_hill_curve_dataset() -> Tuple[DataFrame]:

    # The experiment uses only four datasets
    uhe1_data = read_hill_curve(sheet_name="THG1")
    uhe2_data = read_hill_curve(sheet_name="THG2")
    uhe3_data = read_hill_curve(sheet_name="THG3")
    uhe4_data = read_hill_curve(sheet_name="THG4")

    uhe1_data.columns = ["queda", "vazao", "rendimento"]
    uhe2_data.columns = ["queda", "vazao", "rendimento"]
    uhe3_data.columns = ["queda", "vazao", "rendimento"]
    uhe4_data.columns = ["queda", "vazao", "rendimento"]

    return uhe1_data, uhe2_data, uhe3_data, uhe4_data

